# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.
# Requisitos
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).
# 3. Por cada producto (usar for):
# o Pedir precio (entero, validar .isdigit()).
# o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
# o Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar:
# o Total sin descuentos
# o Total con descuentos
# o Ahorro total
# o Promedio por producto (usar float y formatear con :.2f, ejem: x = 3.14159
# print(f"{x:.2f}"))
# Validaciones obligatorias
# • Sin try/except.
# • No aceptar vacío en nombre (si queda vacío, es error).
# • Cantidad > 0 (si ingresa 0, volver a pedir).
# Salida esperada (ejemplo)
# Cliente: Ana
# Cantidad de productos: 3
# Producto 1 - Precio: 100 Descuento (S/N): s
# Producto 2 - Precio: 50 Descuento (S/N): n
# Producto 3 - Precio: 200 Descuento (S/N): s
# Total sin descuentos: $350
# Total con descuentos: $320.00
# Ahorro: $30.00
# Promedio por producto: $106.6
salida = ""
total_sin_descuento = 0
total_con_descuento = 0
porc_descuento = 0.1
print("\n\n ============= # Ejercicio 1— “Caja del Kiosco” =============== \n\n")
nombre_cliente=input("Ingrese nombre del cliente: ")
while nombre_cliente == "" or not nombre_cliente.isalpha():
    print("Error: Solo se permiten letras")
    nombre_cliente=input("Ingrese nombre del cliente: ")
nombre_cliente=nombre_cliente.capitalize()
cantidad = input("Ingrese la cantidad de productos a comprar: ")
while (cantidad =="" or not cantidad.isdigit()) or (int(cantidad)<=0):
    print("Error: Solo se permiten numeros y cantidad mayor a cero.")
    cantidad = input("Ingrese la cantidad de productos a comprar: ")
salida = "Cliente: " + nombre_cliente + "\n"
salida = salida + "Cantidad de productos: " + cantidad + "\n"
for x in range(int(cantidad)):
    precio = input("Ingrese el precio del producto: ")
    while (precio =="" or not precio.isdigit()) or (int(precio)<=0):
        print("Error: Solo se permiten numeros y precio mayor a cero.")
        precio = input("Ingrese el precio del producto: ")
    descuento=input("¿Posee descuento (S/N)?: ").upper()
    while descuento != "S" and descuento != "N":
        print("Debe ingresar S o N.")
        descuento=input("¿Posee descuento?: ").upper()
    if descuento == "S":
        total_con_descuento = total_con_descuento + float(precio)*porc_descuento
    total_sin_descuento = total_sin_descuento + float(precio)
    salida = salida + "Producto "+ str(x+1) + " - Precio: "+ str(precio) + "\t" + " Descuento (S/N): " + descuento + "\n"

salida = salida + "\n"
salida = salida + "Total sin descuento: $ " + str(round(total_sin_descuento,2)) + "\n"
salida = salida + "Total con descuento: $ " + str(round((total_sin_descuento - total_con_descuento),2)) + "\n"
salida = salida + "Ahorro: $" + str(total_sin_descuento)  + "\n"
salida = salida + "Promedio por producto: $ " + str(round(((total_sin_descuento - total_con_descuento)/(x+1)),2))  + "\n"
print(salida)


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Requisitos
# 1. Definir credenciales fijas en el código:
# o usuario correcto: "alumno"
# o clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
# 1. Ver estado de inscripción (mostrar “Inscripto”)
# 2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
# 3. Mostrar mensaje motivacional (1 frase)
# 4. Salir
# 5. Validación del menú:
# o Debe ser número (.isdigit())
# o Debe estar entre 1 y 4
# Cambio de clave
# • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, 
# rechazar.
# Salida esperada 
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.
# Intento 2/3 - Usuario: alumno
# Clave: python123
# Acceso concedido.
# 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.
# Opción: 2
# Nueva clave: 123
# Error: mínimo 6 caracteres.

