import sys
sys.path.append('../../')
from Loan.loan_base import *

# this is just for testing the loan_base, we will not initialize with asset
# for this test
l = Loan(100000, .05, 360, None)

# period parameter doesnt really matter or this case
print '\nTesting Monthly Payment'
print 'This Should Return $536.82...'
print l.monthlyPayment(44)

print '\nTesting Total Payment'
print 'This Should Return $536.82... * 360 months = $193,255.784...'
print l.totalPayment()

print '\nTesting Total Interest'
print 'This Should Return $193,255.784... - the $100,000 face value = 93,255.784...'
print l.totalInterest()

print '\nTesting Intrest Due at various periods'
print 'This Should Return 416.67...'
print l.interestDue(1)
print 'This Should Return 412.08...'
print l.interestDue(10)
print 'This Should Return 331.37...'
print l.interestDue(130)
print 'This Should Return 2.22...'
print l.interestDue(360)

print '\nTesting Principal Due at various periods'
print 'This Should Return 120.15...'
print l.principalDue(1)
print 'This Should Return 124.73...'
print l.principalDue(10)
print 'This Should Return 205.44...'
print l.principalDue(130)
print 'This Should Return 534.59...'
print l.principalDue(360)

print '\nTesting balance at various periods'
print 'This Should Return 120.15...'
print l.balance(1)
print 'This Should Return 124.73...'
print l.balance(10)
print 'This Should Return 205.44...'
print l.balance(130)
print 'This Should Return 534.59...'
print l.balance(360)

