import pandas as pd
import requests
import csv

import requests
import pandas as pd
from dotenv import dotenv_values



APP_ID, APP_KEY = dotenv_values('.env').values()

urlclima = f'http://api.weatherunlocked.com/api/current/51.50,-0.12?app_id={APP_ID}&app_key={APP_KEY}'

response = requests.get(
    urlclima,
    )

if response.ok: # chequeamos si la respuesta fue correcta

    data_response=response.json()
    
    df = pd.DataFrame(data=data_response, index=["Linea 1"]) 

    df.to_json('salida.json',
    orient='records')

    print('Archivo JSON descargado y guardado exitosamente.')

else:
    print(f'Error. Código de estado: {response.status_code}\nMensaje de error: {response.text}')