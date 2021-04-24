import math


r = float(input('Enter circle radius in m: '))

area = round(pow(r,2) * math.pi)
cir = round(2 * math.pi * r)

print(f'The circle area is: {area} m^2\nThe circle circumference is: {cir} m')

