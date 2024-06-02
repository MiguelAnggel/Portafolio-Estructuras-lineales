from nodo import Nodo
from listaSimple import ListaSimple
from listaDoble import ListaDoble
from listaDobleCircular import ListaDobleCircular
from pila import Pila
from cola import Cola 
from pilaEstatica import PilaEstatica
from colaCircular import ColaCircular
from colaDoble import ColaDoble
from colaER import ColaER
from colaSR import ColaSR
from colaPA import ColaPA
from colaPD import ColaPD
from listaCircular import ListaCircular
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape

# Crear un objeto console para usar con Rich
console = Console()

def mostrar_menu_principal():
    menu_text = "1.- Listas\n2.- Pilas\n3.- Colas\n0.- Salir"

    console.print(Panel(menu_text, title="[bold magenta]Portafolio de Estructura de Datos[/]", border_style="green"))

def mostrar_submenu_listas():
    options = Text("1.- Lista Simple\n2.- Lista Doble\n3.- Lista Doble Circular\n4.- Lista Simple Circular\n5.- Regresar al menú principal", style="bold yellow")
    console.print(Panel(options, title="[bold cyan]Listas[/]", border_style="bright_blue"))

def mostrar_submenu_pilas():
    options = Text("1.- Pila Dinámica.\n2.- Pila Estática.\n3.- Regresar al menú principal", style="bold yellow")
    console.print(Panel(options, title="[bold cyan]Pilas[/]", border_style="bright_blue"))

def mostrar_submenu_colas():
    options = Text("1.- Cola Simple\n2.- Cola Doble\n3.- Cola Circular\n4.- Cola Entrada Restringida\n5.- Cola Salida Restringida\n6.- Cola Prioridad Ascendete\n7.- Cola Prioridad Descendente\n8.- Regresar al menú principal", style="bold yellow")
    console.print(Panel(options, title="[bold cyan]Colas[/]", border_style="bright_blue"))

def submenu_lista_simple():
    lista = ListaSimple()  # Crear una nueva lista simple
    while True:
        options_text = "1. Agregar elemento\n2. Eliminar elemento\n3. Mostrar lista\n4. Buscar elemento\n5. Eliminar el último elemento\n6. Regresar\n0. Definición"
        console.print(Panel(options_text, title="[bold red]Menu Lista Simple[/]", border_style="red"))
        opcion_ls = console.input("Seleccione una opción: ")

        if opcion_ls == "1":
            elemento = console.input("Ingrese el valor a agregar: ")
            lista.agregar(elemento)
            console.print("Elemento agregado.", style="green")
        elif opcion_ls == "2":
            elemento = console.input("Ingrese el valor a eliminar: ")
            eliminado = lista.eliminar(elemento)
            if eliminado:
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("Elemento no encontrado.", style="yellow")
        elif opcion_ls == "3":
            console.print("Elementos de la lista:")
            lista.recorrer()
        elif opcion_ls == "4":
            elemento = console.input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                console.print("Elemento encontrado.", style="green")
            else:
                console.print("Elemento no encontrado.", style="yellow")
        elif opcion_ls == "5":
            eliminado = lista.eliminar_final()
            if eliminado:
                console.print("Último elemento eliminado.", style="red")
            else:
                console.print("Lista ya está vacía.", style="yellow")
        elif opcion_ls == "0":
            console.print(Panel("[bold]La Lista Simple es una estructura de datos que organiza elementos de manera secuencial, donde cada elemento está conectado únicamente al siguiente. Es fácil de implementar y usar para colecciones de datos lineales.[/]", title="Definición", border_style="green"))
        elif opcion_ls == "6":
            break
        else:
            console.print("Opción no válida.", style="bold red")

