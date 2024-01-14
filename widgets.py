import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


class FrameBusca(ctk.CTkFrame):
    '''
    Frame onde são colocados os dados para realizar buscas
    '''

    def __init__(self, container):
        super().__init__(container)
        self.configure(width=400)
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
        self.label_datainicial = ctk.CTkLabel(self, text='Data inicial:')
        self.input_datainicial = ctk.CTkEntry(self)

        self.label_datafinal = ctk.CTkLabel(self, text='Data final:')
        self.input_datafinal = ctk.CTkEntry(self)

        self.label_nome = ctk.CTkLabel(self, text='Nome:')
        self.input_nome = ctk.CTkEntry(self)

        self.label_cidade = ctk.CTkLabel(self, text='Cidade:')
        self.input_cidade = ctk.CTkEntry(self)

        self.label_pais = ctk.CTkLabel(self, text='País:')
        self.input_pais = ctk.CTkEntry(self)

        # Cria combobox que altera quais inputs aparecem
        self.combobox_label = ctk.CTkLabel(self, text='Buscar por:')
        combobox_busca_values = ['Selecione um valor',
                                 'Data', 'Nome', 'Cidade', 'País']
        self.combobox_busca = ctk.CTkComboBox(self, values=combobox_busca_values, command=self.altera_entries)

        self.combobox_label.grid(row=0, column=0)
        self.combobox_busca.grid(row=0, column=1)

        self.button_buscar = ctk.CTkButton(self, text='Buscar')
        self.button_redefinir = ctk.CTkButton(self, text='Redefinir')

        self.button_buscar.grid(row=2, column=0),
        self.button_redefinir.grid(row=2, column=1)


class FrameDados(ctk.CTkFrame):
    '''
    Frame onde são mostrados os dados da foto selecionada
    '''

    def __init__(self, container):
        super().__init__(container)

        self.configure(width=400)
        self.pack(side=tk.BOTTOM, fill=tk.X)
        self.columnconfigure(2, minsize=150)
        self.columnconfigure(1, minsize=100, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        # Dados da imagem
        self.var_nome = tk.StringVar()
        self.label_nome = ctk.CTkLabel(self, text='Nome:')
        self.dado_nome = ctk.CTkLabel(self, textvariable=self.var_nome)

        self.var_data = tk.StringVar()
        self.label_data = ctk.CTkLabel(self, text='Data:')
        self.dado_data = ctk.CTkLabel(self, textvariable=self.var_data)

        self.var_lat = tk.StringVar()
        self.label_lat = ctk.CTkLabel(self, text='Latitude:')
        self.dado_lat = ctk.CTkLabel(self, textvariable=self.var_lat)

        self.var_longitude = tk.StringVar()
        self.label_longitude = ctk.CTkLabel(self, text='Longitude:')
        self.dado_longitude = ctk.CTkLabel(self, textvariable=self.var_longitude)

        self.var_cidade = tk.StringVar()
        self.label_cidade = ctk.CTkLabel(self, text='Cidade:')
        self.dado_cidade = ctk.CTkLabel(self, textvariable=self.var_cidade)

        self.var_pais = tk.StringVar()
        self.label_pais = ctk.CTkLabel(self, text='País:')
        self.dado_pais = ctk.CTkLabel(self, textvariable=self.var_pais)

        self.label_nome.grid(row=0, column=0, sticky=tk.W)
        self.dado_nome.grid(row=0, column=1)

        self.label_data.grid(row=1, column=0, sticky=tk.W)
        self.dado_data.grid(row=1, column=1)

        self.label_lat.grid(row=2, column=0, sticky=tk.W)
        self.dado_lat.grid(row=2, column=1)

        self.label_longitude.grid(row=3, column=0, sticky=tk.W)
        self.dado_longitude.grid(row=3, column=1)

        self.label_cidade.grid(row=4, column=0, sticky=tk.W)
        self.dado_cidade.grid(row=4, column=1)

        self.label_pais.grid(row=5, column=0, sticky=tk.W)
        self.dado_pais.grid(row=5, column=1)

        # Imagem

        # Contorna bug da falta de imagem:
        img = Image.open('./assets/placeholder.png')
        # dado_img = ImageTk.PhotoImage(img)
        dado_img = ctk.CTkImage(light_image=img, size=(150, 150))
        self.label_img = ctk.CTkLabel(self, image=dado_img, text='')
        self.label_img.image = dado_img

        self.label_img.grid(row=0, rowspan=6, column=2, sticky=tk.W)