print("\n\n ============= # Ejercicio 2 “Acceso al Campus y Menú Seguro” =============== \n\n")
cont = 1
bandera = True
usuario=input("Ingrese usuario: ")
clave=input("Ingrese clave: ")
while cont < 3 and bandera:
    if usuario != "alumno" or clave !="python123":
        print(f"Intento {cont}/3 - Usuario: alumno")
        print("Clave: xxx")
        print("Error: credenciales inválidas."+"\n")
        usuario=input("Ingrese usuario: ")
        clave=input("Ingrese clave: ")
    else:
        bandera = False
    cont +=1
if not bandera:
    print(f"\n Intento {cont-1}/3 - Usuario: alumno")
    print("Clave: python123")
    print("Acceso concedido.")
    bandera = True
    print("1. Ver estado de inscripción.")
    print("2. Cambia clave.")
    print("3. Frase motivacional.")
    print("4. Salir")
    opcion = input("Ingrese opcion: ")
    while bandera:
        while not opcion.isdigit() or not (int(opcion)>0 and int(opcion)<5):
            if not opcion.isdigit():
                print(f"Opcion: {opcion} \nError: ingreso un número inválido.")
            else:
                print(f"Opcion: {opcion} \nError: opción fuera de rango.")
            print("\n1. Ver estado de inscripción.")
            print("2. Cambia clave.")
            print("3. Frase motivacional.")
            print("4. Salir")
            opcion = input("Ingrese opcion: ")
        if opcion=="1":
            print("Estado de inscripción: Inscripto.")
            print("\n1. Ver estado de inscripción.")
            print("2. Cambia clave.")
            print("3. Frase motivacional.")
            print("4. Salir")
            opcion = input("Ingrese opcion: ")
        elif opcion == "2":
            print("Opcion 2")
            clave_nueva =input("Ingrese nueva clave: ")
            while len(clave_nueva)<6:
                print(f"Nueva clave: {clave_nueva} \nError: mínimo 6 caracteres.")
                clave_nueva =input("Ingrese nueva clave: ")
            clave_segunda_clave =input("Ingrese clave para confimar: ")
            while clave_segunda_clave != clave_nueva:
                print(f"Confirmacion clave: {clave_segunda_clave} \nError: no coincida con la clave para confirmar.")
                clave_segunda_clave =input("Ingrese clave para confimar: ")
            print("\nCambio de clave correcto.")
            print("\n1. Ver estado de inscripción.")
            print("2. Cambia clave.")
            print("3. Frase motivacional.")
            print("4. Salir")
            opcion = input("Ingrese opcion: ")
        elif opcion == "3":
            print("Frase motivacional.")
            print("\n1. Ver estado de inscripción.")
            print("2. Cambia clave.")
            print("3. Frase motivacional.")
            print("4. Salir")
            opcion = input("Ingrese opcion: ")
        else:
            print("Salir.")
            bandera = False
        

else:
    print("Cuenta bloqueada.")



print("\n\n ============= # Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas) =============== \n\n")
# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Contexto
# Hay 2 días de atención: Lunes y Martes.
# Cada día tiene cupos fijos:
# • Lunes: 4 turnos
# • Martes: 3 turnos
# Reglas
# 1. Pedir nombre del operador (solo letras).
# 2. Menú repetitivo hasta salir:
#       1. Reservar turno
#       2. Cancelar turno (por nombre)
#       3. Ver agenda del día
#       4. Ver resumen general
#       5. Cerrar sistema
# 3. Reservar:
#   o Elegir día (1=Lunes, 2=Martes).
#   o Pedir nombre del paciente (solo letras).
#   o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#   o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
# 4. Cancelar:
#   o Elegir día.
#   o Pedir nombre del paciente (solo letras).
#   o Si existe, cancelar y dejar el espacio vacío ("").
# 5. Ver agenda del díao Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
# 6. Resumen general:
# o Turnos ocupados y disponibles por día.
# o Día con más turnos (o empate).
# Restricciones
# • ❌ No listas, no diccionarios, no sets, no tuplas.
# • ✅ Se permite usar "" como “vacío”.
# • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except)

a1 = b1 = c1 = d1 = a2 = b2 = c2 = ""

