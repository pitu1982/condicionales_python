# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5
if numero_1 >= 5:
    print("numero_1 es mayor a 5")

#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
if numero_2 > 0:
    print(' numero_2 es positivo')
elif numero_2 < 0:
    print('numero_2 es negativo')
else:
    print('numero_2 es 0')

#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"

print('el resultado de la negacion es ="Resp=1"')

#  --> En caso negativo (numero_1 no es mayor a 5)

if not(numero_1 > 5):
    print('numero_1 ={} no es mayor a 5 ={}'.format(numero_1,5))  
else:
    print('5 = {} no es mayor a numero_1 ={}'.format(5,numero_1))


#      verifique si el numero_2 es mayor a 5
if numero_2 >= 5:
    print("numero_2 es mayor a 5")



#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

print(' el resultado de la negacion es="Resp=4"')

# Verifique la calificación de un estudiante según su
# puntaje en un examen
puntaje = 70

# Si el puntaje es mayor igual a 90 --> imprimir A
# Si el puntaje es mayor igual a 80 --> imprimir B
# Si el puntaje es mayor igual a 70 --> imprimir C
# Si el puntaje es mayor igual a 60 --> imprimir D
# Si el puntaje es menor a  60      --> imprimir F

if puntaje >= 90:
    print(" puntaje es mayor o igual a 90,  A")

if puntaje >= 80:
    print(" puntaje es mayor o igual a 80,  b")

if puntaje >= 70:
    print(" puntaje es mayor o igual a 70,  c")

if puntaje >= 60:
    print(" puntaje es mayor o igual a 60,  d")
    
if puntaje < 60:
    print(" puntaje es menor 60,  f")




# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados
