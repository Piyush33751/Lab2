def calculate_bmi(height,weight):
    print("Height")
    print("Weight")
    bmi = weight/(height*height)
    print("BMI" +str(bmi))
    return bmi

def classify_bmi(bmi):
    if(bmi< 18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<=25):
        print("Normal Weight")
    else:
        print("Overweight,excerise!!!!")
    return  

def app():
    output =calculate_bmi(1,7,60)
    classify_bmi(output)
    return


calculate_bmi(10,20)

print