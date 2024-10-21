'''  En este vídeo vamos a resolver el ejercicio 4, donde calcularemos el área y longitud
de una circunferencia.'''

# Area = 3.14 * r**2
# longitud 2 * 3.14 * r
#
import math  ## debo solicitar la exportación de match que es donde se guarda PI 0 3.14...

radio = float(input("radio ->  "))

## Area = 3.14 * radio**2   << mi solución
## longitud = 2 * 3.14 * radio  << mi solución

Area = math.pi * radio**2
longitud = 2 * math.pi * radio


print(f"EL valor del area es: {Area: .2f} ")
print(f"EL valor de la longitud es: {longitud: 2f} ")



