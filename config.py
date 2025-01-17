from datetime import datetime
import os


TIME_EXECUTION = datetime.now().strftime('%d.%m.%Y_%H.%M.%S')

# URL do site que será acessado durante a automação.
URL_SITE  = 'https://rpachallengeocr.azurewebsites.net/'

# Constantes de diretórios, definindo caminhos para armazenamento de arquivos.
BASE_DIRECTORY = os.getcwd()
DIRECTORY_CSVS = os.path.join(BASE_DIRECTORY, 'RESULTS')
DIRECTORY_IMGS = os.path.join(BASE_DIRECTORY, 'IMGS', TIME_EXECUTION)
DIRECTORY_IMGS_ERRORS = os.path.join(BASE_DIRECTORY, 'IMGS', 'ERRORS')

COLUMNS_CSV_FILE = ['NUMERO_DA_FATURA', 'DATA_DA_FATURA', 'URL_DA_FATURA']

# Variáveis de controle do fluxo do programa
loop = 'ON'  # Controle para manter o loop ativo
state = 'INITIALIZATION'  # Estado inicial do sistema
first_execution = True  # Flag para indicar a primeira execução
