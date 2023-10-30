import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Função para lidar com o botão "Salvar"


def salvar_registro():
    ra = entrada_ra.get()
    nome = entrada_nome.get()
    data_nascimento = entrada_data_nascimento.get()

    if ra and nome and data_nascimento:
        dados = {'RA': [ra], 'Nome': [nome],
                 'Data de Nascimento': [data_nascimento]}
        df = pd.DataFrame(data=dados)

        # Adiciona os dados ao DataFrame ou cria um novo DataFrame, se ainda não existir
        if 'alunos.csv' in os.listdir():
            df.to_csv('alunos.csv', mode='a', header=False, index=False)
        else:
            df.to_csv('alunos.csv', index=False)

        status_label.config(text='Registro salvo com sucesso!')
    else:
        status_label.config(text='Erro: Preencha todos os campos.')


# Cria a janela principal
janela = tk.Tk()
janela.title("Registro de Alunos")

# Cria rótulos e campos de entrada para RA, nome e data de nascimento
rotulo_ra = ttk.Label(janela, text="RA:")
rotulo_nome = ttk.Label(janela, text="Nome:")
rotulo_data_nascimento = ttk.Label(janela, text="Data de Nascimento:")

entrada_ra = ttk.Entry(janela)
entrada_nome = ttk.Entry(janela)
entrada_data_nascimento = ttk.Entry(janela)

# Cria um botão "Salvar" que chama a função salvar_registro
botao_salvar = ttk.Button(janela, text="Salvar", command=salvar_registro)

# Cria um rótulo para exibir o status
status_label = ttk.Label(janela, text="")

# Posiciona os elementos na janela
rotulo_ra.grid(row=0, column=0)
rotulo_nome.grid(row=1, column=0)
rotulo_data_nascimento.grid(row=2, column=0)
entrada_ra.grid(row=0, column=1)
entrada_nome.grid(row=1, column=1)
entrada_data_nascimento.grid(row=2, column=1)
botao_salvar.grid(row=3, column=0, columnspan=2)
status_label.grid(row=4, column=0, columnspan=2)

# Inicia a interface gráfica
janela.mainloop()
