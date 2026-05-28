# Ejemplo 2 condicional if

numero = input("Introduzca el puntaje del alumno (0-100): ")

if float(numero) > 90:
    print("La calificación del alumno es A")
elif float(numero) > 80:
    print("La calificación del alumno es B")
elif float(numero) > 60 :
    print("La calificación del alumno es C")
else:
    print("El alumno ha reprobado.")

