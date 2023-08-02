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

        self.view.frame_busca.button_buscar['command'] = lambda: self.busca_botao()
        self.view.frame_busca.button_redefinir['command'] = lambda: self.redefinir_busca()

    def executa(self):
        '''Método principal da interface pública da classe.'''
        self.root.mainloop()

    def busca_botao(self):
        children_widgets = self.view.frame_busca.winfo_children()
        input_values = []

        if self.view.frame_busca.combobox_busca.get() == 'Selecione um valor':
            messagebox.showerror('Erro', 'Selecione uma opção válida antes de buscar.')


        # procura os inputs filhos do frame_busca dinamicamente
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry' and child_widget.winfo_ismapped():
                if child_widget.get() == "": 
                    messagebox.showerror('Erro', 'informe um valor')
                else: 
                    input_values.append(child_widget.get())


        if self.view.frame_busca.combobox_busca.get() == 'Data':
            self.busca_por_data(input_values[0], input_values[1])

        elif self.view.frame_busca.combobox_busca.get() == 'Nome':
            self.busca_por_nome(input_values[0])

        elif self.view.frame_busca.combobox_busca.get() == 'Cidade':
            self.busca_por_cidade(input_values[0])

        elif self.view.frame_busca.combobox_busca.get() == 'País':
            self.busca_por_pais(input_values[0])

    def adicionar_marcador(self, latitude, longitude, image_path, data):
        img = Image.open(image_path)
        img_resized = img.resize(size=(50, 50))
        image = ImageTk.PhotoImage(img_resized.resize(size=(50, 50)))

        nome_marcador = self.view.map.set_marker(latitude, longitude, image=image, command= self.clica_marcador,data = data)

    
    def clica_marcador(self,event):
      dado_img = ImageTk.PhotoImage(Image.open(event.data.nome()).resize(size=(150, 150)))
      marcador = event.data
      self.view.frame_dados.var_nome.set(os.path.basename(event.data.nome()))
      self.view.frame_dados.label_img = tk.Label(self.view.frame_dados, image=dado_img)
      self.view.frame_dados.label_img.image = dado_img
      self.view.frame_dados.label_img.grid(row=0, rowspan=5, column=2, sticky=tk.W)

      latitude = marcador.latitude
      longitude = marcador.longitude
      self.view.frame_dados.var_coords.set(f"{latitude} {longitude}")

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