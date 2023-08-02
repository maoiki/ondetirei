import tkinter as tk
import tkintermapview as tkmv

from widgets import FrameBusca, FrameDados

class MapaView:
    def __init__(self, root):
        self.root = root 

        self._inicializa_gui()
    
    def _inicializa_gui(self):
        self.root.geometry('800x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Projeto final')

        self.map = tkmv.TkinterMapView(self.root, width=400, height=600)
        self.map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map.set_address('ECT UFRN') # centraliza mapa na ECT/UFRN
        self.map.set_zoom(15)

        self.map.pack(side=tk.LEFT)

        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(expand=True, fill=tk.BOTH)

        self.frame_busca = FrameBusca(self.frame_right)
        self.frame_dados = FrameDados(self.frame_right)
