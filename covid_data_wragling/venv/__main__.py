import api
import wragling as wra

def main():
    departament = "RISARALDA"

    try:
        data = api.get_data(1000, departament)
        data_frame = api.process_data(data)

        print("\nANTES DE LA IMPUTACION DE DATOS:\n")
        wra.show_understanding_data(data_frame)
        input("\n Presiona Enter para continuar...")
        
        print("\nDESPUES DE LA IMPUTACION DE DATOS:\n")
        data_frame = wra.data_imputation(data_frame)
        
        wra.show_understanding_data(data_frame)
        input("\n Presiona Enter para continuar...")
        
        wra.print_stats(data_frame)
        input("\n Presiona Enter para continuar...")
    
    except Exception as message:
        print(message)

if __name__ == "__main__":
    main()