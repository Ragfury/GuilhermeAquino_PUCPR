from funcoes import *

# Teste 1: Manipulação de Strings
def test_inversao_texto():
    assert inverter_string("github") == "buhtig"
    assert inverter_string("ana") == "ana"

# Teste 2: Operações com Listas
def test_processamento_lista():
    entrada = [1, 2, 3]
    esperado = [2, 4, 6]
    assert listar_dobro(entrada) == esperado

# Teste 3: Validação Booleana
def test_logica_par():
    assert verificar_par(10) is True
    assert verificar_par(7) is False

# Teste 4: Formatação de Texto (Concatenação)
def test_criacao_email():
    assert formatar_email("guilherme") == "guilherme@pucpr.edu.br"

# Teste 5: Verificação de Conteúdo (In)
def test_pertencimento_lista():
    frutas = ["maçã", "banana", "uva"]
    assert "banana" in frutas
    assert "morango" not in frutas