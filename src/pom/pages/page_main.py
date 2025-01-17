from typing import Any, Generator, Dict

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from src.pom.web_driver_base_actions import WebDriverBaseActions
from src.pom.locators.page_main_locators import PageMainLocators



class PageMain(WebDriverBaseActions):
    """
    Classe para interações na página principal da aplicação web.

    Esta classe utiliza o padrão de design Page Object Model (POM) para
    encapsular a lógica de interação com os elementos da página principal.
    O POM facilita a manutenção do código, permitindo uma separação clara
    entre a lógica de teste e a estrutura da página.

    Attributes:
        driver (WebDriver): A instância do Selenium WebDriver, herdada
        da classe base.
    """

    def __init__(self):
        """
        Inicializa a página principal chamando o construtor da classe base.

        A classe base WebDriverBaseActions fornece métodos comuns para
        interações com o WebDriver, como clicar em elementos e digitar texto.
        """
        super().__init__()


    def get_url_file(self, element: WebElement, selector: tuple) -> str:
        """
        Captura o atributo href do botão de download na página.

        Este método utiliza os localizadores definidos na classe 
        PageMainLocators para encontrar o botão de download e obter
        o URL associado.

         Args:
            element (WebElement): O elemento onde o botão de download
            está localizado.
            selector (tuple): O seletor para localizar o elemento
            específico na página.

        Returns:
            str: O URL do arquivo a ser baixado.

        Raises:
            Exception: Se ocorrer um erro ao capturar o atributo
            href do elemento.
        """
        try:
            attribute = self._find_element_in_web_element(element, selector)
            href_value = attribute.get_attribute('href')
            return href_value
        except Exception as error:
            raise Exception(
                f'Erro ao capturar o atributo href do elemento: {error}'
            )


    def check_button_next_disabled(self) -> bool|None:
        """
        Verifica se o botão "Next" está desabilitado.

        Este método localiza o botão de paginação e verifica se ele está
        desabilitado. Retorna True se o botão estiver desabilitado,
        ou None caso contrário.

        Returns:
            bool | None: Retorna True se o botão estiver desabilitado,
            caso contrário None.
        """
        try:
            self.wdw = WebDriverWait(self.driver, 1)
            element = self._find_element_in_page(
                PageMainLocators.BUTTON_NEXT_PAGE_DISABLED
            )
            if element:
                return True
            return None
        except (NoSuchElementException, TimeoutException) as error:
            return None
        
    
    def click_next_button(self):
        """
        Clica no botão "Next" para avançar para a próxima página.

        Este método chama o método `_click` para clicar no botão de
        navegação para a próxima página da tabela.
        """
        try:
            self._click(PageMainLocators.BUTTON_NEXT_PAGE)
        except Exception as error:
            raise Exception(
                f'Erro ao clicar no botão Next no site: {error}'
            )


    def check_table(self) -> bool|None:
        """
        Verifica se a tabela está presente na página.

        Este método localiza a tabela na página principal e verifica se
        ela existe. Retorna True se a tabela for encontrada,
        caso contrário None.

        Returns:
            bool | None: Retorna True se a tabela estiver presente.

        Raises:
            NoSuchElementException, TimeoutException: Caso o elemento não
            for encontrado na página ou o tempo de procura pelo elemento
            for estourado irá ser gerado a exceção.
        """
        try:
            element = self._find_element_in_page(PageMainLocators.TABLE)
            if element:
                return True
            return None
        except (NoSuchElementException, TimeoutException) as error:
            raise Exception(
                f'Erro ao encontrar a tabela inicial no site: {error}'
            )
        
            
    def get_rows(self) -> Generator[dict[str, str], Any, None]:
        """
        Este método percorre as linhas da tabela na página atual,
        extrai as informações relevantes de cada linha
        (id, data e link do arquivo) e as retorna uma por uma de forma
        eficiente usando o 'yield'. 

        Ao invés de retornar todos os dados de uma vez, o 'yield'
        permite que os dados sejam gerados e retornados sob demanda,
        o que é útil para economizar memória, especialmente quando
        lidamos com tabelas grandes.

        Yields:
            dict: Um dicionário contendo os dados de uma linha da tabela
            com as seguintes chaves:
                - 'id': Identificador da linha, extraído da segunda célula.
                - 'date': Data associada à linha, extraída da
                terceira célula.
                - 'file_link': URL do arquivo associado à linha,
                extraída da quarta célula.

        Exceptions:
            Exceções podem ser levantadas em caso de erro durante a captura
            dos dados ou falha ao localizar os elementos da página.
        """
        rows = self._find_elements_in_page(PageMainLocators.ROWS_OF_TABLE)
        for row in rows:
            cells = self._find_elements_in_web_element(
                row, PageMainLocators.CELLS_OF_ROWS
            )
            if len(cells) > 3:
                element_url_file = self.get_url_file(
                    cells[3], PageMainLocators.LINK_TO_URL_FILE
                )
                yield {
                    'NUMERO_DA_FATURA': cells[1].text,
                    'DATA_DA_FATURA': cells[2].text,
                    'URL_DA_FATURA': element_url_file
                }
