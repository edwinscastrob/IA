import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://datos.bancomundial.org/country/CO"

try:
    response = requests.get(url)
    response.raise_for_status()

    # Obtener el contenido HTML de la respuesta
    html_content = response.text

    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Buscar los elementos div con las clases "indicator-item__title" y "indicator-item__data-info"
    title_elements = soup.find_all("div", class_="indicator-item__title")
    data_info_elements = soup.find_all("div", class_="indicator-item__data-info")

    # Crear una lista de diccionarios con los datos
    data = []
    for title, data_info in zip(title_elements, data_info_elements):
        data.append({
            "Título": title.text.strip(),
            "Valor": data_info.text.strip()
        })

    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(data)

    # Imprimir la tabla
    print(df)

except requests.exceptions.RequestException as e:
    print("Error al realizar la solicitud:", e)