def sub_menu_lista_doble():
    lista = ListaDoble()  
    while True:
        options_text = Text(
            "1. Agregar elemento al final\n""2. Agregar elemento al inicio\n""3. Eliminar elemento del final\n""4. Eliminar elemento del inicio\n""5. Eliminar elemento\n""6. Mostrar lista desde el inicio\n""7. Mostrar lista desde el final\n""8. Buscar elemento\n""9. Regresar\n""0. Definición", style="bold yellow")
        console.print(Panel(options_text, title="[bold red]Menú Lista Doble[/]", border_style="red"))

        opcion_ld = console.input("Seleccione una opción: ")

        if opcion_ld == "1":
            elemento = console.input("Ingrese el valor a agregar: ")
            lista.agregar_final(elemento)
            console.print("Elemento agregado.", style="green")

        elif opcion_ld == "2":
            elemento = console.input("Ingrese el valor a agregar: ")
            lista.agregar_inicio(elemento)
            console.print("Elemento agregado.", style="green")

        elif opcion_ld == "3":
            eliminado = lista.eliminar_final()
            if eliminado:
                console.print("Último elemento eliminado.", style="red")
            else:
                console.print("Lista ya está vacía.", style="yellow")

        elif opcion_ld == "4":
            eliminado = lista.eliminar_inicio()
            if eliminado:
                console.print("Primer elemento eliminado", style="red")
            else:
                console.print("La lista ya está vacía.", style="yellow")

        elif opcion_ld == "5":
            elemento = input("Ingrese el valor a eliminar: ")
            eliminado = lista.eliminar(elemento)
            if eliminado:
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("Elemento no encontrado.", style="yellow")

        elif opcion_ld == "6":
            console.print("Elementos de la lista desde el inicio:")
            lista.recorrer_inicio()

        elif opcion_ld == "7":
            console.print("Elementos de la lista desde el final:")
            lista.recorrer_fin()

        elif opcion_ld == "8":
            elemento = console.input("Ingrese el valor a buscar: ")
            encontrado = lista.buscar(elemento)
            if encontrado:
                console.print("Elemento encontrado.", style="green")
            else:
                console.print("Elemento no encontrado.", style="yellow")

        elif opcion_ld == "0":
            definition_text = Text('''La Lista Doble es similar a la lista simple pero cada nodo tiene dos enlaces: uno hacia el \npróximo nodo y otro hacia el anterior. Esto facilita recorrer la lista en ambas direcciones, \nmejorando la flexibilidad para operaciones de inserción y eliminación.''', style="italic")
            console.print(Panel(definition_text, title="[bold magenta]Definición[/]", border_style="green"))
            
        elif opcion_ld == "9":
            break

        else:
            console.print("Opción no válida.", style="bold red")

def submenu_listaDobleCircular():
    lista = ListaDobleCircular()  
    while True:
        options_text = Text(
            "1. Agregar elemento al final\n"
            "2. Agregar elemento al inicio\n"
            "3. Eliminar elemento del final\n"
            "4. Eliminar elemento del inicio\n"
            "5. Eliminar elemento\n"
            "6. Mostrar lista desde el inicio\n"
            "7. Mostrar lista desde el final\n"
            "8. Buscar elemento\n"
            "9. Regresar\n"
            "0. Definición", style="bold yellow")
        console.print(Panel(options_text, title="[bold red]Menú Lista Doble Circular[/]", border_style="red"))

        opcion_ldc = input("Seleccione una opción: ")

        if opcion_ldc == "1":
            elemento = console.input("Ingrese el valor a agregar: ")
            lista.agregar_final(elemento)
            console.print("Elemento agregado.", style="green")
            
        elif opcion_ldc == "2":
            elemento = input("Ingrese el valor a agregar: ")
            lista.agregar_inicio(elemento)
            console.print("Elemento agregado.", style="green")
            
        elif opcion_ldc == "3":
            if lista.eliminar_final():
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("Lista ya está vacía.", style="yellow")
                
        elif opcion_ldc == "4":
            if lista.eliminar_inicio():
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("La lista ya está vacía.", style="yellow")
                
        elif opcion_ldc == "5":
            elemento = input("Ingrese el valor a eliminar: ")
            if lista.eliminar(elemento):
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("Elemento no encontrado.", style="yellow")
                
        elif opcion_ldc == "6":
            lista.recorrer_inicio()
            
        elif opcion_ldc == "7":
            lista.recorrer_fin()
            
        elif opcion_ldc == "8":
            elemento = input("Ingrese el valor a buscar: ")
            if lista.buscar(elemento):
                console.print("Elemento encontrado.", style="green")
            else:
                console.print("Elemento no encontrado.", style="yellow")
        elif opcion_ldc == "0":
            
            console.print(Text('''La Lista Doble Circular es una variante de las listas dobles en la que el último elemento está 
            conectado al primero, formando un círculo. Esto permite un recorrido continuo de la lista y mejora 
            la eficiencia de ciertas operaciones.''', style="italic"), justify="center")
            
        elif opcion_ldc == "9":
            break
        else:
            console.print("Opción no válida", style="bold red")
            
            
            
