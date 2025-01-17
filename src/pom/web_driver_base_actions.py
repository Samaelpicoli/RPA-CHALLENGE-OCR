from typing import List

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from src.managers.web_driver_controller import WebDriverController



class WebDriverBaseActions(WebDriverController):
    """
    Classe base para ações com o WebDriver, estendendo WebDriverController.
    
    Esta classe fornece métodos comuns de interação com a interface do usuário
    usando o Selenium WebDriver. Ao estender WebDriverController, garante que
    todas as interações utilizem uma única instância do WebDriver,
    implementando o padrão de design Singleton. Além disso, segue o conceito
    do padrão de projeto Page Object Model (POM), que separa a lógica de
    interação com a interface de usuário da lógica de testes, proporcionando
    uma estrutura mais modular e reutilizável.


    Attributes:
        driver (WebDriver): A instância do Selenium WebDriver.
        wdw (WebDriverWait): O objeto para controle de espera.
        ac (ActionChains): O objeto para realizar ações com o mouse.
    """

    def __init__(self):
        """
        Inicializa a classe e configura o driver e o WebDriverWait.

        O tempo de espera padrão para as operações é definido como
        60 segundos.
        """
        super().__init__()
        self.driver = self.get_driver()
        self.wdw = WebDriverWait(self.driver, 60)
        self.ac = ActionChains(self.driver)


    def _click(self, selector: tuple):
        """
        Clica em um elemento especificado pelo seletor.

        Args:
            selector (tuple): Localizador do elemento.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        self.driver.find_element(selector.by, selector.value).click()


    def _find_element_in_page(self, selector: tuple) -> WebElement:
        """
        Procura por um elemento na página.

        Args:
            selector (tuple): Localizador do elemento.

        Returns:
            WebElement: Retorna o elemento web encontrado.
        """
        self.wdw.until(
            ec.presence_of_element_located((selector.by, selector.value))
        )
        return self.driver.find_element(selector.by, selector.value)
    

    def _find_element_in_web_element(
            self, element: WebElement, selector: tuple
        ) -> WebElement:
        """
        Procura por um elemento dentro de outro elemento (WebElement).

        Este método é útil quando você já tem um WebElement e deseja buscar um
        elemento filho dentro dele. 

        Args:
            element (WebElement): O elemento onde a busca será realizada.
            selector (tuple): Localizador do elemento filho.

        Returns:
            WebElement: O elemento encontrado dentro do WebElement fornecido.
        """
        return element.find_element(selector.by, selector.value)
    

    def _find_elements_in_page(self, selector: tuple) -> List[WebElement]:
        """
        Procura por múltiplos elementos na página.

        Args:
            selector (tuple): Localizador do elemento.

        Returns:
            List[WebElement]: Lista de elementos web encontrados.
        """
        self.wdw.until(
            ec.presence_of_element_located((selector.by, selector.value))
        )
        elements = self.driver.find_elements(selector.by, selector.value)
        return elements
    

    def _find_elements_in_web_element(
            self, element: WebElement, selector: tuple
        ) -> List[WebElement]:
        """
        Procura por múltiplos elementos dentro de um WebElement.

        Semelhante a _find_elements_in_page, mas a busca ocorre dentro de um
        elemento específico, em vez de toda a página.

        Args:
            element (WebElement): O elemento onde a busca será realizada.
            selector (tuple): Localizador dos elementos filhos.

        Returns:
            List[WebElement]: Lista de elementos encontrados dentro
            do WebElement.
        """
        elements = element.find_elements(selector.by, selector.value)
        return elements


    def _move_mouse_to_hover_element(self, selector: tuple):
        """
        Move o mouse para o elemento especificado.

        Args:
            selector (tuple): Localizador do elemento.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        element = self.driver.find_element(selector.by, selector.value)
        self.ac.move_to_element(element).perform()


    def _type_input(self, selector: tuple, input_data: str):
        """
        Digita dados em um campo de entrada especificado pelo seletor.

        Args:
            selector: Localizador do elemento.
            input_data (str): Dados a serem inseridos no campo de entrada.
        """
        self.wdw.until(
            ec.element_to_be_clickable((selector.by, selector.value))
        )
        self.driver.find_element(selector.by, selector.value).clear()
        self.driver.find_element(
            selector.by, selector.value
        ).send_keys(input_data)


    def _get_text(self, selector: tuple) -> str:
        """
        Captura o texto de um elemento especificado pelo seletor.

        Args:
            selector (tuple): Localizador do elemento.

        Returns:
            str: O texto do elemento encontrado.
        """
        self.wdw.until(
            ec.visibility_of_element_located((selector.by, selector.value))
        )
        element = self.driver.find_element(selector.by, selector.value)
        return element.text
    
