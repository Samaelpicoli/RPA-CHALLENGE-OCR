import os
import requests


class RequestManager:
    """
    Classe que gerencia requisições HTTP utilizando a biblioteca requests.

    Essa classe permite realizar requisições GET para URLs, facilitando o
    scraping de dados e a conversão de respostas em arquivos, como CSV.
    
    Utiliza sessões para otimizar múltiplas requisições.

    Attributes:
        session (requests.Session): A sessão HTTP que mantém conexões
        persistentes.
    """

    def __init__(self):
        """
        Inicializa a classe RequestManager.

        Cria uma nova sessão requests para gerenciar as requisições HTTP.
        """
        self.session = requests.Session()

    
    def get(self, url: str) -> requests.Response:
        """
        Realiza uma requisição GET para a URL especificada.

        Args:
            url (str): A URL para a qual a requisição será feita.

        Returns:
            requests.Response: A resposta da requisição.

        Raises:
            Exception: Se a resposta não for bem-sucedida
            (código de status diferente de 200).
        """
        response = self.session.get(url)
        if response.status_code == 200:
            return response
        raise Exception(f'Erro: {response.status_code}')


    def convert_response_to_file_img(
            self, response: requests.Response, directory: str, file_name: str
        ) -> str:
        """
        Converte a resposta de uma requisição em um arquivo de imagem.

        Args:
            response (requests.Response): A resposta da requisição que contém
            os dados da imagem.
            directory (str): O diretório onde o arquivo será salvo.
            file_name (str): O nome do arquivo a ser criado.

        Returns:
            str: O caminho completo do arquivo salvo.
        """
        file_path = os.path.join(directory, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_path