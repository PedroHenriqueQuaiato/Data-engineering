import itertools
import os

def gerar_combinacoes_caracteres(tamanho):
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[{]}|;:,<.>/?'
    return itertools.product(caracteres, repeat=tamanho)

def salvar_combinacoes_para_arquivo(tamanho, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for combinacao in gerar_combinacoes_caracteres(tamanho):
            senha = ''.join(combinacao)
            arquivo.write(senha + '\n')

def main():
    tamanho_senha = 4  # Defina o tamanho da senha desejado
    caminho_pasta = input("Digite o caminho da pasta onde deseja salvar o arquivo: ").strip()

    if not os.path.exists(caminho_pasta):
        print("O caminho especificado não existe.")
        return

    nome_arquivo = 'combinacoes_senha.txt'
    nome_com_caminho = os.path.join(caminho_pasta, nome_arquivo)

    salvar_combinacoes_para_arquivo(tamanho_senha, nome_com_caminho)

    print(f"Todas as combinações de senha de tamanho {tamanho_senha} foram salvas no arquivo '{nome_com_caminho}'.")

if __name__ == "__main__":
    main()
