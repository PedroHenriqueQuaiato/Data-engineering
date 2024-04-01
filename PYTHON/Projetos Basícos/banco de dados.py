import psycopg2

# Conectar ao banco de dados
conn = psycopg2.connect(
    dbname="Testes ",
    user="postgres",
    password="postgres",
    host="localhost",
    port='5434'
)
prompt = input('O que você quer criar mestre')

# Criar um cursor
cursor = conn.cursor()

# Executar uma consulta SQL para obter os dados
cursor.execute("SELECT * FROM contratos")

# Recuperar os resultados
rows = cursor.fetchall()

# Fechar o cursor e a conexão
cursor.close()
conn.close()

# Processar os resultados e armazenar em variáveis
ids = []
migracoes = []
ativacoes = []
revendas = []

for row in rows:
    ids.append(row[0])
    migracoes.append(int(row[1]))  # Converter para número (assumindo que são números)
    ativacoes.append(int(row[2]))  # Converter para número (assumindo que são números)
    revendas.append(row[3])

# Agora, as listas ids, migracoes, ativacoes e revendas contêm os dados de cada coluna
    
def operacao(migracoes, ativacoes):
    resultado = [ativacao - migracao for migracao, ativacao in zip(migracoes, ativacoes)]
    return resultado

# Chamar a função operacao
resultado_operacao = operacao(migracoes, ativacoes)

# Exibir o resultado
print("Resultado da operação:", resultado_operacao)
  