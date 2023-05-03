from abc import ABCMeta, abstractmethod
from src.blogs import Blog

class BlogRepositorio(metaclass= ABCMeta):
    @abstractmethod
    def obter_lista_blog(self) -> list:
        pass


    @abstractmethod
    def obter_por_id(self, id: int) -> Blog:
        pass