import os
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import tkintermapview as tkmv
import customtkinter as ctk


class MapaController:
    def __init__(self):
        self.bd_imagens = None
        self.view = None
        self.root = ctk.CTk()

    def inicializa(self, model, view):
        '''
        Método faz parte da interface pública: atribui view e model
        e em seguida, configura o controlador com o view e model.
        '''
        self.bd_imagens = model
        self.view = view
        self._configura()

    def _configura(self):
        self.processa_imagens()
        self.view.frame_busca.button_buscar.configure(
            command=self.busca_botao)
        self.view.frame_busca.button_redefinir.configure(
            command=self.redefinir_busca)
    def executa(self):
        '''Método principal da interface pública da classe.'''
        self.root.mainloop()

    def busca_botao(self):
        opcao_selecionada = self.view.frame_busca.combobox_busca.get()
        valor_input1 = self.view.frame_busca.input_1.get()
        valor_input2 = self.view.frame_busca.input_2.get()

        if opcao_selecionada == 'Selecione':
            messagebox.showerror('Erro', 'Selecione uma opção válida antes de buscar.')

        elif valor_input1 == "" or (opcao_selecionada == 'Data' and valor_input2 == ""):
            messagebox.showerror('Erro', 'informe um valor')
        
        else:
            if opcao_selecionada == 'Data':
                self.busca_por_data(valor_input1, valor_input2)

            elif opcao_selecionada == 'Nome':
                self.busca_por_nome(valor_input1)

            elif opcao_selecionada == 'Cidade':
                self.busca_por_cidade(valor_input1)

            elif opcao_selecionada == 'País':
                self.busca_por_pais(valor_input1)

    def adicionar_marcador(self, latitude, longitude, image_path, data):
        img = Image.open(image_path)
        img_resized = img.resize(size=(50, 50))
        image = ImageTk.PhotoImage(img_resized.resize(size=(50, 50)))

        nome_marcador = self.view.map.set_marker(latitude, longitude, image=image, command= self.clica_marcador,data = data)

    
    def clica_marcador(self,event):
        img = Image.open(event.data.nome())
        dado_img = ctk.CTkImage(light_image=img, size=(150, 150))
        marcador = event.data
        self.view.frame_dados.var_nome.set(os.path.basename(event.data.nome()))
        self.view.frame_dados.label_img = ctk.CTkLabel(
            self.view.frame_dados, image=dado_img, text="")
        self.view.frame_dados.label_img.image = dado_img
        self.view.frame_dados.label_img.grid(
            row=0, rowspan=6, column=2, sticky=tk.W)

        latitude = marcador.latitude
        longitude = marcador.longitude
        self.view.frame_dados.var_lat.set(latitude)
        self.view.frame_dados.var_longitude.set(longitude)

        data = marcador.data
        if data:
            self.view.frame_dados.var_data.set(data)
        else:
            self.view.frame_dados.var_data.set("N/A")

        pais = tkmv.convert_coordinates_to_country(latitude, longitude)
        cidade = tkmv.convert_coordinates_to_city(latitude, longitude)
        self.view.frame_dados.var_pais.set(pais)
        self.view.frame_dados.var_cidade.set(cidade)

    def processa_imagens(self):
        self.bd_imagens.processa()

        for imagem in self.bd_imagens.todas():
            self.adicionar_marcador(imagem.latitude, imagem.longitude, imagem.nome(), imagem)
        
    def busca_por_nome(self, nome):
        imagens = self.bd_imagens.busca_por_nome(nome)

        self.limpar_marcadores()
        for imagem in imagens:
            self.adicionar_marcador(imagem.latitude, imagem.longitude, imagem.nome(), imagem)

    def busca_por_data(self, dini: datetime, dfim: datetime):
        imagens = self.bd_imagens.busca_por_data(dini, dfim)

        self.limpar_marcadores()
        for imagem in imagens:
            self.adicionar_marcador(imagem.latitude, imagem.longitude, imagem.nome(), imagem)

    def busca_por_cidade(self, cidade):
        imagens = [img for img in self.bd_imagens.todas() if img.cidade != None and img.cidade.lower() == cidade.lower()]

        self.limpar_marcadores()
        for imagem in imagens:
            self.adicionar_marcador(imagem.latitude, imagem.longitude, imagem.nome(), imagem)

    def busca_por_pais(self, pais):
 
        imagens = [img for img in self.bd_imagens.todas() if img.pais != None  and img.pais.lower() == pais.lower()]

        self.limpar_marcadores()
        for imagem in imagens:
            self.adicionar_marcador(imagem.latitude, imagem.longitude, imagem.nome(), imagem)

    def redefinir_busca(self):
        self.limpar_marcadores()
        self.processa_imagens()


    def limpar_marcadores(self):
        self.view.map.delete_all_marker()