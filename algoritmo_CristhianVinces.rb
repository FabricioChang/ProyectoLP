
#Cristhian Vinces
# Este es un programa simple en Ruby que realiza operaciones con números

# Definir variables
nombre = "Juan"  # Variable de tipo cadena
edad = 25        # Variable de tipo entero
altura = 1.75    # Variable de tipo flotante
es_adulto = true  # Variable booleana

# Imprimir el saludo con el nombre
puts "Hola, mi nombre es #{nombre}."

# Verificar si la persona es adulta
if es_adulto
  puts "Soy un adulto."
else
  puts "Soy menor de edad."
end

# Realizar operaciones aritméticas
numero1 = 10
numero2 = 5

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Mostrar los resultados de las operaciones
puts "La suma de #{numero1} y #{numero2} es: #{suma}"
puts "La resta de #{numero1} y #{numero2} es: #{resta}"
puts "La multiplicación de #{numero1} y #{numero2} es: #{multiplicacion}"
puts "La división de #{numero1} y #{numero2} es: #{division}"

# Usar una estructura de control de tipo case
puts "¿Tienes alguna mascota?"
mascota = "Perro"

case mascota
when "Perro"
  puts "Tienes un perro."
when "Gato"
  puts "Tienes un gato."
else
  puts "No sabemos qué mascota tienes."
end

# Fin del programa
