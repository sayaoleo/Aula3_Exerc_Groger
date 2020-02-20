import math as mt

def circle_area(radius_circle):
    area = (radius_circle ** 2) * mt.pi
    return print('Área do círculo é: ', area)
   
def circle_compr(radius_circle):
    compr = 2 * mt.pi * radius_circle
    return print('Comprimento do círculo é: ', compr)

try:
    radius_circle = float(input('Insert the circle s radius: '))
    circle_area(radius_circle)
    circle_compr(radius_circle)
except:
    radius_circle=0
    print('Digite um número para o raio')





