import funciones as fn
import time

fn.habitacion()

print("Bienvenido a la Guarderia Mascota Segura")
time.sleep(3)
while True:
    opc = fn.mostrar_menu()
    if opc == 1:
        fn.grabar_mascota()
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    else:
        print("Gracias por visitarnos y esperamos que tenga buen dia")
        break