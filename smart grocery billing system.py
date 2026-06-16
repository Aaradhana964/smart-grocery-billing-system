# Product Dictionary
products = {
    "apple": 50,
    "milk": 30,
    "bread": 40,
    "eggs": 60
}

# Input
user_input = input("Enter products: ")

# Clean Input
items = user_input.strip().lower().split(",")

clean_list = []

for item in items:
    clean_list.append(item.strip())

# Validate Products
cart = []
invalid = []

for item in clean_list:

    if item in products:
        cart.append(item)

    else:
        invalid.append(item)

# Remove Duplicates for Printing
unique_items = []

for item in cart:

    if item not in unique_items:
        unique_items.append(item)

# Invoice
print("\n------ INVOICE ------")

total = 0

for item in unique_items:

    # Count quantity using count()
    quantity = cart.count(item)

    price = products.get(item)

    item_total = quantity * price

    total += item_total

    # Show format: Apple x2 = ₹100
    print(item.capitalize(), "x" + str(quantity), "= ₹" + str(item_total))

# Final Total
print("\nTotal Bill = ₹", total)

# Invalid Items
if invalid:

    print("\nUnavailable Items:")

    for item in invalid:
        print(item.capitalize())