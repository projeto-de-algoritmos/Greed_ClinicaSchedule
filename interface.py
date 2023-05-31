import tkinter as tk
import pandas as pd
import numpy as np
from partitioning import interval_partioniong

consultas_csv = pd.read_csv("paciente.csv")
consultas = pd.DataFrame(consultas_csv)

atendimento_csv = pd.read_csv("atendimento.csv")
atendimento = pd.DataFrame(atendimento_csv)

import pandas as pd

# Exemplo de uso
procedimentos = [
    {'nome': 'Consulta médica', 'valor': 200, 'duracao': 1},
    {'nome': 'Exame de sangue', 'valor': 150, 'duracao': 0.5},
    {'nome': 'Raio-X', 'valor': 300, 'duracao': 1.5},
    {'nome': 'Eletrocardiograma', 'valor': 250, 'duracao': 1},
    {'nome': 'Tomografia', 'valor': 500, 'duracao': 2},
    {'nome': 'Endoscopia', 'valor': 400, 'duracao': 1.5},
]



def obter_nome_por_cpf(cpf, dataframe):
    # Filtra as linhas do dataframe com base no CPF
    
    linhas_filtradas = dataframe[dataframe['cpf_paciente'] == cpf]
 
    
    # Verifica se há linhas correspondentes ao CPF
    if not linhas_filtradas.empty:
        # Obtém o valor da coluna "nome"
        
        nome = linhas_filtradas.iloc[0]['paciente']
        return nome
    else:
        return None
    
def obter_inicio_por_cpf(cpf, dataframe):
    # Filtra as linhas do dataframe com base no CPF
    
    linhas_filtradas = dataframe[dataframe['cpf_paciente'] == cpf]

    
    # Verifica se há linhas correspondentes ao CPF
    if not linhas_filtradas.empty:
        # Obtém o valor da coluna "nome"
        
        inicio = linhas_filtradas.iloc[0]['inicio']
        return inicio
    else:
        return None
    
def obter_fim_por_cpf(cpf, dataframe):
    # Filtra as linhas do dataframe com base no CPF
    
    linhas_filtradas = dataframe[dataframe['cpf_paciente'] == cpf]
    
    # Verifica se há linhas correspondentes ao CPF
    if not linhas_filtradas.empty:
        # Obtém o valor da coluna "nome"
        
        fim = linhas_filtradas.iloc[0]['termino']
        return fim
    else:
        return None

def obter_medico_por_cpf(cpf, dataframe):
    # Filtra as linhas do dataframe com base no CPF
    
    linhas_filtradas = dataframe[dataframe['cpf_paciente'] == cpf]

    
    # Verifica se há linhas correspondentes ao CPF
    if not linhas_filtradas.empty:
        # Obtém o valor da coluna "nome"
        
        medico = linhas_filtradas.iloc[0]['medico']
        return medico
    else:
        return None
    
def obter_sala_por_cpf(cpf, dataframe):
    # Filtra as linhas do dataframe com base no CPF
    
    linhas_filtradas = dataframe[dataframe['cpf_paciente'] == cpf]

    
    # Verifica se há linhas correspondentes ao CPF
    if not linhas_filtradas.empty:
        # Obtém o valor da coluna "nome"
        
        sala = linhas_filtradas.iloc[0]['sala']
        return sala
    else:
        return None


