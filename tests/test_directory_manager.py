import os


def test_create_directory(directory_manager):
    """Testa se o diretório é criado corretamente."""
    assert os.path.exists(directory_manager.directory)


def test_search_files(directory_manager):
    """Testa a busca por arquivos."""
    test_file = directory_manager.directory + "/test_file.txt"
    with open(test_file, 'w') as f:
        f.write("Hello, World!")
    
    found_files = directory_manager.search_files("test_file")
    assert "test_file.txt" in found_files

def test_get_file(directory_manager):
    """Testa a obtenção do caminho do primeiro arquivo encontrado."""
    test_file = directory_manager.directory + "/test_file.txt"
    with open(test_file, 'w') as f:
        f.write("Hello, World!")
    
    file_path = directory_manager.get_file("test_file")
    assert file_path == test_file

def test_get_file_return_none(directory_manager):
    file_path = directory_manager.get_file('test_file')
    assert file_path == None


def test_delete_file(directory_manager):
    """Testa a deleção de um arquivo."""
    test_file = directory_manager.directory + "/test_file.txt"
    with open(test_file, 'w') as f:
        f.write("Hello, World!")

    directory_manager.delete_file("test_file.txt")
    assert not os.path.exists(test_file)

def test_delete_files(directory_manager):
    """Testa a deleção de todos os arquivos no diretório."""
    with open(directory_manager.directory + "/file1.txt", 'w') as f:
        f.write("File 1")
    with open(directory_manager.directory + "/file2.txt", 'w') as f:
        f.write("File 2")

    directory_manager.delete_files()
    assert len(os.listdir(directory_manager.directory)) == 0

def test_move_file(directory_manager):
    """Testa a movimentação de um arquivo."""
    source_file = directory_manager.directory + "/source.txt"
    destination_directory = directory_manager.directory + "/destination"

    with open(source_file, 'w') as f:
        f.write("Movable File")

    result = directory_manager.move_file(source_file, destination_directory)
    assert os.path.exists(os.path.join(destination_directory, "source.txt"))
    assert not os.path.exists(source_file)
    assert "movido" in result



def test_monitor_directory_returns_none(directory_manager):
    keyword = "temp_file.txt"
    timeout = 5
    interval = 1
    found_file = directory_manager.monitor_directory(keyword, timeout, interval)
    assert found_file == None



