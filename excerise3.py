def get_user_input(numb):
    x=numb.split()
    print(x)
    return x
number = input("Input the numbers you want in a string format: ")

idnt = get_user_input(number)  # Now idnt will be a list, not None

float_list = [float(element) for element in idnt]

print("List of floats:", float_list)