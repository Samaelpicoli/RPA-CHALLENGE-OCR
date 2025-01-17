import shutil

import pytest
import requests

from src.managers.directory_manager import DirectoryManager
from src.managers.requests_manager import RequestManager


@pytest.fixture
def request_manager():
    """Fixture para criar uma instância do RequestManager."""
    return RequestManager()

@pytest.fixture
def mock_response_img():
    """Fixture para criar uma resposta mockada."""
    mock_response = requests.Response()
    mock_response._content = b'Test image content'
    mock_response.status_code = 200
    return mock_response


@pytest.fixture
def directory_manager(tmp_path):
    """Fixture para criar um DirectoryManager com um diretório temporário."""
    test_directory = tmp_path / "test_directory"
    manager = DirectoryManager(str(test_directory))
    yield manager
    shutil.rmtree(test_directory, ignore_errors=True)