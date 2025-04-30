def get_user_input(numb):
    x=numb.split()
    print(x)
    return x

number = input("Input the numbers you want in a string format: ")

idnt = get_user_input(number) 
float_list=[]
for item in idnt:
    float_list.append(float(item))
print("List of floats:", float_list)


 #float_list = [float(element) for element in idnt]