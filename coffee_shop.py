SMALL_SIZE = 9
MEDIUM_SIZE = 12
LARGE_SIZE = 15

SMALL_PRICE = 1.75
MEDIUM_PRICE = 1.90
LARGE_PRICE = 2.00


def print_menu():
    print("\nCoffee Shop Management System")
    print("1. Order coffee")
    print("2. Check total money made")
    print("3. Check total coffee sold")
    print("4. Check number of cups sold")
    print("5. Print sales data")
    print("9. Exit")


def order_coffee(small_cups, medium_cups, large_cups, total_money, total_coffee):
    order_total = 0

    while True:
        print("\n1. Small coffee - $1.75")
        print("2. Medium coffee - $1.90")
        print("3. Large coffee - $2.00")
        print("9. Finish order")

        choice = input("Enter your choice: ")

        if choice == "1":
            small_cups += 1
            total_money += SMALL_PRICE
            total_coffee += SMALL_SIZE
            order_total += SMALL_PRICE
            print("Small coffee added.")
        elif choice == "2":
            medium_cups += 1
            total_money += MEDIUM_PRICE
            total_coffee += MEDIUM_SIZE
            order_total += MEDIUM_PRICE
            print("Medium coffee added.")
        elif choice == "3":
            large_cups += 1
            total_money += LARGE_PRICE
            total_coffee += LARGE_SIZE
            order_total += LARGE_PRICE
            print("Large coffee added.")
        elif choice == "9":
            print(f"Order total: ${order_total:.2f}")
            return small_cups, medium_cups, large_cups, total_money, total_coffee
        else:
            print("Invalid choice. Please try again.")


def check_total_money(total_money):
    print(f"Total money made: ${total_money:.2f}")


def check_total_coffee(total_coffee):
    print(f"Total coffee sold: {total_coffee} oz")


def check_cups_sold(small_cups, medium_cups, large_cups):
    print(f"Small cups sold: {small_cups}")
    print(f"Medium cups sold: {medium_cups}")
    print(f"Large cups sold: {large_cups}")
    print(f"Total cups sold: {small_cups + medium_cups + large_cups}")


def print_data(small_cups, medium_cups, large_cups, total_money, total_coffee):
    print("\nSales Summary")
    print("-" * 30)
    check_cups_sold(small_cups, medium_cups, large_cups)
    check_total_coffee(total_coffee)
    check_total_money(total_money)


def main():
    small_cups = 0
    medium_cups = 0
    large_cups = 0
    total_money = 0
    total_coffee = 0

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            small_cups, medium_cups, large_cups, total_money, total_coffee = order_coffee(
                small_cups,
                medium_cups,
                large_cups,
                total_money,
                total_coffee
            )
        elif choice == "2":
            check_total_money(total_money)
        elif choice == "3":
            check_total_coffee(total_coffee)
        elif choice == "4":
            check_cups_sold(small_cups, medium_cups, large_cups)
        elif choice == "5":
            print_data(small_cups, medium_cups, large_cups, total_money, total_coffee)
        elif choice == "9":
            print("Thank you for using the Coffee Shop Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