bandera = True
salida = ""
nombre_operador=input("Ingrese nombre operador: ")
while nombre_operador == "" or not nombre_operador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_operador=input("Ingrese nombre operador: ")
nombre_operador=nombre_operador.capitalize()
while bandera:
    opcion = input(f"\nMenú de opciones.\n1. Reservar turno.\n2. Cancelar turno (por nombre).\n3. Ver agenda del día.\n4. Ver resumen general.\n5. Cerrar Sistema.\n\nIngrese opción: ")
    while not opcion.isdigit() or not (int(opcion)>0 and int(opcion)<6):
        print(f"Opcion: {opcion} \nError: ingreso opción inválida.")
        opcion = input(f"\nMenú de opciones.\n1. Reservar turno.\n2. Cancelar turno (por nombre).\n3. Ver agenda del día.\n4. Ver resumen general.\n5. Cerrar Sistema.\n\nIngrese opción: ")
    if opcion == "1":
        print("Reservar Turno.\n")
        nombre_paciente=input("Ingrese nombre paciente: ")
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print("Error: Solo se permiten letras.")
            nombre_paciente=input("Ingrese nombre paciente: ")
        nombre_paciente=nombre_paciente.capitalize()
        dia = input("Ingrese 1= Lunes, 2=Martes: ")
        while not dia.isdigit() or not (int(dia)>0 and int(dia)<3):
            print(f"Opcion: {dia} \nError: ingreso opción inválida.")
            dia = input("Ingrese 1= Lunes, 2=Martes: ")
        if dia == "1":
            if a1 == "":
                a1 = nombre_paciente
                print("\nTurno registrado.\n")
            elif b1 == "":
                if a1 != nombre_paciente:
                    b1 = nombre_paciente
                    print("\nTurno registrado.\n")
                else:
                    print("Ya tiene turno asignado ese día.")
            elif c1 == "":
                if a1!=nombre_paciente and b1!=nombre_paciente:
                    c1 = nombre_paciente
                    print("\nTurno registrado.\n")
                else:
                    print("Ya tiene turno asignado ese día.")
            elif d1 == "":
                if a1!=nombre_paciente and b1!=nombre_paciente and nombre_paciente!=c1:
                    d1 = nombre_paciente
                    print("\nTurno registrado.\n")
                else:
                    print("\nYa tiene turno asignado ese día.")
            else:
                print("\nNo hay turnos disponibles para ese día.")
        else:
            if a2 == "":
                a2 = nombre_paciente
                print("\nTurno registrado.\n")
            elif b2 == "":
                if a2 != nombre_paciente:
                    b2 = nombre_paciente
                    print("\nTurno registrado.\n")
                else:
                    print("Ya tiene turno asignado ese día.")
            elif c2 == "":
                if a2!=nombre_paciente and b2!=nombre_paciente:
                    c2 = nombre_paciente
                    print("\nTurno registrado.\n")
                else:
                    print("\nYa tiene turno asignado ese día.")
            else:
                print("\nNo hay turnos disponibles para ese día.")
    elif opcion == "2":
        print("\nCancelar Turno.\n")
        nombre_paciente=input("Ingrese nombre paciente: ")
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print("Error: Solo se permiten letras.")
            nombre_paciente=input("Ingrese nombre paciente: ")
        nombre_paciente=nombre_paciente.capitalize()
        dia = input("Ingrese 1= Lunes, 2=Martes: ")
        while not dia.isdigit() or not (int(dia)>0 and int(dia)<3):
            print(f"Opcion: {dia} \nError: ingreso opción inválida.")
            dia = input("Ingrese 1= Lunes, 2=Martes: ")
        if dia =="1":
            if a1==nombre_paciente:
                a1=""
                print("Turno cancelado con exito.\n")
            elif b1==nombre_paciente:
                b1 = ""
                print("Turno cancelado con exito.\n")
            elif c1==nombre_paciente:
                c1 ="" 
                print("Turno cancelado con exito.\n")
            elif d1==nombre_paciente:
                d1==""
                print("Turno cancelado con exito.\n")
            else:
                print("\nNo tiene turno asignado es día.\n")
        else:
            if a2 ==nombre_paciente:
                a2 = ""
                print("Turno cancelado con exito.\n")
            elif b2 ==nombre_paciente:
                b2 = ""
                print("Turno cancelado con exito.\n")
            elif c2==nombre_paciente:
                c2==""
                print("Turno cancelado con exito.\n")
            else:
                print("\nNo tiene turno asignado es día.\n")


    elif opcion == "3":
        print("Agenda del día.\n")
        print("Lunes: \n")
        if a1=="":
            salida = "Primer turno: Libre.\n"
        else:
            salida = "Primer turno: " + a1 + "\n"
        if b1=="":
            salida = salida + "Segundo turno: Libre.\n"
        else:
            salida = salida + "Segundo turno: " + b1 + "\n"
        if c1=="":
            salida = salida + "Tercer turno: Libre.\n"
        else:
            salida = salida + "Tercer turno: " + c1 + "\n"
        if d1=="":
            salida = salida + "Cuarto turno: Libre.\n"
        else:
            salida = salida + "Cuarto turno: " + d1 + "\n"
        salida = salida + "\n" + "Martes:" +"\n"
        if a2=="":
            salida = salida + "Primer turno: Libre.\n"
        else:
            salida = salida + "Primer turno: " + a2 + "\n"
        if b2=="":
            salida = salida + "Segundo turno: Libre.\n"
        else:
            salida = salida + "Segundo turno: " + b2 + "\n"
        if c2=="":
            salida = salida + "Tercer turno: Libre.\n"
        else:
            salida = salida + "Tercer turno: " + c2 + "\n"
        print(salida)
    elif opcion == "4":
        tl1 = tl2 = to1 = to2 = 0
        if a1=="":
            tl1 +=1
        else:
            to1 +=1
        if b1=="" :
            tl1 +=1
        else:
            to1 +=1
        if c1=="" :
            tl1 +=1
        else:
            to1 +=1 
        if d1=="" :
            tl1 +=1
        else:
            to1 +=1 
        if a2=="" :
            tl2 +=1
        else:
            to2 +=1 
        if b2=="" :
            tl2 +=1
        else:
            to2 +=1 
        if c2=="" :
            tl2 +=1
        else:
            to2 +=1
        print(f"Día lunes. \nTurnos ocupados: {to1} - Turnos libres: {tl1}")
        print(f"Día martes. \nTurnos ocupados: {to2} - Turnos libres: {tl2}")
        if to1>to2:
            print("Día lunes con mayor cantidad de turnos.")
        elif to1 == to2:
            print("Día lunes y martes igual cantidad de turnos.")
        else:
            print("Día martes con mayor cantidad de turnos.")

        pass
    else:
        bandera = False

