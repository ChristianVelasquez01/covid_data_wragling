import math

# Understading data
def show_understanding_data(data_frame):
    print("Number of rows::", data_frame.shape[0])
    print("Number of columns::", data_frame.shape[1])
    print("Column names::", data_frame.columns.values.tolist())
    print("Column data types::", data_frame.dtypes)
    print("Columns with Missing Values::", data_frame.columns[data_frame.isnull().any()].tolist())
    print("Number of rows with Missing Values::", len(data_frame[data_frame.isnull().any(axis=1)]))
    print("Sample Indices with missing data::", data_frame[data_frame.isnull().any(axis=1)].index.tolist()[0:20])
    print("General Stats::")
    print(data_frame.info())

    return data_frame

# Imputacion de datos
def data_imputation(data_frame):
    data_frame = delete_columns(data_frame)
    data_frame = delete_no_id_cases(data_frame)
    data_frame = correct_dates(data_frame)
    data_frame = delete_duplicates(data_frame)
    data_frame = correct_ages_to_positive_value(data_frame)
    data_frame = correct_gender(data_frame)
    data_frame = correct_null_age_values(data_frame)
    data_frame = correct_unknowns(data_frame)
    data_frame = correct_no_applies(data_frame)
    
    return data_frame

def delete_columns(data_frame):
    data_frame = data_frame.drop(columns=['fecha_reporte_web'])
    data_frame = data_frame.drop(columns=['fecha_de_notificaci_n'])
    data_frame = data_frame.drop(columns=['departamento'])
    data_frame = data_frame.drop(columns=['ciudad_municipio'])
    data_frame = data_frame.drop(columns=['unidad_medida'])
    data_frame = data_frame.drop(columns=['per_etn_'])
    data_frame = data_frame.drop(columns=['nom_grupo_'])
    data_frame = data_frame.drop(columns=['pais_viajo_1_cod'])
    data_frame = data_frame.drop(columns=['pais_viajo_1_nom'])
    
    return data_frame

def correct_dates(data_frame):
    data_frame['fecha_inicio_sintomas'] = data_frame['fecha_inicio_sintomas'].str.slice(stop=10)
    data_frame['fecha_diagnostico'] = data_frame['fecha_diagnostico'].str.slice(stop=10)
    data_frame['fecha_recuperado'] = data_frame['fecha_recuperado'].str.slice(stop=10)
    data_frame['fecha_muerte'] = data_frame['fecha_muerte'].str.slice(stop=10)
    
    return data_frame

def delete_duplicates(data_frame):
    data_frame = data_frame.drop_duplicates()
    
    return data_frame

def correct_ages_to_positive_value(data_frame):
    data_frame['edad'] = data_frame['edad'].astype(int)
    data_frame['edad'] = data_frame['edad'].abs()
    
    return data_frame

def correct_gender(data_frame):
    data_frame['sexo'] = data_frame['sexo'].replace('f', 'F')
    data_frame['sexo'] = data_frame['sexo'].replace('m', 'M')
    
    return data_frame

def correct_unknowns(data_frame):
    data_frame['ciudad_municipio_nom'] = data_frame['ciudad_municipio_nom'].fillna('Unknown')
    data_frame['tipo_recuperacion'] = data_frame['tipo_recuperacion'].fillna('Unknown')
    data_frame['ubicacion'] = data_frame['ubicacion'].replace('N/A', 'Unknown')
    data_frame['fuente_tipo_contagio'] = data_frame['fuente_tipo_contagio'].fillna('Unknown')
    data_frame['ubicacion'] = data_frame['ubicacion'].fillna('Unknown')
    data_frame['estado'] = data_frame['estado'].replace('N/A', 'Unknown')
    data_frame['recuperado'] = data_frame['recuperado'].replace('N/A', 'Unknown')
    data_frame['fecha_inicio_sintomas'] = data_frame['fecha_inicio_sintomas'].fillna('Unknown')
    data_frame['fecha_diagnostico'] = data_frame['fecha_diagnostico'].fillna('Unknown')
    
    return data_frame

def correct_null_age_values(data_frame):
    data_frame['edad'] = data_frame['edad'].fillna(data_frame['edad'].mean())
    
    return data_frame

def correct_no_applies(data_frame):
    data_frame['fecha_recuperado'] = data_frame['fecha_recuperado'].fillna('No Aplica')
    data_frame['fecha_muerte'] = data_frame['fecha_muerte'].fillna('No Aplica')
    
    return data_frame

def delete_no_id_cases(data_frame):
    data_frame['id_de_caso'] = data_frame['id_de_caso'].astype(int)
    data_frame = data_frame.drop(data_frame[data_frame['id_de_caso'] == 0].index)
    
    return data_frame

def print_stats(data_frame):
    print("\nEstadísticas generales:")
    
    plot_cli_age_range(data_frame)
    get_mean_age(data_frame)

    plot_cli_gender(data_frame)
    percent_of_gender(data_frame)

    percent_of_recoverys(data_frame)
    percent_of_deaths(data_frame)
    prom_age_deaths(data_frame)
    percent_of_unknowns(data_frame)

def get_mean_age(data_frame):
    mean_age = data_frame['edad'].mean()
    
    print(f"\nPromedio de edades: {mean_age}")

def plot_cli_age_range(data_frame):
    print("\nDistribución de edades:")
    
    age_ranges = range(0, 100, 10)
    frequencies = [0] * len(age_ranges)

    for age in data_frame['edad']:
        if not math.isnan(age):
            index = int(age // 10)
            if index < len(frequencies):
                frequencies[index] += 1

    for i, frequency in enumerate(frequencies):
        age_range = f"{age_ranges[i]:02d}-{age_ranges[i] + 9:02d}"
        bar = "#" * (frequency // 2)
        print(f"{age_range}: {bar}")
        
def plot_cli_gender(data_frame):
    print("\nDistribución por género:")
    
    gender_counts = data_frame['sexo'].value_counts()

    for gender, count in gender_counts.items():
        bar = "#" * (count // 4)
        print(f"{gender}: {bar}")
        
def percent_of_gender(data_frame):
    total_cases = len(data_frame)
    gender_counts = data_frame['sexo'].value_counts()
    
    print()
    for gender, count in gender_counts.items():
        percent = (count / total_cases) * 100
        print(f"Porcentaje de {gender}: {percent:.2f}%")
        
def percent_of_recoverys(data_frame):
    total_cases = len(data_frame)
    total_recovereds = len(data_frame[data_frame['recuperado'] == 'Recuperado'])
    percent = (total_recovereds / total_cases) * 100
    
    print(f"\nPorcentaje de recuperados: {percent:.2f}%")
    
def percent_of_deaths(data_frame):
    total_cases = len(data_frame)
    total_deaths = len(data_frame[data_frame['recuperado'] == 'Fallecido'])
    percent = (total_deaths / total_cases) * 100
    
    print(f"\nPorcentaje de fallecidos: {percent:.2f}%")
    
def prom_age_deaths(data_frame):
    prom_age_deaths = data_frame[data_frame['recuperado'] == 'Fallecido']['edad'].mean()
    print(f"Promedio de edad de los fallecidos: {prom_age_deaths:.2f}")
    
def percent_of_unknowns(data_frame):
    total_cases = len(data_frame)
    total_unknowns = len(data_frame[data_frame['recuperado'] == 'Unknown'])
    percent = (total_unknowns / total_cases) * 100
    
    print(f"\nPorcentaje de casos sin definir: {percent:.2f}%")
        
def data_frame_to_list_of_dicts(data_frame):
    list_of_dicts = data_frame.to_dict('records')
    
    return list_of_dicts