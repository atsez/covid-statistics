
#enter your hight in meter

#enter your weight in kilogram

while True :

    height = float(input('enter your height: '))
    weight =int(input("enter your weight: "))

    BMI = weight / height ** 2

    if BMI >= 17.9 and BMI <= 23.1 :
        print(BMI)
        print('normal')

    elif BMI < 17.9 : 
        print(BMI)
        print('underweight')

    elif BMI > 23.1 :
        
        print(BMI)
        print('overweight')

    elif BMI >= 24.2 :

        print(BMI)
        print('obese class 1 (severely obese')