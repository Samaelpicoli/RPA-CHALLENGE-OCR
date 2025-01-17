from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from src.managers.web_driver_options import WebDriverOptions



class WebDriverController:
    """
    Controla a instância do driver do Selenium WebDriver.

    Implementa o padrão de design Singleton para garantir que apenas uma
    instância do WebDriver seja criada e reutilizada em toda a aplicação.

    Attributes:
        _instancia_driver (WebDriver): A instância do driver do WebDriver.
    """
    _instancia_driver = None


    def __init__(self):
        """
        Inicializa a classe WebDriverController.

        Se 'WebDriverController._instancia_driver' for None, configura
        o driver do Selenium WebDriver. Caso contrário, reutiliza a instância
        existente do driver.

        Para configurar o driver, a classe utiliza composição com a classe
        WebDriverOptions para obter as opções do WebDriver.
        """
        if WebDriverController._instancia_driver is None:
            options = WebDriverOptions().get_options()
            WebDriverController._instancia_driver = webdriver.Chrome(
                options=options
            )


    @classmethod
    def get_driver(cls) -> WebDriver:
        """
        Retorna a instância do driver do Selenium WebDriver.

        Se a instância do driver não existir, inicializa a classe para
        garantir que o driver seja criado.

        Args:
            cls: A própria classe.

        Returns:
            WebDriver: A instância do driver do Selenium WebDriver.
        """
        if cls._instancia_driver is None:
            cls()
        return cls._instancia_driver


    def open_site(self, url: str):
        """
        Abre o site especificado na instância do driver do
        Selenium WebDriver.

        Args:
            url (str): URL do site a ser aberto.
        """
        if WebDriverController._instancia_driver:
            WebDriverController._instancia_driver.get(url)


    def close_browser(self):
        """
        Fecha a instância do Selenium WebDriver.
        """
        if WebDriverController._instancia_driver:
            WebDriverController._instancia_driver.quit()
            WebDriverController._instancia_driver = None


    def screenshot_of_screen(self, path_image: str = 'erro.png'):
        """
        Faz um screenshot da tela e salva na pasta especificada.

        Args:
            path_image (str): Caminho onde a imagem deverá ser salva.
        """
        if WebDriverController._instancia_driver:
            WebDriverController._instancia_driver.save_screenshot(path_image)
            return path_image