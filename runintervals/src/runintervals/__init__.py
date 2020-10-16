def __init__(self, runsNumber=5, runsLength=5, breakLength=1, currentStatus='inactive', displayTime=0, runStartTime=0):
    """
    Instantiate runsNumber, runsLength, & breakLength, so these can be
    taken from the user.
    These values are the only vars in scope throughout the class
    """
    self.runsNumber = runsNumber
    self.runsLength = runsLength
    self.breakLength = breakLength
    self.currentStatus = currentStatus
    self.displayTime = displayTime
    self.runStartTime = runStartTime
