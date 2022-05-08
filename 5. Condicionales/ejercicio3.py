'''
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

'''

primera = input("Introduzca la primera palabra: ")
segunda = input("Introduzca la segunda palabra: ")

if(primera[-3: ] == segunda[-3: ]):
    print("Riman")
elif primera[-2: ] == segunda[-2: ]:
    print("Riman un poco")
else:
    print("No riman")