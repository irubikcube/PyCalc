# se inician con una F mayuscula o minuscula, seguido de comillas simples o dobles
# tambien usan {} para indicar el final de la cadena

username = "cristian"
print (f"hola como estas {username}")

# lo que esta dentro de las comillas se imprimira tal cual como esta escrito, siendo esa conocida como la parte literal

#esto es en el caso del dolar
precio_unitario = 49.90
cantidad = 30
print (f"el precio total es de ${precio_unitario * cantidad:,.2f} pesos")

#esto es para el perso chileno
#:,.0f → Formatea con 0 decimales y separa los miles con coma.
#	•	.replace(",", ".") → Cambia la coma por punto, para seguir el formato chileno.
#	•	El número 49990 en este caso representa 49.990 CLP (sin decimales).

precio_unitario = 3990
cantidad = 34
total = precio_unitario * cantidad + iva
iva = 0,19

print(f"el precio final a pagar es de ${total:,.0f} pesos".replace (",", "."))
