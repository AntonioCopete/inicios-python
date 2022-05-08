'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''


def calculaImpuesto():

    bruto = float(input("Introduzca el importe: "))
    impuesto = int(input("Introduzca el impuesto: "))

    if impuesto == 0 :
        return bruto + bruto*21/100
    
    else:
        
        return bruto + bruto*impuesto/100
        


print(calculaImpuesto())