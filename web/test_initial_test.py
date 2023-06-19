import pytest
import web

def test_soma_file():
    assert 1 == 1

def test_route_default():
    data = web.index()
    assert data == "Hello, World! -- TURMA DA CESAR SCHOOL"
