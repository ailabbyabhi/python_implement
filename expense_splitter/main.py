from expense_splitter import calculate_split_amount
from exceptions import (
    InvalidBillAmountError,
    InvalidPeopleCountError,
    InvalidTipPercentage,
)


def display_split_result(
    bill_amount: float,
    number_of_people: int,
    tip_percentage: float
) -> None:
    
    try:
        amount_per_person = calculate_split_amount(
            bill_amount=bill_amount,
            number_of_people=number_of_people,
            tip_percentage=tip_percentage
        )

        print("Expense split successful")
        print(f"Bill amount: ₹{bill_amount}")
        print(f"Number of people: {number_of_people}")
        print(f"Tip percentage: {tip_percentage}%")
        print(f"Each person should pay: ₹{amount_per_person}")

    except InvalidBillAmountError as error:
        print(f"Invalid bill amount: {error}")

    except InvalidPeopleCountError as error:
        print(f"Invalid people count: {error}")

    except InvalidTipPercentage as error:
        print(f"Invalid tip percentage: {error}")


def main() -> None:
    expense_scenarios = [
        {
            "bill_amount": 1200,
            "number_of_people": 4,
            "tip_percentage": 10
        },
        {
            "bill_amount": 850,
            "number_of_people": 3,
            "tip_percentage": 5
        },
        {
            "bill_amount": 0,
            "number_of_people": 4,
            "tip_percentage": 10
        },
        {
            "bill_amount": 1500,
            "number_of_people": 0,
            "tip_percentage": 5
        },
        {
            "bill_amount": 2000,
            "number_of_people": 5,
            "tip_percentage": -10
        },
    ]

    for scenario in expense_scenarios:
        display_split_result(
            bill_amount=scenario["bill_amount"],
            number_of_people=scenario["number_of_people"],
            tip_percentage=scenario["tip_percentage"]
        )


if __name__ == "__main__":
    main()