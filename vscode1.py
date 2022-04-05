h=float(input("enter height"))
w=float(input("Enter weight"))
bmi=w/(h*h)
print("bmi="+bmi)
if(bmi<18.5):
    print("underweight")
elif(bmi>18.5 and bmi<24.9):
    print("Healthy")
elif(bmi>25 and bmi<29.9):
    print("overweight")
else:
    print("Obese")