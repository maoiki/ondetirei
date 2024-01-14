import tkinter as tk
import customtkinter as ctk
import tkintermapview as tkmv

from widgets import FrameBusca, FrameDados

class MapaView:
    def __init__(self, root):
        self.root = root 

        self._inicializa_gui()
    
    def _inicializa_gui(self):
        self.root.geometry('900x600')
        self.root.minsize(900,600)
        self.root.title('Onde tirei?')

        ctk.set_default_color_theme("green")

        self.map = tkmv.TkinterMapView(self.root, corner_radius=0)
        self.map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map.set_address('Rio Grande do Norte, Brasil')
        self.map.set_zoom(15)

        self.map.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.frame_right = ctk.CTkFrame(self.root)
        self.frame_right.pack(expand=True, fill=tk.BOTH)

        self.frame_busca = FrameBusca(self.frame_right)
        self.frame_dados = FrameDados(self.frame_right)
