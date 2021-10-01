# James Shaw
# receipt.py
# 9/20/21

# Use string formatting to insert the name variable into the subsequent input strings
food_name1 = input("Input the name of a food item: ")
food_price1 = float(input(f"Input the price of the {food_name1}: "))
food_quantity1 = int(input(f"Input the quantity of the {food_name1}: "))

food_name2 = input("Input the name of a second food item: ")
food_price2 = float(input(f"Input the price of the {food_name2}: "))
food_quantity2 = int(input(f"Input the quantity of the {food_name2}: "))

# Calculate total before gratuity
total = food_price1 * food_quantity1 + food_price2 * food_quantity2
gratuity = total * 0.15

# Using string formatting as asked by the assignment, but using identifiable argument names.
# When using the "{}" format in a normal string, arguments are created at those spaces, you can name the argument for
# the later .format() statement so that it's more readable for you or anyone else reading your code.
# As the arguments are being defined in the .format() statement, you may do the required work for that argument
# within the statement.
# Here, I also spaced the arguments vertically for readability with newlines.
# To name arguments in this kind of format, the name comes before the : in the {name:.2f} characters.
# Arguments when defined in the .format() statement are not beholden to appear in the order where they appear in the string,
# as long as the argument is given a name.
print("""
RECEIPT
{a:} {b:} @ ${c:.2f} = ${d:.2f}
{e:} {f:} @ ${g:.2f} = ${h:.2f}
Total cost: ${total_cost:.2f}

15% gratuity: ${i:.2f}
Total with tip: ${j:.2f}""".format(
    a=food_quantity1,
    b=food_name1,
    c=food_price1,
    d=food_price1 * food_quantity1,
    e=food_quantity2,
    f=food_name2,
    g=food_price2,
    h=food_price2 * food_quantity2,
    i=gratuity,
    j=total + gratuity,
    total_cost=total
))
