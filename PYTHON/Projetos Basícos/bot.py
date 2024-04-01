import tkinter as tk
from tkinter import messagebox
from PIL import Image

def mostrar_imagem(prompt):
    if prompt == '1':
        imagem_path = 'C:\\Users\\pedro\\Downloads\\teste.png'
    elif prompt == '2':
        imagem_path = 'C:\\Users\\pedro\\Downloads\\teste1.png'
    elif prompt == '3':
        imagem_path = 'C:\\Users\\pedro\\Downloads\\teste2.png'
    elif prompt == '4':
        imagem_path = 'C:\\Users\\pedro\\Downloads\\teste3.png'
    else:
        messagebox.showerror("Erro", "Opção inválida!")
        return

    try:
        imagem = Image.open(imagem_path)
        imagem.show()
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado!")

def main():
    # Função a ser chamada quando o botão for pressionado
    def button_pressed():
        prompt = entry.get()
        mostrar_imagem(prompt)

    # Configurações da janela principal
    root = tk.Tk()
    root.title("MachineImaginator")

    # Criar e posicionar os widgets
    label = tk.Label(root, text="O que você deseja criar, mestre? Digite '1 2 3 4'")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Visualizar", command=button_pressed)
    button.pack()

    # Executar a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
