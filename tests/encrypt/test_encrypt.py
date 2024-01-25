from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "teste2")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(["teste4", "teste5"], 4)
    assert encrypt_message("batuta", 3) == "tab_atu"
    assert encrypt_message("batuta", 4) == "at_utab"
    assert encrypt_message("batuta", 9) == "atutab"