def filtra_data(df, string):
    # Lista para armazenar as linhas correspondentes
    linhas_filtradas = []
    
    filtro = df[df["data"] == string]

    linhas_filtradas = filtro["cpf_paciente"].to_list()

    return linhas_filtradas


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
        
        self.button_consultas_data = tk.Button(
            self.master,text="Procedimentos",command=self.abrir_tela_procedimento
        )
        self.button_consultas_data.grid(row=4, column=1, padx=5, pady=5)


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

    def abrir_tela_procedimento(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaProcedimentos(nova_tela)
    
    

class TelaProcedimentos(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Procedimentos")
    
        
        # Criar lista
        self.lista = tk.Listbox(self.master,height=10, width=90)
        self.lista.pack()

        self.botao = tk.Button(self.master, text="Tempo disponivel",command=self.abrir_tela_knap)
        self.botao.pack()


        # Adicionar procedimentos à lista
        for procedimento in procedimentos:
            nome = procedimento['nome']
            valor = procedimento['valor']
            duracao = procedimento['duracao']
            item = f"{nome} - Valor: {valor} - Duração: {duracao} horas"
            self.lista.insert(tk.END, item)

    def abrir_tela_knap(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        KnapsackConsulta(nova_tela)
    


    
class KnapsackConsulta(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Disponibilidade")

        self.label_horas = tk.Label(self.master, text="Horas")
        self.label_horas.grid(row=0, column=0, padx=5, pady=5)
        self.entry_horas = tk.Entry(self.master)
        self.entry_horas.grid(row=0, column=1, padx=5, pady=5)


        self.button_cadastrar = tk.Button(
            self.master, text="Priorizar consultas", command=self.knapsack)
        self.button_cadastrar.grid(row=5, column=0, padx=5, pady=5)

    def knapsack(self):
        horas = self.entry_horas.get()
    
    


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

        self.label_data = tk.Label(
            self.master, text="Data:")
        self.label_data.grid(row=4, column=0, padx=5, pady=5)
        self.entry_data = tk.Entry(self.master)
        self.entry_data.grid(row=4, column=1, padx=5, pady=5)

        self.button_cadastrar = tk.Button(
            self.master, text="Cadastrar", command=self.cadastrar)
        self.button_cadastrar.grid(row=5, column=0, padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=5, column=1, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)

    def cadastrar(self):
        nome = self.entry_nome.get()
        hora_inicio = self.entry_inicio.get()
        hora_fim = self.entry_fim.get()
        cpf = self.entry_cpf.get()
        data = self.entry_data.get()

        nova_linha = {'cpf_paciente': cpf, 'paciente': nome,
                      'inicio': hora_inicio,'termino':hora_fim,'data':data}
        
        consultas.loc[len(consultas)] = nova_linha


        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


class TelaPesqConsulta(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Pesquisa Consulta")

        self.label_cpf = tk.Label(self.master, text="cpf do paciente:")
        self.label_cpf.grid(row=0, column=0, padx=5, pady=5)
        self.entry_cpf = tk.Entry(self.master)
        self.entry_cpf.grid(row=0, column=1, padx=5, pady=5)

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=3, column=0, padx=5, pady=5)

        self.button_pesquisar = tk.Button(
           self.master,text='pesqusiar',command=self.pesquisar 
        )
        self.button_pesquisar.grid(row=3,column=1,padx=5,pady=5)

    def pesquisar(self):
        cpf = self.entry_cpf.get()
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaConsulta(nova_tela,cpf=cpf)    

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)


class TelaConsulta(tk.Frame):
    def __init__(self,master=None,cpf=int):
        super().__init__(master)
        self.master = master
        self.master.title("Consulta paciente")



        nome = obter_nome_por_cpf(int(cpf),consultas)
        inicio = obter_inicio_por_cpf(int(cpf),consultas)
        fim = obter_fim_por_cpf(int(cpf),consultas)
        medico = obter_medico_por_cpf(int(cpf),atendimento)
        sala = obter_sala_por_cpf(int(cpf),atendimento)

        print(sala)

        self.label_cpf = tk.Label(self.master, text=f"Consulta do(a){nome}")
        self.label_cpf.grid(row=0, column=0, padx=5, pady=5)

        self.label_cpf = tk.Label(self.master, text=f"Com inicio: {inicio}")
        self.label_cpf.grid(row=1, column=0, padx=5, pady=5)

        self.label_cpf = tk.Label(self.master, text=f"Com termino: {fim}")
        self.label_cpf.grid(row=2, column=0, padx=5, pady=5)
        
        self.label_cpf = tk.Label(self.master, text=f"Com Medico(a): {medico} na sala {sala}")
        self.label_cpf.grid(row=3, column=0, padx=5, pady=5)

        
        

        

        self.button_voltar = tk.Button(
            self.master, text="voltar", command=self.voltar)
        self.button_voltar.grid(row=4, column=0, padx=5, pady=5)

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

        self.button_pesquisar = tk.Button(
            self.master, text="pesquisar", command=self.pesquisar)
        self.button_pesquisar.grid(row=3, column=0, padx=5, pady=5)

    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela)
    
    def pesquisar(self):
        data = self.entry_consulta.get()

        data_c = filtra_data(consultas,data)

        self.master.destroy()
        nova_tela = tk.Tk()
        ListBoxConsultas(nova_tela,data=data_c)

class ListBoxConsultas(tk.Frame):
    def __init__(self,master=None,data=list):
        super().__init__(master)
        self.master = master
        self.master.title("consultas do dia x")

        # criando a Listbox
        self.listbox_consultas = tk.Listbox(self.master)
        self.listbox_consultas.pack(padx=5, pady=5)

        # Fazer a busca no grafo das pessoas que escutam aquele mesmo artista ou artistas o mais parecido possivel e retornar em um for dando insert
        # Adicionar itens à Listbox (apenas como exemplo)
        print(data)

        for i in data:
            self.listbox_consultas.insert(tk.END, i)

        self.button_voltar = tk.Button(
            self.master, text="Voltar", command=self.voltar)
        self.button_voltar.pack(padx=5, pady=5)



    def voltar(self):
        self.master.destroy()
        nova_tela = tk.Tk()
        TelaPrincipal(nova_tela) 


root = tk.Tk()
TelaPrincipal(root)
root.mainloop()
