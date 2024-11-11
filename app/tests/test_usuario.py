import pytest

from app.models.usuario_model import Usuario

def test_usuario_nome_vazio_mensagem_erro():
    with pytest.raises(ValueError,match="O nome está vazio"):
        Usuario("","juliocesarbonfim@gmail.com","julio12345")

def test_usuario_nome_vazio_invalido_erro():
    with pytest.raises(TypeError,match="O nome está invalido"):
        Usuario(111,"juliocesarbonfim@gmail.com","julio12345")

def test_usuario_email_vazio_mensagem_erro():
    with pytest.raises(ValueError,match="O email está vazio"):
        Usuario("Julio Cesar de Jesus Bonfim","","julio12345")

def test_usuario_email_invalido_mensagem_erro():
    with pytest.raises(TypeError,match="O email está invalido"):
        Usuario("Julio Cesar de Jesus Bonfim",111,"julio12345")

def test_usuario_senha_vazia_mensagem_erro():
    with pytest.raises(ValueError,match="A senha está vazia"):
        Usuario("Julio Cesar de Jesus Bonfim","juliocesarbonfim@gmail.com","")

def test_usuario_senha_invalida_mensagem_erro():
    with pytest.raises(TypeError,match="A senha está inválida"):
        Usuario("Julio Cesar de Jesus Bonfim","juliocesarbonfim@gmail.com",111)