def submenu_listaSimpleCircular():
    lista=ListaCircular()
    while True:
        # Usando Rich para imprimir el menú con un panel estilizado
        console.print(Panel(
            "1. Agregar elemento al final\n"
            "2. Agregar elemento al inicio\n"
            "3. Eliminar elemento del final\n"
            "4. Eliminar elemento del inicio\n"
            "5. Eliminar elemento\n"
            "6. Mostrar lista desde el inicio\n"
            "7. Mostrar lista desde el final\n"
            "8. Buscar elemento\n"
            "9. Regresar\n"
            "0. Definición", title="[bold red]Menú Lista Simple Circular[/]", border_style="red"))

        opcion_lsc = console.input("[bold orange]Seleccione una opción: [/]")

        if opcion_lsc == "1":
            elemento = console.input("[bold orange]Ingrese el valor a agregar: [/]")
            lista.agregar_final(elemento)
            console.print("Elemento agregado.", style="green")

        elif opcion_lsc == "2":
            elemento = console.input("[bold orange]Ingrese el valor a agregar: [/]")
            lista.agregar_inicio(elemento)
            console.print("Elemento agregado.", style="green")

        elif opcion_lsc == "3":
            if lista.eliminar_final():
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("Lista ya está vacía.", style="yellow")

        elif opcion_lsc == "4":
            if lista.eliminar_inicio():
                console.print("Elemento eliminado.", style="red")
            else:
                console.print("La lista ya está vacía.", style="yellow")

        elif opcion_lsc == "5":
            elemento = console.input("[bold orange]Ingrese la posición del valor a eliminar: [/]")
            if elemento.isdigit():
                posicion = int(elemento)
                if lista.eliminar(posicion):
                    console.print("Elemento eliminado.", style="red")
                else:
                    console.print("Elemento no encontrado.", style="yellow")
            else:
                console.print("[bold yellow]Por favor, ingrese un número válido para la posición.[/]")

        elif opcion_lsc == "6":
            console.print("Elementos de la lista desde el inicio:")
            lista.recorrer_adelante()

        elif opcion_lsc == "7":
            console.print("Elementos de la lista desde el final:")
            lista.recorrer_atras()

        elif opcion_lsc == "8":
            elemento = console.input("[bold orange]Ingrese el valor a buscar: [/]")
            if lista.buscar(elemento):
                console.print("Elemento encontrado.", style="green")
            else:
                console.print("Elemento no encontrado.", style="yellow")

        elif opcion_lsc == "0":
            console.print(Text('''La Lista Simple Circular es una lista en la que el último nodo está conectado al primero, 
            creando un bucle circular. Esto es útil para aplicaciones que necesitan un reciclaje continuo de 
            los datos.''', style="italic"), justify="center")

        elif opcion_lsc == "9":
            break

        else:
            console.print("Opción no válida", style="bold red")
    
