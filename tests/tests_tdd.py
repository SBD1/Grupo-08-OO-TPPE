import pytest
from src.models.veiculo import Veiculo

@pytest.mark.skip(reason="TDD - Teste a ser implementado após desenvolvimento do módulo")
def test_criar_veiculo_tdd():
    """
    Teste TDD para criação de veículo (ignorado temporariamente)
    """
    # Este é um teste que será implementado depois
    veiculo = Veiculo(
        id=1,
        modelo="Gol",
        marca="Volkswagen",
        placa="ABC1234",
        ano=2022,
        disponivel=True
    )
    
    assert veiculo.id == 1
    assert veiculo.modelo == "Gol"
    assert veiculo.disponivel is True