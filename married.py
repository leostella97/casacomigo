import tkinter as tk
import random

# Define uma função que move o botão "Sim" para uma posição aleatória na janela
def mover_botao_sim(event):
    # Obtém as dimensões da janela
    largura = janela.winfo_width()
    altura = janela.winfo_height()

    # Define as novas coordenadas x e y do botão
    novo_x = random.randint(0, largura - botao_sim.winfo_width())
    novo_y = random.randint(0, altura - botao_sim.winfo_height())

    # Move o botão para as novas coordenadas
    botao_sim.place(x=novo_x, y=novo_y)

# Cria uma janela
janela = tk.Tk()

# Define o tamanho da janela
janela.geometry("500x300")

# Adiciona um rótulo com o texto "Quer casar comigo?"
texto = tk.Label(janela, text="Quer casar comigo?", font=("Arial Bold", 24))
texto.pack(pady=50)

# Adiciona o botão "Sim" e define seu comando para mover o botão para uma posição aleatória
botao_sim = tk.Button(janela, text="Sim", font=("Arial", 18))
botao_sim.place(x=200, y=200)
botao_sim.bind("<Enter>", mover_botao_sim)

# Adiciona o botão "Não"
botao_nao = tk.Button(janela, text="Não", font=("Arial", 18))
botao_nao.place(x=300, y=200)

# Inicia a janela
janela.mainloop()