print("\n\n ============= # Ejercicio 4 — “Escape Room: La Bóveda” =============== \n\n")

# Ejercicio 4 — “Escape Room: La Bóveda”
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados.
# Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.
# Variables iniciales (NO se piden por teclado)
# • energia = 100
# • tiempo = 12
# • cerraduras_abiertas = 0
# • alarma = False
# • codigo_parcial = ""
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cont_regla = 0
nombre_agente=input("Ingrese nombre del agente: ")
while nombre_agente == "" or not nombre_agente.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_agente=input("Ingrese nombre del agente: ")
nombre_agente=nombre_agente.capitalize()
bandera =True
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    opcion= input(f"Menu.\n1. Forzar Cerradura.\n2. Hackear Panel.\n3. Descansar.\n")
    while not opcion.isdigit() or not (int(opcion)>0 and int(opcion)<6):
        print(f"Opcion: {opcion} \nError: ingreso opción inválida.")
        opcion= input(f"Menu.\n1. Forzar Cerradura.\n2. Hackear Panel.\n3. Descansar.\n")
    if opcion == "1":
        energia -= 20
        tiempo -=2
        cont_regla +=1
        if energia < 40:
            riesgo_alarma = input("Riego de alarma.\nIngres 1-2-3: ")
            while not riesgo_alarma.isdigit() or not (int(riesgo_alarma)>0 and int(riesgo_alarma)<4):
                print(f"Opcion: {opcion} \nError: ingreso opción inválida.")
                riesgo_alarma = input("Riego de alarma.\nIngres 1-2-3: ")
            if riesgo_alarma =="3":
                alarma = True
        else:
            if cont_regla == 3:
                print("Se activo la regla anti-spam.\nNo abre cerradura.")
                alarma = True
            else:
                print("Abrió una cerrudara.")
                cerraduras_abiertas +=1
    elif opcion =="2":
        energia -=20
        tiempo -=2
        for x in range(1,5):
            cont_regla=0
            letra=input("Ingrese una letra: ")
            while (letra == "" or not letra.isalpha()) and len(letra)==1:
                print("Error: Solo se permite una letra.")
                letra=input("Ingrese una letra: ")
            codigo_parcial = codigo_parcial + letra
            if len(codigo_parcial)>=8 and cerraduras_abiertas<=3:
                print("Se ha abierto una cerradura-")
                cerraduras_abiertas +=1
    else:
        print("Descanzar")
        energia +=15
        if energia>100:
            energia=100
        tiempo-=1
        if alarma:
            energia-=10
