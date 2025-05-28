def multiply_addition(a, b, c):
    return (a * b + c)

def get_valid_number(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be blank.")
        elif not value.isdigit():
            print("Please enter a valid number.")
        else:
            return int(value)

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            return answer
        print("Please enter 'yes' or 'no'.")

while True:
    order = []
    cost = 0.0

    while True:
        lemonade = input("What type of lemonade would you like? regular, strawberry, watermelon, blackberry? ").strip().lower()
        if lemonade in ["regular", "strawberry", "watermelon", "blackberry"]:
            break
        else:
            print("Please choose regular, strawberry, watermelon, or blackberry.")

    while True:
        size = input("What size? (small, medium, large) ").strip().lower()
        if size in ["small", "medium", "large"]:
            break
        else:
            print("Please enter small, medium, or large.")

    number = get_valid_number("How many? ")
    order.append(f"You ordered {number} {size} {lemonade} lemonades")

    lemonade_prices = {
        "regular": {"small": 1.50, "medium": 2.00, "large": 2.50},
        "strawberry": {"small": 1.80, "medium": 2.30, "large": 2.80},
        "watermelon": {"small": 1.80, "medium": 2.30, "large": 2.80},
        "blackberry": {"small": 1.80, "medium": 2.30, "large": 2.80},
    }
    cost = multiply_addition(lemonade_prices[lemonade][size], number, cost)

    ice = get_yes_no("Would you like ice? (yes or no) ")
    if ice == "yes":
        ice_number = get_valid_number("How many ice cubes per drink? ")
        order.append(f"Added {ice_quantity} ice cubes per drink")

    dried_fruit = get_yes_no("Would you like dried fruit? (yes or no) ")
    if dried_fruit == "yes":
        dried_fruit_number = get_valid_number("How many dried fruit pieces per drink? ")
        cost = multiply_addition(0.75, number, cost)
        order.append(f"Added {dried_fruit_quantity} dried fruit pieces per drink")

    if number > 2:
        cost -= 0.50
        order.append("You got a $0.50 discount for ordering more than two drinks!")

    print("\nThis is your total order:")
    for item in order:
        print("-", item)

    print(f"Your total cost is: ${round(cost, 2)}")

    reorder = get_yes_no("Do you want to restart your order? (yes or no) ")
    if reorder == "yes":
        print("\nStarting over...\n")
        continue
    else:
        print("Thank you for your order!")
        break


