import os
import psycopg2

def conectar_banco():
    try:
        conn = psycopg2.connect(
            dbname="territorios",
            user="postgres",
            password="postgres",
            host="localhost",
            port='5434'
        )
        print("Conexão bem-sucedida!")
        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def inserir_imagem(conn, nome_arquivo, caminho_imagem):
    try:
        cursor = conn.cursor()
        with open(caminho_imagem, "rb") as file:
            bits_imagem = file.read()
        cursor.execute("INSERT INTO territorios (nome, imagem) VALUES (%s, %s)", (nome_arquivo, psycopg2.Binary(bits_imagem)))
        conn.commit()
        cursor.close()
        print(f"Imagem {nome_arquivo} inserida com sucesso!")
    except psycopg2.Error as e:
        print("Erro ao inserir imagem no banco de dados:", e)

def listar_arquivos_em_diretorio(diretorio):
    arquivos = []
    for nome_arquivo in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        if os.path.isfile(caminho_completo) and nome_arquivo.lower().endswith('.pdf'):
            nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]
            arquivos.append((nome_arquivo_sem_extensao, caminho_completo))
    return arquivos

def main():
    conn = conectar_banco()
    if conn:
        diretorio = "C:\\Users\\pedro\\OneDrive\\Área de Trabalho\\Territorios"
        lista_arquivos = listar_arquivos_em_diretorio(diretorio)
        for nome_arquivo, caminho in lista_arquivos:
            inserir_imagem(conn, nome_arquivo, caminho)
        conn.close()

if __name__ == "__main__":
    main()
