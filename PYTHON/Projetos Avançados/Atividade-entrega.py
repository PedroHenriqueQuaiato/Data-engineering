import boto3
import pandas as pd
import os
from io import BytesIO
from io import StringIO
import botocore.session

session = botocore.session.Session()
session.set_config_variable('signature_version', 's3v4')

cliente = boto3.client(
    's3',
    endpoint_url='https://127.0.0.1:9000',
    aws_access_key_id='5pQdehYsquOt0o2K',
    aws_secret_access_key="y8gk8SmENxwRrdzAGF8LLOtUPTfwjo9r",
    aws_session_token=None,
    region_name='sa-east-1',
    verify=False,
    config=boto3.session.Config(signature_version='s3v4')
)

# Leitura do arquivo JSON
arquivo = pd.read_json(r"C:\Users\pedro\Downloads\estados (1).json")

# Extrair estados únicos
estados_unicos = arquivo['uf'].unique()

# Criar diretórios e organizar cidades por estado
for estado in estados_unicos:
    # Criar pasta para o estado
    caminho_estado = fr"C:\Users\pedro\OneDrive\Área de Trabalho\ESTADOS\{estado}"
    os.makedirs(caminho_estado, exist_ok=True)

    # Filtrar as cidades do estado
    cidades_estado = arquivo[arquivo['uf'] == estado]['nome']
    
    # Criar arquivo CSV para o estado
    caminho_csv = os.path.join(caminho_estado, 'cidades.csv')
    cidades_estado.to_csv(caminho_csv, index=False)

    print(f"Arquivo cidades.csv para o estado {estado} salvo em {caminho_csv}")


csv_buffer = StringIO()  # criar o CSV ou o arquivo na memoria   

arquivo.to_csv(csv_buffer)  # aqui fazemos o processo de salvamento, porem ao inves de colocar o diretorio para salvar, colocamos o nosso CSV que é igual ao StringIO()

cliente.put_object(Body=csv_buffer.getvalue(), Bucket='awari-aula-6', Key=f"Aula/{estado}/cidades.csv")
