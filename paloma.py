import requests
from bs4 import BeautifulSoup

def obtener_pib_colombia():
    # URL de la página con los datos del PIB
    url = "https://datos.bancomundial.org/country/CO"
    
    # Realizar la solicitud GET a la página
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup para analizar el contenido HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar el elemento que contiene el valor del PIB
        pib_element = soup.find("span", class_="field-content")
        
        # Obtener el texto del elemento y limpiar los caracteres no deseados
        pib = pib_element.text.strip().replace(",", "")
        
        # Convertir el valor a un número decimal
        pib = float(pib)
        
        return pib
    else:
        # Si la solicitud no fue exitosa, mostrar un mensaje de error
        print("No se pudo obtener el PIB de Colombia.")
        return None

# Llamar a la función para obtener el PIB de Colombia
pib_colombia = obtener_pib_colombia()

# Verificar si se obtuvo el valor del PIB exitosamente
if pib_colombia is not None:
    print("PIB de Colombia actualizado:", pib_colombia)
