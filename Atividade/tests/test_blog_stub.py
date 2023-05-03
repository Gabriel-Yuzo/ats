import pytest




from tests.test_blog import BlogRepositorioStub, ExcecaoBlogNaoEncontrado
from tests.blogRepositorioMock import BlogRepositorioMock



@pytest.fixture
def servico():
    blogRep = BlogRepositorioStub()
    blogMock = BlogRepositorioMock(blogRep)
    return blogMock


def test_busca_lista(servico):
    b1 = servico.buscar_todos()
    assert list == b1

def test_busca_por_id_deve_devolver_blog_com_id_111(servico):
    b1 = servico.obter_por_id(1)
    assert b1.id == 2

def test_busca_por_id_deve_devolver_blog_com_id_222(servico):
    b1 = servico.obter_por_id(2)
    assert b1.id == 2


def test_busca_por_id_333_deve_devolver_excecao(servico):
    with pytest.raises(ExcecaoBlogNaoEncontrado):
        b1 = servico.obter_por_id(80)