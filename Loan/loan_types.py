from loan_base import *

# This class will behave exactly the same as the loan base class and
# therefor will just called the loan base class init function and
# provide no extra functionality
class FixedRateLoan(Loan):
    def __init__(self, face, rate, term, asset):
        super().__init__(face, rate, term, asset)


# This class will call the loan base init function but with a None rate,
# the rate will be detretrmined by the passed in dictionary of rates
class VariableRateLoan(Loan):
    def __init__(self, face, rateDict, term, asset):
        super().__init__(face, None, term, asset)
        self._rateDict = rateDict
    
    @property
    def rateDict(self):
        return self._rateDict
    
    @rateDict.setter
    def rateDict(self, input_rateDict)
        self._rateDict = input_rateDict
    
    def getRate(self, period):
        return self._rateDict[period]

    def setRate(self, period, rate):
        self._rateDict[period] = rate

    # Overriding these formulas from the base class because they are different for
    # vairbale rate loans opposed to fixed rate loan
    def monthlyPayment(self, period):
        face = self._face
        rate = self.monthlyRate(self._rateDict[period])
        term = self._term
        return self.calculateMonthlyPayment(face, rate, term, period)

    def interestDue(self, period):
        rate = self.monthlyRate(self._rateDict[period])
        balance = self.balance(period)
        return balance * rate

    def balance(self, period):
        face = self._face
        rate = self.monthlyRate(self._rateDict[period])
        term = self._term
        return self.calculateBalance(face, rate, term, period)

