# change k to l and l - k

weight = float(input("Enter Your weight: ")) # input weight

unit = input('Enter your unit: ') # k or lbs

if(unit == 'k'):
    weight = weight * 2.205
    unit = 'lbs'

elif(unit == 'lbs'):
    weight = weight / 2.205
    unit = 'k'

else:
    print(f'{unit} is not valid')

print(f'Your Weight is {round(weight,3)} {unit}')