def submenu_pila():
    pilaD = Pila()  
    while True:
        console.print(Panel(
            "1. Apilar\n"
            "2. Desapilar\n"
            "3. Consultar\n"
            "4. Obtener el tamaño de la pila\n"
            "5. Verificar si la pila está vacía\n"
            "6. Regresar\n"
            "0. Definición", title="[bold red]Submenú Pila Dinámica[/]", border_style="red"))

        opcion_pd = console.input("[bold orange]Ingrese una opción: [/]")

        if opcion_pd == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a apilar: [/]")
            pilaD.apilar(elemento)
            console.print("Elemento agregado a la Pila.", style="green")
        elif opcion_pd == "2":
            if not pilaD.esta_vacia():
                pilaD.desapilar()
                console.print("Elemento eliminado de la Pila.", style="red")
            else:
                console.print("La pila actual ya está vacía.", style="yellow")
        elif opcion_pd == "3":
            elemento = pilaD.consultar()
            if elemento is not None:
                console.print(f"El elemento en la cima es: {elemento}", style="bold magenta")
            else:
                console.print("La pila está vacía.", style="yellow")
        elif opcion_pd == "4":
            console.print(f"El tamaño de la Pila actual es: {pilaD.size()}", style="bold magenta")
        elif opcion_pd == "5":
            if pilaD.esta_vacia():
                console.print("La pila está vacía.", style="yellow")
            else:
                console.print("La pila no está vacía", style="green")
        elif opcion_pd == "0":
            console.print(Text('''La Pila es una estructura de datos del tipo LIFO (Last In, First Out), donde el último elemento 
            añadido es el primero en ser retirado. Es ampliamente usada en situaciones que requieren una 
            gestión inversa temporal de los datos.''', style="italic"), justify="center")
        elif opcion_pd == "6":
            break
        else:
            console.print("Opción no válida", style="bold red")  
                
def submenu_pilaE():
    
    pilae = PilaEstatica()  

    while True:
        console.print(Panel(
            "1. Apilar\n"
            "2. Desapilar\n"
            "3. Consultar\n"
            "4. Obtener el tamaño de la pila\n"
            "5. Verificar si la pila está vacía\n"
            "6. Regresar\n"
            "0. Definición", title="[bold red]Menú Pila Estática con 5 espacios[/]", border_style="red"))

        opcion_pe = console.input("[bold orange]Ingrese una opción: [/]")

        if opcion_pe == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a apilar: [/]")
            pilae.apilar(elemento)
            console.print("Elemento agregado a la Pila.", style="green")
        elif opcion_pe == "2":
            if not pilae.esta_vacia():
                pilae.desapilar()
                console.print("Elemento eliminado de la Pila.", style="red")
            else:
                console.print("La pila actual ya está vacía.", style="yellow")
        elif opcion_pe == "3":
            elemento = pilae.consultar()
            if elemento is not None:
                console.print(f"El elemento en la cima es: {elemento}", style="bold magenta")
            else:
                console.print("La pila está vacía.", style="yellow")
        elif opcion_pe == "4":
            console.print(f"La capacidad de la pila es de 5 Elementos.\nY contiene {pilae.tamanio()} Elemento/s.", style="bold magenta")
        elif opcion_pe == "5":
            if pilae.esta_vacia():
                console.print("La pila está vacía.", style="yellow")
            else:
                console.print("La pila no está vacía", style="green")
        elif opcion_pe == "0":
            console.print(Text('''La Pila Estática es una pila con un tamaño fijo. Una vez que se llena, no se pueden añadir más 
            elementos a menos que se libere espacio. Esto puede limitar su uso pero garantiza un control sobre 
            el consumo de memoria.''', style="italic"), justify="center")
        elif opcion_pe == "6":
            break
        else:
            console.print("Opción no válida", style="bold red")


