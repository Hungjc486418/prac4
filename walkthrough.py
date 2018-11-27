def main():
    """Display income report for incomes over a given number of months."""
    incomes, months = count_month()

    print("\nIncome Report\n-------------")
    report_income(incomes, months)


def report_income(incomes, months):
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def count_month():
    incomes = []
    months = int(input("How many months? "))
    for month in range(1, months + 1):
        income = float(input("Enter income for month {} ".format(month)))
        incomes.append(income)
    return incomes, months


main()