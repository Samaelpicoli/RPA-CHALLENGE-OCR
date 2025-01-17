from unittest.mock import mock_open, patch

import pytest
import requests

from config import *



def test_request_site_returns_200(request_manager):
    esperado = 200
    response = request_manager.get(URL_SITE)
    assert response.status_code == esperado

def test_request_manager_get_returns_response_type(request_manager):
    response = request_manager.get(URL_SITE)
    assert isinstance(response, requests.Response)

def test_request_manager_not_returns_200(request_manager):
    esperado = 'Erro: 404'
    with pytest.raises(Exception) as exc_info:
        request_manager.get(f'{URL_SITE}/teste')
    
    assert str(exc_info.value) == esperado

def test_convert_response_to_file_img(request_manager, mock_response_img):
    directory = 'test_directory'
    file_name = 'test_image.png'

    with patch('builtins.open', mock_open()) as mocked_file, \
         patch('os.path.join', return_value=f'{directory}/{file_name}'):
        file_path = request_manager.convert_response_to_file_img(
            mock_response_img, directory, file_name
        )
        expected_file_path = os.path.join(directory, file_name)
        assert file_path == expected_file_path

