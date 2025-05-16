def calculate_bmi(height,weight):
    print("Height= ",height)
    print("Weight=", weight)
    bmi = weight/(height*height)
    print("BMI" +str(bmi))
    return bmi

def classify_bmi(bmi):
    if(bmi< 18.5):
        print("Underweight")
        return -1 
    elif(bmi>=18.5 and bmi<=25):
        print("Normal Weight")
        return 0
    else:
        print("Overweight,excerise!!!!")
        return 1
    return  

def app():
    output =calculate_bmi(1.78,65)
    print(classify_bmi(output))

def figuring_out():
    print("Hi wassup")

bmi_main = app()
print(bmi_main)
#tonights the night by dexter morgan