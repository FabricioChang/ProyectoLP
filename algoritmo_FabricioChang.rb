# Declaración de variables
nombre = "Fabricio"
$contador = 10
@lista = [1, 2, 3, 4, 5]

# Estructura de datos Hash
mi_hash = { "clave1" => 10, "clave2" => 20 }

# Solicitud de datos
puts "Escribe un número:"
numero = gets()

# Función con parámetros por defecto
def saludar(nombre = "Invitado")
    puts "Hola, #{nombre}"
end

# Condicionales y operadores lógicos
if numero.to_i > 5 && @lista.include?(numero.to_i)
    puts "El número está en la lista y es mayor a 5"
else
    puts "El número no cumple las condiciones"
end

# Ciclo until
until $contador == 0
    puts "Contador: #{$contador}"
    $contador -= 1
end

# Función llamada con y sin parámetros
saludar()
saludar(nombre)

# Uso de interpolación en cadenas
puts "El valor de mi_hash['clave1'] es #{mi_hash['clave1']}"

# Operación aritmética e incremento
suma = 0
@lista.each do |num|
    suma += num
end
puts "La suma de la lista es #{suma}"

