import time_windows_constrains
import traveling_sales_person
import vehicle_routing
import weight_constrains


def display_menu():
    options = {
        1: ("Opción 1: Viajante",
            "Busca encontrar la ruta más corta que permita a un viajero visitar un conjunto de ciudades una sola vez y regresar a la ciudad de origen."),
        2: ("Opción 2: Problema de Rutas",
            "Determina las rutas óptimas para un conjunto de vehículos que deben entregar bienes a un conjunto de clientes, minimizando el costo total de viaje."),
        3: ("Opción 3: Restricción de Peso",
            "Planifica las rutas de manera que se respeten las restricciones de capacidad de los vehículos."),
        4: ("Opción 4: Ventanas de Tiempo",
            "Asegura que las entregas se realicen dentro de las ventanas de tiempo asignadas a cada cliente.")
    }

    print("Seleccione una opción:")
    for key, (title, description) in options.items():
        print(f"{key}. {title}")
        print(f"   {description}\n")


def get_user_choice():
    while True:
        try:
            choice = int(input("Ingrese el número de la opción seleccionada: "))
            if choice in range(1, 5):
                return choice
            else:
                print("Por favor, ingrese un número válido entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def get_tsp_data():
    while True:
        try:
            num_places = int(input("Ingrese la cantidad de lugares: "))
            if num_places > 0:
                break
            else:
                print("Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    distance_matrix = []
    print(f"Ingrese la matriz de distancias ({num_places}x{num_places}):")
    for i in range(num_places):
        row = []
        for j in range(num_places):
            if i == j:
                row.append(0)
                continue
            while True:
                try:
                    distance = int(input(f"Distancia de localización {i + 1} a localización {j + 1}: "))
                    row.append(distance)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        distance_matrix.append(row)

    index = int(input("Ingrese el índice de inicio: "))

    return num_places, distance_matrix, index


def get_vr_data():
    while True:
        try:
            num_places = int(input("Ingrese la cantidad de lugares: "))
            if num_places > 0:
                break
            else:
                print("Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    distance_matrix = []
    print(f"Ingrese la matriz de distancias ({num_places}x{num_places}):")
    for i in range(num_places):
        row = []
        for j in range(num_places):
            if i == j:
                row.append(0)
                continue
            while True:
                try:
                    distance = int(input(f"Distancia de localización {i + 1} a localización {j + 1}: "))
                    row.append(distance)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        distance_matrix.append(row)

    index = int(input("Ingrese el índice de inicio: "))
    car_num = int(input("Ingrese el cantidad de autos: "))

    return num_places, distance_matrix, index, car_num


def get_vrw_data():
    while True:
        try:
            num_places = int(input("Ingrese la cantidad de lugares: "))
            if num_places > 0:
                break
            else:
                print("Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    distance_matrix = []
    print(f"Ingrese la matriz de distancias ({num_places}x{num_places}):")
    weight_list = []

    for i in range(num_places):
        weight = int(input(f"Ingrese la demanda del sitio {i}: "))
        weight_list.append(weight)
        row = []
        for j in range(num_places):
            if i == j:
                row.append(0)
                continue
            while True:
                try:
                    distance = int(input(f"Distancia de localización {i + 1} a localización {j + 1}: "))
                    row.append(distance)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        distance_matrix.append(row)

    index = int(input("Ingrese el índice de inicio: "))
    car_num = int(input("Ingrese el cantidad de autos: "))
    capacity = input("Ingrese la capacidad de los autos separado por espacios: ").split()
    car_capacity = []
    for i in capacity:
        car_capacity.append(int(i))

    return num_places, distance_matrix, index, car_num, weight_list, car_capacity


def get_vrtw_data():
    while True:
        try:
            num_places = int(input("Ingrese la cantidad de lugares: "))
            if num_places > 0:
                break
            else:
                print("Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    time_matrix = []
    time_windows = []
    print(f"Ingrese la matriz de tiempo ({num_places}x{num_places}):")
    for i in range(num_places):
        time = input(f"Ingrese la ventana de tiempo para el lugar {i + 1} separado por espacios: ").split()
        time_windows.append((int(time[0]), int(time[1])))
        row = []
        for j in range(num_places):
            if i == j:
                row.append(0)
                continue
            while True:
                try:
                    distance = int(input(f"Tiempo de localización {i + 1} a localización {j + 1}: "))
                    row.append(distance)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
        time_matrix.append(row)

    index = int(input("Ingrese el índice de inicio: "))
    car_num = int(input("Ingrese el cantidad de autos: "))

    return num_places, time_matrix, index, car_num, time_windows


def main():
    display_menu()
    choice = get_user_choice()

    if choice == 1:
        print("Has seleccionado la Opción 1: Viajante.")
        num_places, distance_matrix, index = get_tsp_data()
        print(f"Cantidad de lugares: {num_places}")
        print("Matriz de distancias:")
        # Get data!!!!
        data = {}
        data["distance_matrix"] = distance_matrix
        data['depot'] = index
        data["num_vehicles"] = 1

        for row in distance_matrix:
            print(row)
        result = traveling_sales_person.main(data)
        print(result)

    elif choice == 2:
        print("Has seleccionado la Opción 2: Problema de Rutas. Pidiendo datos específicos...")
        num_places, distance_matrix, index, car_num = get_vr_data()
        data = {}
        data['distance_matrix'] = distance_matrix
        data['depot'] = index
        data['num_vehicles'] = car_num
        print(data)

        result = vehicle_routing.main(data)
        print(result)

        # Aquí pedirá los datos específicos para Problema de Rutas (implementar más adelante)

    elif choice == 3:
        print("Has seleccionado la Opción 3: Restricción de Peso. Pidiendo datos específicos...")
        num_places, distance_matrix, index, car_num, weight_list, car_capacity = get_vrw_data()
        data = {}
        data['distance_matrix'] = distance_matrix
        data['depot'] = index
        data['num_vehicles'] = car_num
        data["demands"] = weight_list
        data["vehicle_capacities"] = car_capacity
        print(data)

        result = weight_constrains.main(data)
        print(result)

    elif choice == 4:
        print("Has seleccionado la Opción 4: Ventanas de Tiempo. Pidiendo datos específicos...")
        num_places, time_matrix, index, car_num, time_windows = get_vrtw_data()
        data = {}
        data['time_matrix'] = time_matrix
        data['depot'] = index
        data['num_vehicles'] = car_num
        data["time_windows"] = time_windows
        print(data)
        result = time_windows_constrains.main(data)
        print(result)


if __name__ == "__main__":
    main()
