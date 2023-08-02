import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk

class FrameBusca(tk.LabelFrame):
    '''
    Frame onde são colocados os dados para realizar buscas
    '''

    def __init__(self, container):
        super().__init__(container)
        self.configure(width=400, text="Busca por imagens")
        self.pack(side=tk.TOP, fill=tk.X)

        self.__create_widgets()

    def altera_entries(self, event):
        '''
        Método para alterar quais campos são mostrados
        '''

        if self.combobox_busca.get() == 'Data':
            self.label_datainicial.grid(row=1, column=0, sticky=tk.W)
            self.input_datainicial.grid(row=1, column=1)

            self.label_datafinal.grid(row=1, column=2, sticky=tk.W)
            self.input_datafinal.grid(row=1, column=3)
        else:
            if self.label_datafinal.winfo_ismapped():
                self.label_datainicial.grid_forget()
                self.input_datainicial.grid_forget()
                self.label_datafinal.grid_forget()
                self.input_datafinal.grid_forget()

        if self.combobox_busca.get() == 'Nome':
            self.label_nome.grid(row=1, column=0, sticky=tk.W)
            self.input_nome.grid(row=1, column=1)
        else:
            if self.label_nome.winfo_ismapped():
                self.label_nome.grid_forget()
                self.input_nome.grid_forget()

        if self.combobox_busca.get() == 'Cidade':
            self.label_cidade.grid(row=1, column=0, sticky=tk.W)
            self.input_cidade.grid(row=1, column=1)
        else:
            if self.label_cidade.winfo_ismapped():
                self.label_cidade.grid_forget()
                self.input_cidade.grid_forget()

        if self.combobox_busca.get() == 'País':
            self.label_pais.grid(row=1, column=0, sticky=tk.W)
            self.input_pais.grid(row=1, column=1)
        else:
            if self.label_pais.winfo_ismapped():
                self.label_pais.grid_forget()
                self.input_pais.grid_forget()
        
    def __create_widgets(self):
        # Cria inputs/labels para busca
        self.label_datainicial = tk.Label(self, text='Data inicial:')
        self.input_datainicial = tk.Entry(self)

        self.label_datafinal = tk.Label(self, text='Data final:')
        self.input_datafinal = tk.Entry(self)

        self.label_nome = tk.Label(self, text='Nome:')
        self.input_nome = tk.Entry(self)

        self.label_cidade = tk.Label(self, text='Cidade:')
        self.input_cidade = tk.Entry(self)

        self.label_pais = tk.Label(self, text='País:')
        self.input_pais = tk.Entry(self)

        # Cria combobox que altera quais inputs aparecem
        self.combobox_label = tk.Label(self, text='Buscar por:')
        combobox_busca_values = ['Selecione um valor','Data', 'Nome', 'Cidade', 'País']
        self.combobox_busca = ttk.Combobox(self, values = combobox_busca_values)
        self.combobox_busca.current(0)
        self.combobox_label.grid(row=0, column=0)
        self.combobox_busca.grid(row=0, column=1)

        self.combobox_busca.bind("<<ComboboxSelected>>", self.altera_entries)

        self.button_buscar = tk.Button(self, text='Buscar')
        self.button_redefinir = tk.Button(self, text='Redefinir')

        self.button_buscar.grid(row=2, column=0),
        self.button_redefinir.grid(row=2, column=1)

class FrameDados(tk.LabelFrame):
    '''
    Frame onde são mostrados os dados da foto selecionada
    '''
    def __init__(self, container):
        super().__init__(container)

        self.configure(width=400, text="Imagem")
        self.pack(side=tk.BOTTOM, fill=tk.X)
        self.columnconfigure(2, minsize=150)
        self.columnconfigure(1, minsize=100, weight=1)

        self.__create_widgets()
        
    def __create_widgets(self):
        # Dados da imagem
        self.var_nome = tk.StringVar()
        self.label_nome = tk.Label(self, text='Nome:')
        self.dado_nome = tk.Label(self, textvariable=self.var_nome)

        self.var_data = tk.StringVar()
        self.label_data = tk.Label(self, text='Data:')
        self.dado_data = tk.Label(self, textvariable=self.var_data)

        self.var_coords = tk.StringVar()
        self.label_coords = tk.Label(self, text='Coordenadas:')
        self.dado_coords = tk.Label(self, textvariable=self.var_coords)

        self.var_cidade = tk.StringVar()
        self.label_cidade = tk.Label(self, text='Cidade:')
        self.dado_cidade = tk.Label(self, textvariable=self.var_cidade)

        self.var_pais = tk.StringVar()
        self.label_pais = tk.Label(self, text='País:')
        self.dado_pais = tk.Label(self, textvariable=self.var_pais)

        self.label_nome.grid(row=0, column = 0, sticky=tk.W)
        self.dado_nome.grid(row=0, column= 1)

        self.label_data.grid(row=1, column = 0, sticky=tk.W)
        self.dado_data.grid(row=1, column= 1)

        self.label_coords.grid(row=2, column = 0, sticky=tk.W)
        self.dado_coords.grid(row=2, column= 1)

        self.label_cidade.grid(row=3, column = 0, sticky=tk.W)
        self.dado_cidade.grid(row=3, column= 1)

        self.label_pais.grid(row=4, column = 0, sticky=tk.W)
        self.dado_pais.grid(row=4, column= 1)

        # Imagem

        # Contorna bug da falta de imagem:
        img = Image.open('./assets/placeholder.png')
        dado_img = ImageTk.PhotoImage(img)
        self.label_img = tk.Label(self, image=dado_img)
        self.label_img.image = dado_img

        self.label_img.grid(row=0, rowspan=5, column=2, sticky=tk.W)