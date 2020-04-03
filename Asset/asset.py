# Base Asset Class

class Asset(object):
    def __init__(self, initialValue, depreciationRate):
        self._initialValue = initialValue
        self._depreciationRate = depreciationRate

##################################
#   Property Getter & Setters
##################################

    @property
    def initialValue(self):
        return self._initialValue

    @initialValue.setter
    def initialValue(self, initialValue):
        self._initialValue = initialValue

    # To be implemented in derived classed (car & house classes)
    @property
    def depreciationRate(self):
        raise NotImplementedError()

    @depreciationRate.setter
    def depreciationRate(self, depreciationRate):
        self._depreciationRate = depreciationRate
    
##################################
#   Regular Methods
##################################
    
    # Calculates current value of asset by subtracting total depreciation thus far
    def currentValue(self, period):
        depreciationRate = self.monthlyDepreciationRate(self._depreciationRate)
        totalDepreciation = (1 - depreciationRate) ** period
        currentValue = self._initialValue * totalDepreciation
        return currentValue

    def recoveryValue(self, period):
        recoveryValue = self.currentValue(period) * 0.6
        return recoveryValue

##################################
#   Static Level Methods
##################################

    @staticmethod
    def monthlyDepreciationRate(annualDepreciationRate):
        monthlyDepreciationRate = annualDepreciationRate / 12
        return monthlyDepreciationRate

    @staticmethod
    def annualDepreciationRate(monthlyDepreciationRate):
        annualDepreciationRate = monthlyDepreciationRate * 12
        return annualDepreciationRate