def submenu_cola():
    cola_s = Cola()
    while True:
        console.print(Panel(
            "1. Encolar\n"
            "2. Desencolar\n"
            "3. Consultar\n"
            "4. Verificar si la cola está vacía\n"
            "5. Tamaño de la cola\n"
            "6. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola[/]", border_style="red"))

        opcion_cola = console.input("[bold orange]Ingrese una opción: [/]")

        if opcion_cola == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            cola_s.encolar(elemento)
            console.print("Elemento agregado a la cola", style="green")
        elif opcion_cola == "2":
            if not cola_s.esta_vacia():
                cola_s.desencolar()
                console.print("Elemento desencolado.", style="red")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_cola == "3":
            if cola_s.esta_vacia():
                console.print("La cola está vacía", style="yellow")
            else:
                console.print(f"El próximo valor de la cola en salir es: {cola_s.consultar()}", style="bold magenta")
        elif opcion_cola == "4":
            if not cola_s.esta_vacia():
                console.print("La cola no está vacía.", style="green")
            else:
                console.print("La cola está vacía", style="yellow")
        elif opcion_cola == "5":
            console.print(f"El tamaño de la cola es: {cola_s.size()} Elemento/s", style="bold magenta")
        elif opcion_cola == "0":
            console.print(Text('''La Cola es una estructura de datos del tipo FIFO (First In, First Out), donde el primer elemento 
            en ser añadido es el primero en ser retirado. Es ideal para procesos de planificación y gestión de 
            tareas en secuencia.''', style="italic"), justify="center")
        elif opcion_cola == "6":
            break
        else:
            console.print("Opción no válida", style="bold red") 
            
def submenu_colaDoble():
    colaD = ColaDoble() 
    while True:
        console.print(Panel(
            "1. Encolar al inicio\n"
            "2. Encolar al final\n"
            "3. Desencolar del inicio\n"
            "4. Desencolar del final\n"
            "5. Verificar si la cola está vacía\n"
            "6. Recorrer desde el inicio\n"
            "7. Recorrer desde el final\n"
            "8. Tamaño de la Cola\n"
            "9. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola Doble[/]", border_style="red"))

        opcion_cd = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_cd == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            colaD.encolar_inicio(elemento)
            console.print("Elemento encolado al inicio.", style="green")
        elif opcion_cd == "2":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            colaD.encolar_final(elemento)
            console.print("Elemento encolado al final.", style="green")
        elif opcion_cd == "3":
            if not colaD.esta_vacia():
                colaD.desencolar_inicio()
                console.print("Elemento desencolado.", style="red")
            else:
                console.print("La cola está vacía", style="yellow")
        elif opcion_cd == "4":
            if not colaD.esta_vacia():
                colaD.desencolar_final()
                console.print("Elemento desencolado", style="red")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_cd == "5":
            if colaD.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_cd == "6":
            console.print("Recorriendo desde el inicio:")
            colaD.recorrer_inicio()
        elif opcion_cd == "7":
            console.print("Recorriendo desde el final:")
            colaD.recorrer_fin()
        elif opcion_cd == "8":
            console.print(f"El tamaño de la cola es de: {colaD.size()} Elementos.", style="bold magenta")
        elif opcion_cd == "0":
            console.print(Text('''La Cola Doble permite inserciones y eliminaciones en ambos extremos. Combina las características 
            de una pila y una cola, haciéndola muy versátil para ciertos tipos de procesamientos de datos.''', style="italic"), justify="center")
        elif opcion_cd == "9":
            break
        else:
            console.print("Opción no válida", style="bold red")

