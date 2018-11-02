weight_of_package = input("Enter the weight of the package:")
weight_of_package = int(weight_of_package)
if weight_of_package < 2:
    charge_of_order = weight_of_package*1.5
    print("The shipping charge is:", charge_of_order)
elif weight_of_package > 2 and weight_of_package < 6:
    charge_of_order = weight_of_package*3
    print("The shipping charge is:", charge_of_order)
elif weight_of_package > 6 and weight_of_package < 10:
    charge_of_order = weight_of_package*4
    print("The shipping charge is:", charge_of_order)
else:
    charge_of_order = weight_of_package*4.75
    print("The shipping charge is:", charge_of_order)