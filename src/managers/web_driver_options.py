from selenium.webdriver.chrome.options import Options


class WebDriverOptions:
    """
    Representa as opções para configurar uma instância do Selenium
    WebDriver.

    Attributes:
        _instancia (None): A instância da classe WebDriverOptions.
        options (Options); O objeto Options do Selenium WebDriver.
    """
    _instance = None


    def __init__(self):
        """
        Inicializa a instância do WebDriverOptions.
        Se WebDriverOptions._instance for None, define o atributo 'options'
        como uma nova instância de 'Options()'. Caso contrário, define
        o atributo 'options' como a WebDriverOptions._instance existente.
        """
        if WebDriverOptions._instance is None:
            self.options = Options()
            WebDriverOptions._instance = self
        else:
            self.options = WebDriverOptions._instance.options


    def add_argument(self, argument: str):
        """
        Adiciona um argumento as opções do WebDriver.

        Args:
            argument (str): o argumento a ser adicionado as opções
            do WebDriver.
        """
        self.options.add_argument(argument)


    def add_experimental_option(self, option_name: str, option_value):
        """
        Adiciona uma opção experimental as opções do WebDriver.
        
        Args:
            option_name (str): O nome da opção experimental a ser adicionada
            as opções do WebDriver.
            option_value : O valor associado a opção experimental. Pde variar
            de tipo dependendo da opção adicionada.
        """
        self.options.add_experimental_option(option_name, option_value)
        

    def get_options(self) -> Options:
        """
        Retorna o objeto Options da instância do WebDriverOptions.

        Returns:
            Options: O objeto Options.
        """
        return self.options