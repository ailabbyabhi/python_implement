class InvalidBillAmountError(Exception):
    '''Raised when the bill amount is invalid'''
    pass

class InvalidPeopleCountError(Exception):
    '''Raised whent he no of people are invalid'''
    pass

class InvalidTipPercentage(Exception):
    '''Raised when the tip percentage is invalid'''
    pass