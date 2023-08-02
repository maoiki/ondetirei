
'''
Módulo imagem.

Contém classes para manipular
imagens georreferenciadas (com informação de GPS)

Authors:Caio Murilo
        Julio Duarte
'''

from datetime import datetime
from typing import Tuple
from PIL.ExifTags import TAGS, GPSTAGS
import tkintermapview as tkmv
from PIL import Image

def converte_graus_para_decimais(tup: Tuple[int, int, int], ref: str) -> float:
    '''
    Função utilitária: converte coordenadas de
    graus, minutos e segundos (tupla) para
    decimais (float).
    '''

    if ref is None or ref.strip() == "" or len(tup) < 3:
        raise ValueError(f"Referência inválida: {ref}")

    s = -1 if ref.upper() in ["S", "W"] else 1

    return s * (tup[0] + tup[1] / 60.0 + tup[2] / 3600.0)

class Imagem:
    '''
    Representa uma imagem
    (classe principal do programa).
    '''

    def __init__(self, nome: str):
        '''
        Inicializa um objeto imagem
        a partir do nome do seu arquivo.
        '''

        self._nome = nome
        self._data = None
        self._lat = None
        self._lon = None
        self._pais = None
        self._cidade = None
        self._processa_EXIF()

    def __repr__(self) -> str:
        '''
        Retorna representação de uma imagem
        em forma de str
        '''
        return self._nome

    def _processa_EXIF(self) -> None:
        '''
        Processa metadados EXIF contidos no arquivo da imagem
        para extrair informações de data e local de captura.

        Atribui valores aos atributos de instância correspondentes
        à latitude, longitude, país, cidade e data de captura.
        '''
        self._img = Image.open(self._nome)
        exif_data = self._img._getexif()

        if exif_data is None:
            return

        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag)
            if tag_name == 'GPSInfo':
                for gps_cod, gps_dado in value.items():
                    if GPSTAGS[gps_cod] == 'GPSLatitude':
                        tup_lat = gps_dado
                    if GPSTAGS[gps_cod] == 'GPSLongitude':
                        tup_lon = gps_dado
                    if GPSTAGS[gps_cod] == 'GPSLatitudeRef':
                        ref_lat = gps_dado
                    if GPSTAGS[gps_cod] == 'GPSLongitudeRef':
                        ref_lon = gps_dado

                self._lat = converte_graus_para_decimais(tup_lat, ref_lat)
                self._lon = converte_graus_para_decimais(tup_lon, ref_lon)

            if tag_name == 'DateTime':
                self._data = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')

        if self._lat is not None and self._lon is not None:
            self._pais = tkmv.convert_coordinates_to_country(self._lat, self._lon)
            self._cidade = tkmv.convert_coordinates_to_city(self._lat, self._lon)

    def nome(self) -> str:
        '''
        Retorna o nome do arquivo
        da imagem
        '''
        return self._nome

    @property
    def largura(self) -> int:
        '''
        Retorna a largura da imagem
        '''
        with Image.open(self._nome) as img:
            return img.width

    @property
    def altura(self) -> int:
        '''
        Retorna a altura da imagem
        '''
        with Image.open(self._nome) as img:
            return img.height

    @property
    def tamanho(self) -> Tuple[int, int]:
        '''
        Retorna o tamanho da imagem
        (tupla largura x altura)
        '''
        with Image.open(self._nome) as img:
            return img.size

    @property
    def data(self) -> datetime:
        '''
        Retorna a data em que a imagem
        foi capturada (objeto da classe datetime)
        '''
        return self._data

    @property
    def latitude(self) -> float:
        '''
        Retorna a latitude (em decimais)
        em que a imagem foi capturada
        '''
        return self._lat

    @property
    def longitude(self) -> float:
        '''
        Retorna a longitude (em decimais)
        em que a imagem foi capturada
        '''
        return self._lon

    @property
    def pais(self) -> str:
        '''
        Retorna o país em que a imagem
        foi capturada
        '''
        return self._pais

    @property
    def cidade(self) -> str:
        '''
        Retorna a cidade em que a imagem
        foi capturada
        '''
        return self._cidade

    def imprime_info(self) -> None:
        '''
        Imprime informações sobre
        a imagem
        '''
        print(f"Nome: {self._nome}")
        print(f"Largura: {self.largura}")
        print(f"Altura: {self.altura}")
        print(f"Tamanho: {self.tamanho}")
        print(f"Data: {self.data}")
        print(f"Latitude: {self.latitude}")
        print(f"Longitude: {self.longitude}")
        print(f"País: {self.pais}")
        print(f"Cidade: {self.cidade}")