def submenu_colaCircular():
    colaC = ColaCircular() 

    while True:
        console.print(Panel(
            "1. Encolar un elemento al inicio.\n"
            "2. Desencolar el primer elemento ingresado.\n"
            "3. Consultar el próximo elemento a salir.\n"
            "4. Verificar si la cola está vacía.\n"
            "5. Recorrer desde el inicio.\n"
            "6. Recorrer desde el final.\n"
            "7. Elementos de la cola.\n"
            "8. Regresar\n"
            "0. Definición", title="[bold red]Submenú de Cola Circular[/]", border_style="red"))

        opcion_colaC = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_colaC == "1":
            elemento = console.input("[bold orange]Ingresa el elemento a encolar: [/]")
            colaC.encolar(elemento)
            console.print("Elemento encolado.", style="green")
        elif opcion_colaC == "2":
            if not colaC.esta_vacia():
                colaC.desencolar()
                console.print("Elemento desencolado.", style="red")
            else:
                console.print("La cola está vacía", style="yellow")
        elif opcion_colaC == "3":
            if not colaC.esta_vacia():
                console.print(f"Próximo valor a desencolar: {colaC.consultar()}", style="bold magenta")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colaC == "4":
            if colaC.esta_vacia():
                console.print("La cola está vacía", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_colaC == "5":
            console.print("Recorriendo desde el inicio:")
            colaC.recorrer_inicio()
        elif opcion_colaC == "6":
            console.print("Recorriendo desde el final:")
            colaC.recorrer_final()
        elif opcion_colaC == "7":
            console.print(f"La cola contiene {colaC.size()} Elemento/s", style="bold magenta")
        elif opcion_colaC == "0":
            console.print(Text('''La Cola Circular es una variante de la cola donde los extremos están conectados formando un 
            círculo. Esto optimiza el uso del espacio permitiendo reutilizar las posiciones liberadas de manera 
            continua y eficiente.''', style="italic"), justify="center")
        elif opcion_colaC == "8":
            break
        else:
            console.print("Opción no válida", style="bold red")

        
def submenu_colaRestringida():
    colaR = ColaER()  # Suponemos que tienes definida esta clase ColaER en algún lugar del código

    while True:
        # Usamos Rich para imprimir el menú con un panel estilizado
        console.print(Panel(
            "1. Encolar al inicio\n"
            "2. Desencolar del final\n"
            "3. Consultar el frente\n"
            "4. Consultar el final\n"
            "5. Verificar si la cola está vacía\n"
            "6. Recorrer\n"
            "7. Tamaño de la Cola\n"
            "8. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola de Entrada Restringida[/]", border_style="red"))

        opcion_colaR = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_colaR =="1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            colaR.encolar_inicio(elemento)
            console.print("Elemento agregado.", style="green")
        elif opcion_colaR == "2":
            if colaR.desencolar_final():
                console.print("Elemento eliminado de la cola.", style="red")
            else:
                console.print("No hay elementos para desencolar.", style="yellow")
        elif opcion_colaR == "3":
            primer_elemento = colaR.consultar()
            if primer_elemento:
                console.print(f"Primer elemento de la cola: {primer_elemento}", style="bold magenta")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colaR == "4":
            ultimo_elemento = colaR.consultar_final()
            if ultimo_elemento:
                console.print(f"Último elemento de la cola: {ultimo_elemento}", style="bold magenta")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colaR == "5":
            if colaR.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_colaR =="6":
            console.print("Recorriendo desde el inicio:")
            colaR.recorrer_inicio()
        elif opcion_colaR == "7":
            console.print(f"La cola contiene {colaR.size()} Elemento/s.", style="bold magenta")
        elif opcion_colaR == "0":
            console.print(Text('''La Cola de Entrada Restringida solo permite añadir elementos por un extremo. Esto puede ser útil 
            para controlar cómo se añaden los datos y gestionar de manera precisa el flujo de entrada en 
            entornos controlados.''', style="italic"), justify="center")
        elif opcion_colaR == "8":
            break
        else:
            console.print("Opción no válida", style="bold red")

            
def submenu_colaSR():
    cola_sr = ColaSR()  # Suponemos que tienes definida esta clase ColaSR en algún lugar del código

    while True:
        # Usamos Rich para imprimir el menú con un panel estilizado
        console.print(Panel(
            "1. Encolar al inicio\n"
            "2. Desencolar del final\n"
            "3. Consultar el frente\n"
            "4. Consultar el final\n"
            "5. Verificar si la cola está vacía\n"
            "6. Recorrer\n"
            "7. Tamaño de la Cola\n"
            "8. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola de Salida Restringida[/]", border_style="red"))

        opcion_colasr = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_colasr == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            cola_sr.agregar_inicio(elemento)
            console.print("Elemento agregado.", style="green")
        elif opcion_colasr == "2":
            if not cola_sr.esta_vacia():
                cola_sr.desencolar_final()
                console.print("Elemento eliminado de la cola.", style="red")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colasr == "3":
            if not cola_sr.esta_vacia():
                primer_elemento = cola_sr.consultar_frente()
                console.print(f"Primer elemento de la cola: {primer_elemento}", style="bold magenta")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colasr == "4":
            if not cola_sr.esta_vacia():
                ultimo_elemento = cola_sr.consultar_final()
                console.print(f"Último elemento de la cola: {ultimo_elemento}", style="bold magenta")
            else:
                console.print("La cola está vacía.", style="yellow")
        elif opcion_colasr == "5":
            if cola_sr.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_colasr == "6":
            console.print("Recorriendo desde el inicio:")
            cola_sr.recorrer_inicio()
        elif opcion_colasr == "7":
            console.print(f"La cola contiene {cola_sr.size()} Elemento/s.", style="bold magenta")
        elif opcion_colasr == "0":
            console.print(Text('''La Cola de Salida Restringida es una estructura de datos donde sólo se puede eliminar el primer 
            elemento encolado, es decir, sólo se permite desencolar por un extremo. Esto es útil para casos 
            donde se necesita mantener un control estricto sobre el orden de salida de los elementos, garantizando 
            que el proceso siga un orden estrictamente FIFO (First In, First Out).''', style="italic"), justify="center")
        elif opcion_colasr == "8":
            break
        else:
            console.print("Opción no válida", style="bold red")


def submenu_colaPA():
    cola_pa = ColaPA() 

    while True:
        console.print(Panel(
            "1. Encolar\n"
            "2. Eliminar elemento menor prioritario\n"
            "3. Consultar elemento de menor prioridad\n"
            "4. Verificar si la cola está vacía\n"
            "5. Tamaño de la Cola\n"
            "6. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola de Prioridad Ascendente[/]", border_style="red"))

        opcion_colapa = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_colapa == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            prioridad = console.input("[bold orange]Ingrese la prioridad del elemento (con número entero): [/]")
            if prioridad.isdigit():
                cola_pa.encolar(elemento, int(prioridad))
                console.print("Elemento agregado.", style="green")
            else:
                console.print("Por favor, ingrese un número entero como prioridad.", style="red")

        elif opcion_colapa == "2": 
            if cola_pa.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                cola_pa.menos_p()
                console.print("Elemento de menor prioridad desencolado.", style="red")
        elif opcion_colapa == "3":
            if cola_pa.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                elemento = cola_pa.consultar_min()
                console.print(f"Elemento de menor prioridad: {elemento}", style="bold magenta")
        elif opcion_colapa == "4":
            if cola_pa.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_colapa == "5":
            console.print(f"La cola contiene {cola_pa.size()} Elemento/s.", style="bold magenta")
        elif opcion_colapa == "0":
            console.print(Text('''Las Colas de Prioridad gestionan elementos según su prioridad en lugar de el orden de llegada. 
            En la versión Ascendente, los elementos con menor valor de prioridad salen primero, mientras que 
            en la versión Descendente, los de mayor prioridad salen primero.''', style="italic"), justify="center")
        elif opcion_colapa == "6":
            break
        else:
            console.print("Opción no válida", style="bold red")
        

def submenu_colaPD():
    cola_pd = ColaPD()  # Suponemos que tienes definida esta clase ColaPD en algún lugar del código

    while True:
        # Usamos Rich para imprimir el menú con un panel estilizado
        console.print(Panel(
            "1. Encolar\n"
            "2. Eliminar elemento de mayor prioridad\n"
            "3. Consultar elemento de mayor prioridad\n"
            "4. Verificar si la cola está vacía\n"
            "5. Tamaño de la Cola\n"
            "6. Regresar\n"
            "0. Definición", title="[bold red]Menú Cola de Prioridad Descendente[/]", border_style="red"))

        opcion_colapd = console.input("[bold orange]Ingresa una opción: [/]")

        if opcion_colapd == "1":
            elemento = console.input("[bold orange]Ingrese el elemento a encolar: [/]")
            prioridad = console.input("[bold orange]Ingrese la prioridad del elemento (con número entero): [/]")
            if prioridad.isdigit():
                cola_pd.encolar(int(prioridad), elemento)
                console.print("Elemento agregado.", style="green")
            else:
                console.print("Por favor, ingrese un número entero como prioridad.", style="red")

        elif opcion_colapd == "2": 
            if cola_pd.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                cola_pd.menos_p()
                console.print("Elemento de mayor prioridad desencolado.", style="red")
        elif opcion_colapd == "3":
            if cola_pd.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                elemento = cola_pd.consultar_max()
                console.print(f"Elemento de mayor prioridad: {elemento}", style="bold magenta")
        elif opcion_colapd == "4":
            if cola_pd.esta_vacia():
                console.print("La cola está vacía.", style="yellow")
            else:
                console.print("La cola no está vacía", style="green")
        elif opcion_colapd == "5":
            console.print(f"La cola contiene {cola_pd.size()} Elemento/s.", style="bold magenta")
        elif opcion_colapd == "0":
            console.print(Text('''Las Colas de Prioridad gestionan elementos según su prioridad en lugar de el orden de llegada. 
            En la versión Ascendente, los elementos con menor valor de prioridad salen primero, mientras que 
            en la versión Descendente, los de mayor prioridad salen primero.''', style="italic"), justify="center")
        elif opcion_colapd == "6":
            break
        else:
            console.print("Opción no válida", style="bold red")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                mostrar_submenu_listas()
                opcion_lista = input("Seleccione una opción de lista: ")
                if opcion_lista == "1":
                    submenu_lista_simple()
                    pass
                elif opcion_lista == "2":
                    sub_menu_lista_doble()
                    pass
                elif opcion_lista == "3":
                    submenu_listaDobleCircular()
                    pass
                elif opcion_lista == "4":
                    submenu_listaSimpleCircular()
                    pass
                elif opcion_lista == "5":
                    print("-------------------------------------------------------")
                    
                    break
                
                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                mostrar_submenu_pilas()
                opcion_pila = input("Seleccione una opción de pila: ")
                if opcion_pila == "1":
                    submenu_pila()
                    pass
                elif opcion_pila == "2":
                    submenu_pilaE()
                    pass
                elif opcion_pila == "3":
                    print("-------------------------------------------------------")
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "3":
            while True:
                mostrar_submenu_colas()
                opcion_cola = input("Seleccione una opción de cola: ")
                if opcion_cola == "1":
                    submenu_cola()
                    pass
                elif opcion_cola == "2":
                    submenu_colaDoble()
                    pass
                elif opcion_cola == "3":
                    submenu_colaCircular()
                    pass
                elif opcion_cola == "4":
                    submenu_colaRestringida()
                    pass
                elif opcion_cola == "5":
                    submenu_colaSR()
                    pass
                elif opcion_cola == "6":
                    submenu_colaPA()
                    pass
                elif opcion_cola == "7":
                    submenu_colaPD()
                    pass
                elif opcion_cola == "8":
                    print("-------------------------------------------------------")
                    break
                
                else:
                    print("Opción no válida.")

        elif opcion == "0":
            print("Gracias por utilizar el portafolio de estructuras de datos.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
