import pytest
import web

def test_soma_file():
    data = "leo"
    assert "leo" == data

def test_route_default():
    data = web.index()
    assert data == "Hello, World! -- TURMA DA CESAR SCHOOL"
