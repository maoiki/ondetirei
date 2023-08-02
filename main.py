from mapa_controller import MapaController
from mapa_view import MapaView
from bd_imagens import BDImagens

def main():
    controller = MapaController()
    caminho_dataset = "./dataset1/dataset1/"
    model = BDImagens(caminho_dataset)
    view = MapaView(controller.root)

    controller.inicializa(model, view)
    controller.executa()

if __name__ == "__main__":
    main()
    