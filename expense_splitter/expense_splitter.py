from exceptions import (
    InvalidBillAmountError,
    InvalidPeopleCountError,
    InvalidTipPercentage,
)


def calculate_total_bill(
    bill_amount: float,
    tip_percentage: float
) -> float:
    
    if bill_amount <= 0:
        raise InvalidBillAmountError(
            "Bill amount must be greater than zero."
        )

    if tip_percentage < 0:
        raise InvalidTipPercentage(
            "Tip percentage cannot be negative."
        )

    tip_amount = bill_amount * tip_percentage / 100
    total_bill = bill_amount + tip_amount

    return round(total_bill, 2)


def calculate_split_amount(
    bill_amount: float,
    number_of_people: int,
    tip_percentage: float = 0
) -> float:

    if number_of_people <= 0:
        raise InvalidPeopleCountError(
            "Number of people must be greater than zero."
        )

    total_bill = calculate_total_bill(
        bill_amount=bill_amount,
        tip_percentage=tip_percentage
    )

    amount_per_person = total_bill / number_of_people

    return round(amount_per_person, 2)