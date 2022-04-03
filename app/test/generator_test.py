import pytest, os, uuid, docker
from src.generator import Generator


def test_generate_synthea_patient(mocker):
    # mocker.patch("os.system")
    # mocker.patch("os.mkdir")
    # mocker.patch("uuid.uuid4", return_value=1234567890)



    Generator.generate_synthea_patient()

    # os.system.assert_called_once_with("hello world")
