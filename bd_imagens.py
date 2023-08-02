from datetime import datetime
from typing import List
import os

from imagem import Imagem

class BDImagens:
    '''
    Representa um banco de dados de
    imagens geoespaciais
    (classe de busca do programa)
    '''

    def __init__(self, caminho: str):
        self._imagens = []
        self._caminho = caminho

    def processa(self) -> None:
        '''
        Abre cada imagem no diretório
        especificado pelo caminho e adiciona
        cada imagem à lista.
        '''
        for arquivo in os.listdir(self._caminho):
            if arquivo.endswith(".jpg"):
                caminho_arquivo = os.path.join(self._caminho, arquivo)
                imagem = Imagem(caminho_arquivo)
                self._imagens.append(imagem)

    @property
    def tamanho(self) -> int:
        '''
        Retorna a quantidade de imagens
        no banco de dados.
        '''
        return len(self._imagens)

    def todas(self) -> List[Imagem]:
        '''
        Retorna uma lista contendo
        todas as imagens abertas
        no banco de dados.
        '''
        return self._imagens

    def busca_por_nome(self, texto: str) -> List[Imagem]:
        '''
        Retorna uma lista contendo
        todas as imagens do banco de dados
        cujo nome contenha o texto passado
        como parâmetro.
        '''
        resultado = []
        for imagem in self._imagens:
            if texto.lower() in imagem.nome().lower():
                resultado.append(imagem)
        return resultado

    def busca_por_data(self, dini: datetime, dfim: datetime) -> List[Imagem]:
        '''
        Retorna uma lista contendo
        todas as imagens do banco de dados
        cuja data de captura encontra-se entre
        dini (data inicial) e dfim (data final).
        '''
        resultado = []
        for imagem in self._imagens:
            if imagem.data is not None and dini <= imagem.data <= dfim:
                resultado.append(imagem)
        return resultado