import requests
from datetime import datetime



def get_dollar_value():
    api_url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx"
    params = {
        'user': 'alvaro.sepgon@gmail.com',
        'pass': 'Testing01',                
        'firstdate': datetime.now().strftime('%Y-%m-%d'),
        'lastdate': '',
        'timeseries': 'F073.TCO.PRE.Z.D',
        'function': 'GetSeries'
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        try:
            dollar_value = data['Series']['Obs'][0]['value']
            return float(dollar_value)
        except (KeyError, IndexError, ValueError) as e:
            raise ValueError("Error al extraer el valor del dólar de la respuesta de la API.") from e
    else:
        raise ConnectionError(f"No se pudo obtener los datos. Código de estado: {response.status_code}")
