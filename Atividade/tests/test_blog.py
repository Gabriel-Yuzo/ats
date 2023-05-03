
from src.blogsRepositorio import BlogRepositorio
from src.blogs import Blog


class ExcecaoBlogNaoEncontrado(Exception):
    pass


class BlogRepositorioStub(BlogRepositorio):
    def __init__(self):
        self.blogs = []
    
    def buscar_todos(self) -> list:
        return list(self.blogs)
    

    def obter_por_id(self, id: int) -> Blog:
        for blog in self.blogs:
            if blog.id == id:
                return blog
            raise ExcecaoBlogNaoEncontrado