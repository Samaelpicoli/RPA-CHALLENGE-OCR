from datetime import datetime
import os

import logging


class Logger:

    def __init__(self, directory_log=os.getcwd(), level_log=logging.INFO):
        """
        Inicializador da classe de Log.

        Args:
            _directory_log (str): Caminho onde será criado a pasta de logs.
            Por padrão será salvo na pasta do projeto.
            _level_log (Logging): Nível de log padrão. Será INFO.
        """
        self._date = datetime.now().strftime('%d-%m-%Y')
        self._directory_log = directory_log
        self._level_log = level_log
        self.logger = logging.getLogger('AppLogger')
        self._log_initializer()


    def _log_initializer(self):
        """
        Inicializa o logger configurando o arquivo de log e os handlers.
        Verifica se o logger já possui handlers(manipuladores), caso não,
        chama os métodos para obter o nome do arquivo de log e configurar
        os handlers para o arquivo.
        """
        file_log = self._get_log_file()
        if not self.logger.hasHandlers():
            self._configure_handlers(file_log)


    def _makedir_directory_log(self) -> str:
        """
        Cria o diretório onde serão armazenados os logs, o diretório será
        criado com base no atributo caminho que foi passado na instância
        da classe e dentro dele, será criado um novo diretório com o nome 'LOGS".

        Returns:
            str: caminho do diretório onde foi criado a pasta de LOGS.
        """
        dir_log = os.path.join(self._directory_log, 'LOGS')
        os.makedirs(dir_log, exist_ok=True)
        return dir_log
    

    def _get_log_file(self) -> str:
        """
        Define o nome do arquivo, será a data atual.txt.

        Returns:
            str: nome do arquivo de log para ser escrito.
        """
        path_name = self._makedir_directory_log()
        file_name = os.path.join(path_name, self._date + '.txt')
        return file_name
    

    def _configure_handlers(self, file_log: str):
        """
        Configura o logger para gravar logs em um arquivo e define o 
        formato do log. 
        Define um FileHandler para o arquivo de log e aplica o formato das
        mensagens, que inclui a data, nível e mensagem de log. Também define o
        nível de log para o handler.

        Args:
            file_log (str): o nome do arquivo de log.
        """
        format_log = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )
    
        file = logging.FileHandler(file_log, mode='a')
        file.setLevel(self._level_log)
        file.setFormatter(format_log)
        self.logger.addHandler(file)
        self.logger.setLevel(self._level_log)


    def info(self, message: str):
        """
        Escreve uma mensagem de nível info no arquivo de log.

        Args:
            message (str): Mensagem a ser escrita no arquivo.
        """
        self.logger.info(message)
    

    def alert(self, message: str):
        """
        Escreve uma mensagem de nível warning no arquivo de log.

        Args:
            message (str): Mensagem a ser escrita no arquivo.
        """
        self.logger.warning(message)
    

    def error(self, message: str):
        """
        Escreve uma mensagem de nível erro no arquivo de log.

        Args:
            message (str): Mensagem a ser escrita no arquivo.
        """
        self.logger.error(message)