import os
from google.cloud import bigquery
import requests
import pandas as pd

def google_cloud_connection():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googlecredentials.json"
    project_id = 'manchester-ai'
    client = bigquery.Client()
    return client


def api_get_dataframe(url):
    response = requests.get(url)

    if response.status_code == 200:
        resposta = response.json()
        df = pd.json_normalize(resposta)
        return df
    else:
        print(f"Erro na requisição: {response.status_code}")
