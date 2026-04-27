from funcoes import *

def test_inversao_texto():
    assert inverter_string("github") == "buhtig"
    assert inverter_string("ana") == "ana"

def test_processamento_lista():
    entrada = [1, 2, 3]
    esperado = [2, 4, 6]
    assert listar_dobro(entrada) == esperado

def test_logica_par():
    assert verificar_par(10) is True
    assert verificar_par(7) is False

def test_criacao_email():
    assert formatar_email("guilherme") == "guilherme@pucpr.edu.br"

def test_pertencimento_lista():
    frutas = ["maçã", "banana", "uva"]
    assert "banana" in frutas
    assert "morango" not in frutas