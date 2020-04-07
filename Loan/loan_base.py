# Loan Base Class

import numpy as np

from Asset.asset import *


class Loan(object):
    def __init__(self, face, rate, term, asset):
        self._face = face
        self._rate = rate
        self._term = term
        # Checking if the passed in asset parameter is actually an instance
        # of the Asset class declared in Asset/asset.py
        # giving the option for (or None) for testing purposes 
        # in Tests/Loan_Tests/loan_base_test.py
        if isinstance(asset, Asset) or asset is None:
            self._asset = asset
        else:
            raise Exception("This is not an asset!")
        self._default = False

##################################
#   Property Getter & Setters
##################################
    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, input_face):
        self._face = input_ace

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, input_rate):
        self._rate = input_rate

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, input_term):
        self._term = input_term

##################################
#           Regular Methods
##################################
    # Calculate the monthly payment amount for a given period
    def monthlyPayment(self, period):
        if period < 1 or period > 360:
            return 0
        else:
            face = self._face
            # Call to static method for monthly rate
            rate = self.monthlyRate(self._rate)
            term = self._term
            default = self._default
            # Call to class method for monthly payment
            # Checking if loan defaulted
            return self.calculateMonthlyPayment(face, rate, term, period) if not default else 0

        
    # Calculating the total payments that will be made over the entire life of the loan
    def totalPayment(self):
        totalPayment = 0
        term = self._term
        for t in range(1, term + 1):
            totalPayment += self.monthlyPayment(t)
        return totalPayment

    #Calculating the total intetest that will paid over the entire life of the loan
    def totalInterest(self):
        # Call to method for total payments 
        return self.totalPayment() - self._face

    # Calculating interest due at a given period
    def interestDue(self, period):
        if period < 1 or period > 360:
            return 0
        else:
            rate = self.monthlyRate(self._rate)
            # Call to method for current balance
            balance = self.balance(period)
            return balance * rate

    # Calculating principal due at a given period
    def principalDue(self, period):
        period -= 1
        # Call to regualar method which calls to class method for monthly payment
        # at given period
        monthlyPayment = self.monthlyPayment(period)
        # Calls to method for interest due at given period
        interestDue = self.interestDue(period)
        return monthlyPayment - interestDue

    # Calculating balance of loan at a given period
    def balance(self, period):
        if period < 1:
            return self._face
        else:
            face = self._face
            # Calling to static method
            rate = self.monthlyRate(self._rate)
            term = self._term
            default = self._default
            # Calling to class method for balance, and checking if loan defaulted
            return self.calculateBalance(face, rate, term, period) if not default else 0

    def loanInfo(self, period):
        interestDue = self.interestDue(period)
        principalDue = self.principalDue(period)
        faceBalance = self.balance(period)
        # returning loan information as array
        return [interestDue, principalDue, faceBalance]

    # Calculating recovery value on defaulted debt
    def recoveryValue(self, period):
        # Call to Asset class method
        return self._asset.currentValue(period) * 0.6
        
    # Caluclating equity of loan at given period 
    def equity(self, period):
        loanValue = self.balance(period)
        # Call to Asset class method
        assetValue = self._asset.currentValue(period)
        return assetValue - loanValue

    # Going to use random numbers to pass in to simualte loans defaulting
    def checkDefault(self, period, number):
        recoveryValue = 0
        if number == 0:
            self._default = True
            # Call to Asset class method
            recoveryValue += self._asset.recoveryValue(period)
        return recoveryValue

    # For undefaulting loans
    def resetDefault(self):
        self._default = False
    
##################################
#        Class Level Methods
##################################
    @classmethod
    def calculateMonthlyPayment(cls, face, rate, term, period):
        return rate * face / (1 - (1 + rate) ** (-term))

    @classmethod
    def calculateBalance(cls, face, rate, term, period):
        balance = face * (1 + rate) ** period
        balance -= cls.calculateMonthlyPayment(face, rate, term, period) * ((1 + rate) ** period - 1) / rate
        return max(balance, 0)

##################################
#        Static Level Methods
##################################

    @staticmethod
    def monthlyRate(annualRate):
        return annualRate / 12

    @staticmethod
    def annualRate(monthlyRate):
        return monthlyRate * 12