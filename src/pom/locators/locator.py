from selenium.webdriver.common.by import By


class Locator:
    """
    Representa um localizador de elemento na página web.

    Os localizadores são usados para identificar elementos na interface
    do usuário de uma página web, facilitando a interação com esses
    elementos durante a automação.

    Attributes:
        by (By): O método de localização do elemento.
        value (str): O valor do localizador, que pode ser um seletor
        CSS, ID, etc.
    """

    def __init__(self, by, value):
        """
        Inicializa a classe Locator.

        Args:
            by (By): O método de localização do elemento.
            value (str): O valor do localizador, seletor HTML.
        """
        self.by = by
        self.value = value


    def __repr__(self) -> str:
        """
        Converte o by para um objeto WebDriver.By e retorna
        ele como um objeto, contendo o método e o valor do
        localizador no HTML.

        Returns:
            str: Uma string no formato '(by, value)'.
        """
        by_name = {
            By.ID: 'By.ID',
            By.CLASS_NAME: 'By.CLASS_NAME',
            By.XPATH: 'By.XPATH',
            By.NAME: 'By.NAME',
            By.CSS_SELECTOR: 'By.CSS_SELECTOR',
            By.TAG_NAME: 'By.TAG_NAME',
            By.LINK_TEXT: 'By.LINK_TEXT',
            By.PARTIAL_LINK_TEXT: 'By.PARTIAL_LINK_TEXT'
        }.get(self.by, self.by)
        return f'({by_name}, "{self.value}")'