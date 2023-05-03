from src.blogsRepositorio import BlogRepositorio


class ExcecaoBlogNaoEncontrado(Exception):
    pass


class BlogRepositorioMock(BlogRepositorio):
    def __init__(self):
        self.livros = []

    def obter_blogs(self) -> list:
        return list(self.livros)
    


