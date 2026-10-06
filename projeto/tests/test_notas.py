import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from notas import situacao_aluno


def test_aprovado():
    assert situacao_aluno([8, 9, 10]) == "Aprovado"


def test_aprovado_com_media_exatamente_7():
    assert situacao_aluno([7, 7, 7]) == "Aprovado"


def test_recuperacao():
    assert situacao_aluno([6, 5, 7]) == "Recuperação"


def test_recuperacao_com_media_exatamente_5():
    assert situacao_aluno([5, 5]) == "Recuperação"


def test_reprovado():
    assert situacao_aluno([2, 3, 4]) == "Reprovado"


def test_uma_nota_so():
    assert situacao_aluno([10]) == "Aprovado"


def test_lista_vazia():
    with pytest.raises(ValueError):
        situacao_aluno([])


def test_nota_invalida():
    with pytest.raises(ValueError):
        situacao_aluno([8, 11, 9])


def test_nota_negativa():
    with pytest.raises(ValueError):
        situacao_aluno([5, -1])
