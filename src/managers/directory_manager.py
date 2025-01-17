import glob
import os
import shutil
import time
from typing import List



class DirectoryManager:
    """
    Classe que gerencia operações de manipulação de arquivos em um diretório.

    Esta classe permite a criação, busca, deleção, movimentação e
    monitoramento de arquivos em um diretório específico. Utiliza as
    bibliotecas padrão do Python para interagir com o sistema de arquivos
    e manipular arquivos de forma eficiente.

    Attributes:
        directory (str): Caminho completo do diretório base onde as operações
        com arquivos serão realizadas.
    """

    def __init__(self, directory: str):
        """
        Inicializa a classe com o diretório onde as operações 
        com arquivos serão realizadas.

        Args:
            directory (str): Caminho completo do diretório base.
        """
        self.directory = directory
        self._check_directory()


    def _create_directory(self):
        """
        Cria o diretório especificado na instância.
        
        Utiliza a função os.makedirs() para criar um novo diretório
        de forma recursiva caso ele não exista.
        """
        os.makedirs(self.directory, exist_ok=True)

    
    def _check_directory(self):
        """
        Verifica se o diretório existe, caso contrário, cria-o.

        Essa função é chamada no inicializador para garantir que o diretório
        esteja disponível antes de realizar qualquer operação de arquivo.
        """
        if not os.path.exists(self.directory):
            self._create_directory()

    
    def search_files(self, keyword: str) -> List[str]:
        """
        Procura por arquivos no diretório base.

        Se uma palavra-chave for fornecida, busca arquivos que contenham
        essa palavra no nome. Utiliza glob para realizar a busca.

        Args:
            keyword (str, optional): Palavra que será buscada no
            nome do arquivo. Padrão é None.

        Returns:
            list: Retorna uma lista com os nomes dos arquivos
            que contêm a palavra-chave encontrados no diretório.
        """
        pattern_for_search = f'*{keyword}*'
        file_paths = glob.glob(
            os.path.join(self.directory, pattern_for_search)
        )
        filenames = [os.path.basename(file) for file in file_paths]
        return filenames
    

    def get_file(self, keyword: str) -> str:
        """
        Retorna o caminho completo do primeiro arquivo que contém a
        palavra-chave.

        Args:
            keyword (str, optional): Palavra que será buscada no
            nome do arquivo. Padrão é None.

        Returns:
            str: Nome do caminho completo do arquivo caso encontrado.
            None se não tiver.
        """
        file = self.search_files(keyword)
        if not file:
            return None
        first_file = file[0]
        full_file_path = os.path.join(self.directory, first_file)
        return full_file_path
    

    def delete_file(self, path_or_file_name: str):
        """
        Deleta o arquivo especificado, caso o encontrar na pasta.

        Aceita tanto o caminho completo quanto apenas o nome do arquivo.
        Se for passado apenas o nome do arquivo, utiliza o
        diretório da instância.

        Args:
            path_or_file_name (str): Caminho completo ou só o nome
            do arquivo para deletar.
        """
        if not os.path.isabs(path_or_file_name):
            path_file = os.path.join(self.directory, path_or_file_name)
        else:
            path_file = path_or_file_name

        if os.path.exists(path_file):
            os.remove(path_file)
            

    def delete_files(self):
        """
        Deleta todos os arquivos do diretório instanciado.

        Utiliza glob para buscar todos os arquivos no diretório e
        os remove um a um.
        """
        file_names = glob.glob(os.path.join(self.directory, '*'))

        for file_name in file_names:
            if os.path.isfile(file_name):
                os.remove(file_name)
    

    def monitor_directory(
            self, 
            keyword: str = None, 
            timeout: int = 60, 
            interval: int = 5
        ) -> str:
        """
        Monitora o diretório por um tempo determinado, aguardando um arquivo
        ser encontrado.

        Se um arquivo que contenha a palavra-chave for encontrado,
        retorna o caminho completo. Verifica a pasta a cada intervalo
        de segundos.

        Args:
            keyword (str, optional): Palavra-chave que o robô irá
            procurar no nome dos arquivos no diretório definido.
            timeout (int, optional): Tempo em segundos limite de monitoração
            da pasta.
            interval (int, optional): Intervalo em segundos a cada iteração
            do loop.

        Returns:
            str: Nome do caminho completo do arquivo caso encontrado.
            None se não tiver.
        """
        initial_time = time.time()

        while time.time() - initial_time < timeout:
            file_names = self.search_files(keyword)

            if file_names:
                file_name = file_names[0]
                return file_name
            
            time.sleep(interval)
        return None
    

    def move_file(self, file_origin: str, file_destination: str) -> str:
        """
        Move um arquivo de um local de origem para um destino.

        Cria o diretório de destino caso não exista e move o arquivo
        utilizando shutil.move().

        Args:
            file_origin (str): Caminho do arquivo que será movido.
            file_destination (str): Caminho do diretório de destino.

        Returns:
            str: Mensagem de sucesso ou erro ao mover o arquivo.
        """
        try:
            os.makedirs(file_destination, exist_ok=True)

            file_name = os.path.basename(file_origin)
            destination = os.path.join(file_destination, file_name)
            shutil.move(file_origin, destination)
            return (
                f"Arquivo '{file_origin}' movido para '{destination}' com sucesso!"
            )
        except FileNotFoundError:
            return (f"Arquivo '{file_origin}' não encontrado.")
        except Exception as e:
            return (f"Erro ao mover o arquivo: {e}")