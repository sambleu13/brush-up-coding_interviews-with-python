def exclusive_products(inventory1, inventory2):
    # implement this
    inventory1 = [product.upper() for product in inventory1]
    inventory2 = [product.upper() for product in inventory2]
    inv1 = set(inventory1)
    inv2 = set(inventory2)
    unique_in_1 = inv1 - inv2
    unique_in_2 = inv2 - inv1
    return (sorted(list(unique_in_1)), sorted(list(unique_in_2)))

inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
