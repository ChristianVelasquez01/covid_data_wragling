import os
import platform
 
def print_header():
    clear_console()
    print_title_box()
    print_menu()
    
def print_get_departament():
    clear_console()
    print_title_box()
    separator()
    print(" Visualizar casos de COVID-19 de un departamento")
    separator()

def print_menu():
    separator()
    print(" Menú de opciones")
    separator()
    print(" 1. Visualizar casos de COVID-19 de un departamento")
    print(" 2. Visualizar casos de COVID-19 del deparamento de Risaralda")
    print(" 0. Salir")
    separator()
    
def print_risaralda_data():
    clear_console()
    print_title_box()
    separator()
    print(" Visualizando casos de COVID-19 del departamento de Risaralda")
    separator()
    
def print_title_box():
    title = "Casos positivos de COVID-19 en Colombia"
    
    top_header = '╔' + '═' * 79 + '╗'
    mid_header = '║' + ' '  * 79 + '║'
    text_header = '║' + ' '  * 20 + title.upper() + ' '  * 20 + '║'
    bottom_header = '╚' + '═' * 79 + '╝'

    print (top_header)
    print(mid_header)
    print(text_header)
    print(mid_header)
    print(bottom_header)
    
def print_error(message):
    print(f" Error al obtener o procesar los datos: {message}")
    separator()
    input(" Presione Enter para continuar...")

def separator():
    print("─" * 81)
    
def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def get_option():
    while True:
        option = input(" Seleccione una opción [0 - 2]: ")
        if option in ['0', '1', '2']:
            break
        else:
            separator()
            print(" Por favor, seleccione una opción válida.")
            separator()
            input(" Presione Enter para continuar...")
            clear_console()
            print_header()
    
    return option

def get_departament():
    departament = input(" Ingrese el nombre del departamento a visualizar: ").upper()
    
    return departament

def get_filtered_data(data_frame, columns_to_show):
    filtered_data = data_frame[list(columns_to_show.keys())]
    filtered_data.columns = list(columns_to_show.values())
    return filtered_data

def get_table_borders(col_widths):
    top_border = "┌" + "┬".join("─" * (w + 2) for w in col_widths) + "┐"
    mid_border = "├" + "┼".join("─" * (w + 2) for w in col_widths) + "┤"
    bottom_border = "└" + "┴".join("─" * (w + 2) for w in col_widths) + "┘"
    return top_border, mid_border, bottom_border

def get_row_format(col_widths):
    return "│ " + " │ ".join(f"{{:<{w}}}" for w in col_widths) + " │"

def print_table(filtered_data, col_widths):
    row_format = get_row_format(col_widths)
    top_border, mid_border, bottom_border = get_table_borders(col_widths)
    
    print(top_border)
    print(row_format.format(*filtered_data.columns))
    print(mid_border)
    
    for row in filtered_data.itertuples(index=False):
        print(row_format.format(*row))
    
    print(bottom_border)

def print_data_table(data_frame):
    columns_to_show = {
        'id_de_caso': 'ID',
        'ciudad_municipio_nom': 'Ciudad',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'sexo': 'Sexo',
        'fuente_tipo_contagio': 'Fuente contagio',
        'tipo_recuperacion': 'Tipo',
        'ubicacion': 'Ubicación',
        'estado': 'Estado',
        'recuperado': 'Recuperado',
        'fecha_inicio_sintomas': 'Fecha Sint',
        'fecha_diagnostico': 'Fecha Diag',
        'fecha_recuperado': 'Fecha Recu',
        'fecha_muerte': 'Fecha RIP'
    }
    col_widths = [7, 19, 12, 4, 4, 15, 9, 9, 9, 10, 12, 14, 12, 12]

    filtered_data = get_filtered_data(data_frame, columns_to_show)
    print_table(filtered_data, col_widths)
    
    input("\n Presione Enter para continuar...")