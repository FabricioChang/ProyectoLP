# Algoritmo de prueba - Fabricio Alberto Chang Encalada
# Comentario de prueba: Declaración de variables
edad = 25            # Variable de tipo entero
nombre = "Carlos"    # Variable de tipo cadena
precio = 10.5        # Variable de tipo flotante
is_active = true     # Variable booleana

# Error semántico: Asignación incorrecta de tipo
# Edad debería ser un entero, pero se le asigna una cadena
edad = "treinta"     # Error: Se esperaba un entero

# Operadores y expresiones
total = precio * 2    # Operación válida: multiplicación de flotante
descuento = 5 + "10"  # Error semántico: intento de sumar flotante y cadena

# Estructuras de control
if edad == "treinta"  # Error semántico: edad debería ser un número entero
  puts "Edad válida"
else
  puts "Edad no válida"
end

# Bucle for
for i in 1..3
  puts "Iteración #{i}"
end

# Error semántico: break fuera de un bucle
break  # Error: no está dentro de un bucle

# Funciones
def saludar(nombre)
  # Función correcta: retorna un saludo
  return "Hola, #{nombre}"
end

puts saludar("Carlos")

def calcular_area(base, altura)
  # Función incorrecta: retorna un string en lugar de un número
  return "El área es #{base * altura}"
end

puts calcular_area(5, 10)  # Error semántico: se espera un valor numérico

# Comprobación de variables globales
$contador = 0
$contador += 1
puts $contador

# Uso de variables no declaradas (error léxico y sintáctico)
puts non_existent_variable   # Error sintáctico: variable no definida
