import pytest, os, uuid, docker, json
from src.generator import Generator
from unittest.mock import patch, Mock

def test_generate_synthea_patient(mocker):
    client_mock = Mock()
    containers_mock = Mock()
    client_mock.containers = containers_mock
    containers_mock.get = lambda x: containers_mock
    mocker.patch("docker.from_env", return_value = client_mock)
    containers_mock.attrs = {
        'NetworkSettings': {
            'Networks': {
                'syntheticdatagenerator_default': {
                    'IPAddress': {
                        '123.anything'
                    }
                }
            }
        }
    }

    Generator.generate_synthea_patient()

    containers_mock.run.assert_called_once()

def test_filter_synthea_response():
    input = json.load(open('app/test/patient-synthea-example.json'))
    filtered_patients = Generator.filter_synthea_response(input)
    assert len(filtered_patients) == 1
    assert "text" not in filtered_patients[0]["resource"]