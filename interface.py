import tkinter as tk
import pandas as pd
import numpy as np

consultas_csv = pd.read_csv("consultas.csv")
consultas = pd.DataFrame(consultas_csv)

class TelaPrincipal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Clinica Ambição")



        self.button_tela_cadastro = tk.Button(
            self.master, text="Cadastro consulta", command=self.abrir_tela_cadastro)
        self.button_tela_cadastro.grid(row=3, column=0, padx=5, pady=5)

        self.button_tela_pesquisa = tk.Button(
            self.master,text="Pesquisar consulta",command=self.abrir_tela_pesquisa
        )
        self.button_tela_pesquisa.grid(row=3, column=1, padx=5, pady=5)

        self.button_consultas_data = tk.Button(
            self.master,text="Consultas do dia",command=self.abrir_consulta_data
        )
        self.button_consultas_data.grid(row=4, column=0, padx=5, pady=5)


    def abrir_tela_cadastro(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaCadastro(nova_tela)

    def abrir_tela_pesquisa(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPesqConsulta(nova_tela)
    
    def abrir_consulta_data(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        ListaConsultas(nova_tela)
    



class TelaCadastro(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Cadastro Consulta")

        self.label_inicio = tk.Label(self.master, text="Horario de inicio:")
        self.label_inicio.grid(row=0, column=0, padx=5, pady=5)
        self.entry_inicio = tk.Entry(self.master)
        self.entry_inicio.grid(row=0, column=1, padx=5, pady=5)

        self.label_fim = tk.Label(
            self.master, text="Horario de fim:")
        self.label_fim.grid(row=1, column=0, padx=5, pady=5)
        self.entry_fim = tk.Entry(self.master)
        self.entry_fim.grid(row=1, column=1, padx=5, pady=5)

        self.label_cpf = tk.Label(
            self.master, text="CPF do paciente:")
        self.label_cpf.grid(row=2, column=0, padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.master)
        self.entry_cpf.grid(row=2, column=1, padx=5, pady=5)

        self.label_nome = tk.Label(
            self.master, text="Nome do paciente:")
        self.label_nome.grid(row=3, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(self.master)
        self.entry_nome.grid(row=3, column=1, padx=5, pady=5)

        self.button_cadastrar = tk.Button(
            self.master, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.grid(row=4, column=0, padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=4, column=1, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)

    def cadastrar(self):
        nome = self.entry_nome.get()
        hora_inicio = self.entry_inicio.get()
        hora_fim = self.entry_fim.get()
        cpf = self.entry_cpf.get()

        nova_linha = {'cpf_paciente': cpf, 'paciente': nome,
                      'inicio': hora_inicio,'termino':hora_fim}
        
        consultas.loc[len(consultas)] = nova_linha

        print(consultas)

        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


class TelaPesqConsulta(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pesquisa Consulta")

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=3, column=1, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


class ListaConsultas(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Consultas do dia")

        
        self.label_consulta = tk.Label(self.master, text="Data das consultas:")
        self.label_consulta.grid(row=0, column=0, padx=5, pady=5)
        self.entry_consulta = tk.Entry(self.master)
        self.entry_consulta.grid(row=0, column=1, padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=3, column=1, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)





root = tk.Tk()
TelaPrincipal(root)
root.mainloop()
