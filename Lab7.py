# i. Function to calculate total inventory value
def total_inventory(products):
    inventory = {}
    for product in products:
        name = product['name']
        price = product['price']
        quantity = product['quantity']
        inventory[name] = price * quantity
    return inventory

# ii. Function to calculate grade based on total marks
def calculate_grade(total_marks):
    if total_marks >= 90:
        return 'A'
    elif total_marks >= 80:
        return 'B'
    elif total_marks >= 70:
        return 'C'
    elif total_marks >= 60:
        return 'D'
    else:
        return 'F'
