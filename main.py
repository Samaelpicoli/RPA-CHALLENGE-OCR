from config import *
from src.managers import utils
from src.managers.csv_manager import CsvManager
from src.managers.directory_manager import DirectoryManager
from src.managers.logger import Logger
from src.managers.requests_manager import RequestManager
from src.managers.web_driver_options import WebDriverOptions
from src.pom.pages.page_main import PageMain


"""
Antes da execução, por favor leia o arquivo README.md
para um melhor entendimento.
"""



while loop == 'ON':
    
    match state:

        case 'INITIALIZATION':
            """
            Este estado inicia o processo de configuração da aplicação.
            A aplicação configura o ambiente de execução,
            incluindo a inicialização do logger, a configuração do WebDriver
            e a realização do login no site.

            - Verifica se é a primeira execução e registra a inicialização.
            - Instancia gerenciadores para logs, requisições e diretórios de
            imagens e CSV.
            - Cria um arquivo CSV com as colunas especificadas e
            gerencia seu conteúdo.
            - Configura opções do WebDriver para maximizar a janela
            e desabilitar notificações.
            - Se tudo ocorrer sem erros, o estado é alterado para 'PROCESS'.
            - Em caso de erro, registra a exceção e altera
            o estado para 'END'.

            Attributes:
                logger (Logger): Instância do logger para registrar 
                informações.
                request (RequestManager): Classe para gerenciar
                requisições HTTP.
                directory_csv (DirectoryManager): Classe para gerenciar
                o diretório onde estarão os arquivos CSV.
                directory_imgs (DirectoryManager): Classe para gerenciar
                o diretório onde estarão os arquivos PNG.
                csv_manager (CsvManager): Classe para manipulação de
                arquivos CSV.
                options (WebDriverOptions): Configurações do WebDriver.
                main_page (PageMain): Classe responsável pelas interações na
                página principal.      
            """
            try:
                if first_execution:

                    success = False

                    logger = Logger()
                    logger.info('Iniciando o Processo.')

                    request = RequestManager()

                    directory_imgs = DirectoryManager(DIRECTORY_IMGS)

                    directory_imgs_errors = DirectoryManager(
                        DIRECTORY_IMGS_ERRORS
                    )

                    directory_csv = DirectoryManager(DIRECTORY_CSVS)

                    name_csv = utils.get_file_csv_name(DIRECTORY_CSVS)
                    file_csv = utils.create_csv_file(
                        name_csv, COLUMNS_CSV_FILE
                    )

                    csv_manager = CsvManager(file_csv)
                    csv_manager.view_df()
                    csv_manager.save_file()

                    directory_imgs.delete_files()

                    logger.info('Diretórios e arquivo CSV criados...')

                    options = WebDriverOptions()
                    options.add_argument('--start-maximized')
                    options.add_argument('--disable-notifications')
                    page_main = PageMain()

                state = 'PROCESS'
                continue

            except Exception as error:
                logger.error('Erro durante a inicialização do processo:')
                logger.error(f'{error}')
                state = 'END'
                continue


        case 'PROCESS':
            """
            Estado para processamento de faturas.

            Neste estado, a aplicação coleta e processa faturas a partir do
            site, utilizando o item capturado anteriormente. A lógica de
            processamento é projetada para operar de maneira sequencial,
            garantindo que cada fatura seja tratada adequadamente
            antes de passar para a próxima.

            Este estado também combina o
            uso de Selenium para automação de navegador e Requests para
            manipulação de requisições HTTP.

            A comunicação entre as classes `PageMain`, `RequestManager`
            e `CsvManager` é crucial, permitindo que a aplicação mantenha
            o controle do estado dos dados enquanto interage com a interface
            do usuário. Os logs são utilizados para registrar informações
            importantes sobre o fluxo e facilitar a depuração
            em caso de falhas.
            """
            try:
                if first_execution:

                    page_main.open_site(URL_SITE)

                    logger.info(f'Inicializou o site: {URL_SITE}')

                    table_exists = page_main.check_table()
                    if not table_exists:
                        logger.error(
                            'Erro: Tabela não foi encontrada ao inicializar o site.'
                        )
                        state = 'END'
                        continue

                    first_execution = False

                for row_data in page_main.get_rows():

                    date = row_data['DATA_DA_FATURA']
                    date_is_valid = utils.check_date_before_or_today(date)

                    if date_is_valid:
                        logger.info(
                            f'Data: {date} é menor ou igual a data de hoje.'
                        )
                        row_data['DATA_DA_FATURA'] = utils.format_date(date)
                        id_fatura = row_data['NUMERO_DA_FATURA']

                        response = request.get(row_data['URL_DA_FATURA'])
                        path_img = request.convert_response_to_file_img(
                            response, DIRECTORY_IMGS, f'{id_fatura}.png'
                        )
                        logger.info(
                            f'Dowload da Fatura com sucesso, disponível em: {path_img}'
                        )

                        csv_manager.add_data(row_data)
                        csv_manager.save_file()
                        logger.info(
                            f'Linha da fatura {id_fatura} adicionada com sucesso no arquivo CSV.'
                        )

                button_is_disabled = page_main.check_button_next_disabled()
                if button_is_disabled:
                    logger.info(
                        'Botão Next desabilitado, robô fez toda a paginação.'
                    )
                    success = True
                    state = 'END'
                    continue
                page_main.click_next_button()
                logger.info('Indo para a próxima página.')

            except Exception as error:
                name_img = utils.get_img_name(
                    DIRECTORY_IMGS_ERRORS, 'erro.png'
                )
                page_main.screenshot_of_screen(name_img)
                logger.error('Erro durante o processamento dos itens.')
                logger.error(f'{error}')
                state = 'END'
                continue

        case 'END':
            """
            Estado para finalização do processo.

            Neste estado, a aplicação encerra o fluxo
            de trabalho após o processamento das faturas,
            registrando o resultado final. Dependendo do
            sucesso ou falha do processo, diferentes ações
            são realizadas.

            O fluxo de trabalho inclui:
            1. Verificação do status de sucesso (`success`):
            - Se `True`, registra o caminho do arquivo CSV e o
            diretório das faturas, além de informar que o processo
            foi concluído com sucesso.
            - Se `False`, gera alertas informando sobre a disponibilidade
            das imagens de erro e recomenda verificar as falhas
            durante a execução.

            2. Fechamento do navegador através de
            `page_main.close_browser()` para liberar recursos.

            3. Atualização do loop para 'OFF', indicando que o
            processo foi finalizado e não deve haver mais iterações.
            """
            if success == True:
                logger.info(f'Caminho arquivo CSV: {file_csv}')
                logger.info(
                    f'Camminho da pasta das faturas: {DIRECTORY_IMGS}'
                )
                logger.info('Processo concluído com Sucesso.')
                print('Processo concluído com Sucesso.')
            else:
                logger.alert(
                    f'Imagens de erros disponíveis em {DIRECTORY_IMGS_ERRORS}'
                )
                logger.alert(
                    'Processo teve falhas durante a execução. Verificar!'
                )
                print('Processo teve falhas durante a execução. Verificar!')
            page_main.close_browser()
            loop = 'OFF'
            continue