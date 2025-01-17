from selenium.webdriver.common.by import By

from src.pom.locators.locator import Locator



class PageMainLocators:
    """
    Localizadores para elementos na página principal do site.
    
    O POM organiza o código de automação em classes que representam
    páginas específicas da aplicação web. Cada classe contém métodos
    que correspondem às ações que podem ser realizadas nessa página.

    Esse padrão torna o código mais modular e reutilizável,
    facilitando a manutenção e a leitura.

    Isso facilita a modificação de locadores, pois, se um seletor mudar,
    apenas a definição no localizador precisa ser atualizada,
    sem a necessidade de alterar várias partes do código.
    """
    
    TABLE = Locator(By.ID, 'tableSandbox')
    ROWS_OF_TABLE = Locator(By.CSS_SELECTOR, 'table tbody tr')
    CELLS_OF_ROWS = Locator(By.TAG_NAME, 'td')
    LINK_TO_URL_FILE = Locator(By.TAG_NAME, 'a')
    BUTTON_NEXT_PAGE = Locator(By.ID, 'tableSandbox_next')
    BUTTON_NEXT_PAGE_DISABLED = Locator(
        By.CSS_SELECTOR, '#tableSandbox_next.disabled'
    )