if cerraduras_abiertas == 3:
    print("VICTORIA!")
elif energia<=0 or tiempo <=0:
    print("DERROTA!")
elif alarma:
    print("DERROTA (BLOQUEO)")
else:
    print("Error de juego.")
    print(f"Cerraduras {cerraduras_abiertas}, Energia {energia}, Tiempo {tiempo}, Alarma {alarma}")
    

print("\n\n ============= # Ejercicio 5 — Escape Room: La Arena del # Gladiador  =============== \n\n")


# Ejercicio 5 — “Escape Room:"La Arena del Gladiador" 
# 1. Descripción del Escenario 
# Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un 
# usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El 
# objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo. 
# Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
# control (if/elif/else), ciclos (while y for) y validación de datos estricta. 
# 2. Requerimientos Técnicos 
# A. Tipos de Datos 
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego: 
# • • String: Para el nombre del jugador. 
# • • Int: Para los Puntos de Vida (HP) y cantidad de pociones. 
#       • • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). 



print("--- BIENVENIDO A LA ARENA ---")
gladiador = input("Nombre del gladiador: ").strip()
while gladiador == "" or not gladiador.isalpha():
    print("Error. Solo se permiten letras")
    gladiador = input("Nombre del gladiador: ").strip()
gladiador=gladiador.capitalize() 
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_base_gladiador = 15
danio_base_enemigo = 12
turno_gladiador = True
print(f"=== INICIO DEL COMATE ===") 
while vida_gladiador> 0 and vida_enemigo>0:
    if turno_gladiador:
        print(f"{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}  |  Pociones: {pociones_vida}")
        while True:
            opcion = input("Elige acción: \n1. Ataque Pesado\n2. Ráfaga Veloz.\n3. Curar\nOpción: ").strip()
            while not opcion.isdigit():
                print(f"Opción: {opcion}\nError: ingrese un número válido.")
                opcion = input("Elige acción: \n1. Ataque Pesado\n2. Ráfaga Veloz.\n3. Curar\nOpción: ").strip()
            opcion = int(opcion)
            if opcion==1:
                if vida_enemigo<20:
                    puntos = danio_base_gladiador*1.5
                else:
                    puntos = danio_base_gladiador
                vida_enemigo-=puntos
                print(f"Atacaste al enemigo por {puntos} puntos de daño base.")
                turno_gladiador = False
                break
            elif opcion==2:
                for x in range(3):
                    vida_enemigo-=5
                    print("Golpe conectado por cinco daños.")
                turno_gladiador = False
                break
            elif opcion == 3:
                if pociones_vida >0:
                    vida_gladiador+=30
                    pociones_vida-=1
                else:
                    print("No tienes pociones de vida.")
                    print("Perdiste el turno,")
                turno_gladiador = False
                break
            else:
                print("Opcion erronea.")
    else:
        vida_gladiador-=danio_base_enemigo
        print(f"El enemigo te atacó por {danio_base_gladiador} puntos.")
        turno_gladiador = True
        print("\n=== NUEVO TURNO ===")
if vida_gladiador > 0:
    print(f"VICTORIA! {gladiador} has ganado la batalla.")
else:
    print(f"DERROTA! {gladiador} has perdido la batalla.")