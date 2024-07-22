import datetime


def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in the format: dd/mm/yyyy")


def main():
    today = datetime.datetime.now()

    print("Enter the date in the format: dd/mm/yyyy")
    date = get_date_input("Please enter the date: ")

    difference = today - date

    print(f"The difference is {difference.days} days.")


if __name__ == "__main__":
    main()
