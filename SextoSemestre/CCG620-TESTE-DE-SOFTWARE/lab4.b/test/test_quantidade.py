from src import validar_quantidade

 
def test_validar_quantidade_limite_inferior():
    assert validar_quantidade(-1) == False
    assert validar_quantidade(0) == True
 
 
def test_validar_quantidade_limite_superior():
    assert validar_quantidade(1001) == False
    assert validar_quantidade(1000) == True
