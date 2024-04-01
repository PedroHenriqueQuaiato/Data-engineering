import boto3 
import pandas as pd 
from io import BytesIO
from io import StringIO

# formas de conexão via URL no MiniIO ( e configuração com boto3)

cliente = boto3.client(
    's3',
    endpoint_url="http://127.0.0.1:9000",             # URL que é gerada no arquivo de backup da key do MiniIO, porem como estamos rodando via docker devemos colocar o nome do serviço ou o 127.0.0.1
    aws_access_key_id="5pQdehYsquOt0o2K",   # Aqui deve ser a Access key que tem no arquivo de backup da chave do MiniIO
    aws_secret_access_key="y8gk8SmENxwRrdzAGF8LLOtUPTfwjo9r",  # Chave secreta do MiniIO mesmo arquivo de backup
    aws_session_token=None,  
    region_name='sa-east-1',  # região da AWS que estamos usando, podemos escolher isso depois de criar o bucket
    verify=False,
    config=boto3.session.Config(signature_version='s3v4')

)

data = {
    'macas': [3, 2, 0, 1],         # aqui podemos excolher nossas aplicações com o pandas, não precisa ser necessariamente um data Frame, pode ser diferentes data sets 
    'laranjas': [0, 3, 7, 2]
}

compras_df = pd.DataFrame(data, index=['Alex', 'Roberto', 'Bernardo', 'Paulo'])

csv_buffer = StringIO()  # criar o CSV ou o arquivo na memoria   

compras_df.to_csv(csv_buffer)  # aqui fazemos o processo de salvamento, porem ao inves de colocar o diretorio para salvar, colocamos o nosso CSV que é igual ao StringIO()

cliente.put_object(Body=csv_buffer.getvalue(), Bucket='aula-awari-06', Key="Aula/compras.csv")  # serve para fazer o uploald   

# Aqui chamamos o cliente que guarda nossa conexão, em seguinda colocamos um put_object em seguinda colocamos o BORY que é igual ao nosso CSV_buffer e depois colocamos .GETVaulue 
# depois colocamos o parametro BUCKET seguinda do nosso bucket dentr odo miniIO, (devemos colocar o nome do Bucket) em seguinda por fim colocamos a Key, ou seja, 
#o nome do nosso arquivo, junto ao nosso diretorio (se não tiver o diretorio, ele cria sozinho e automatico se não tiver) 

