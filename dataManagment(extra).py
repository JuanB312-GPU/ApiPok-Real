# Se importa pandas para trabajar con dataframes.
import pandas as pd

# Lista de leads
leads = [
    {"id": 1, "name": "Ana Salcedo", "location": "Medellín", "budget": 200000000},
    {"id": 2, "name": "Santiago Gallo", "location": "Medellín", "budget": 500000000},
    {"id": 3, "name": "Carlota Habib", "location": "Medellín", "budget": 650000000},
    {"id": 4, "name": "Pablo Sánchez", "location": "Bogotá", "budget": 350000000},
    {"id": 5, "name": "Manuel Franco", "location": "Bogotá", "budget": 150000000},
    # ... más leads
]

# Se transforman los diccionarios en un dataFrame, para mejorar el manejo de la estructura.
df_leads = pd.DataFrame(leads)

# Se crea la función para filtrar la data, por defecto tiene a Medellín como locación.
def filter_leads(location = "Medellín"):
    filtered_leads = df_leads.loc[df_leads['location'] == location]
    return filtered_leads

# Ordena un dataframe de entrada en orden descendente, según los valores de la columna budget (Presupuesto).
def budget_order(data_structure = df_leads):
    sorted_leads_desc = data_structure.sort_values(by='budget', ascending=False)
    return sorted_leads_desc

print(budget_order(filter_leads()))
    

