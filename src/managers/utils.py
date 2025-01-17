from datetime import datetime
import os
from typing import List

import pandas as pd


def get_file_csv_name(directory: str) -> str:
    """
    Gera um nome de arquivo CSV baseado na data e hora atuais.

    O nome do arquivo é formatado como
    'FATURAS_DD-MM-YYYY_HH.MM.SS.csv', onde 'DD-MM-YYYY'
    é a data atual e 'HH.MM.SS' é a hora atual.

    Returns:
        str: O nome do arquivo gerado.
    """
    date = datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    file_name = f'FATURAS_{date}.csv'
    full_path = os.path.join(directory, file_name)
    return full_path


def get_img_name(directory: str, name: str) -> str:
    """
    Gera um caminho completo para um arquivo de imagem baseado
    na data e hora atuais.

    O nome do arquivo é formatado como 'name_DD-MM-YYYY_HH.MM.SS.png',
    onde 'name' é o nome fornecido como argumento, 'DD-MM-YYYY' é a
    data atual e 'HH.MM.SS' é a hora atual. O caminho da imagem
    é construído utilizando o diretório especificado.

    Args:
        directory (str): O diretório onde a imagem será salva.
        name (str): O nome base para o arquivo de imagem.

    Returns:
        str: O caminho completo do arquivo de imagem gerado.
    """
    date = datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
    file_name = f'{name}_{date}.png'
    path_img = os.path.join(directory, file_name)
    return path_img


def check_date_before_or_today(
        date_str: str, date_format: str = '%d-%m-%Y'
    ) -> bool:
    """
    Verifica se a data fornecida é anterior ou igual à data de hoje.

    Args:
        date_str (str): A data a ser verificada, no formato de string.
        date_format (str): O formato da data fornecida
        (default é "%Y-%m-%d").

    Returns:
        bool: True se a data fornecida for anterior ou igual à data
        de hoje, caso contrário False.
    """
    try:
        input_date = datetime.strptime(date_str, date_format)
        today = datetime.today().date()
        return input_date.date() <= today
    
    except ValueError:
        return False
    

def format_date(
        date_str: str,
        date_format_origin: str = '%d-%m-%Y',
        date_format_final: str = '%d/%m/%Y'
    ) -> bool:
    """
    Formata uma string de data de um formato para outro.

    Args:
        date_str (str): A data a ser formatada, como uma string.
        date_format_origin (str): O formato original da data
        (padrão: '%d-%m-%Y').
        date_format_final (str): O formato desejado para a data
        (padrão: '%d/%m/%Y').

    Returns:
        str: A data formatada como uma string se bem-sucedido;
    
    Raises:
        ValueError: Se a data fornecida não estiver no formato esperado.
    """
    try:
        input_date = datetime.strptime(date_str, date_format_origin)
        date_formatted = input_date.strftime(date_format_final)
        return date_formatted
    except ValueError:
        raise Exception('Erro ao realizar a formatação da data.')
    

def create_csv_file(file: str, columns: List[str]) -> str:
    """
    Cria um arquivo CSV com as colunas especificadas.

    Args:
        file (str): O caminho do arquivo CSV a ser criado.
        columns (List[str]): Uma lista de nomes de colunas
        para o DataFrame.

    Returns:
        str: O caminho do arquivo CSV criado.
    """
    df = pd.DataFrame(columns=columns)
    df.to_csv(file, index=False)
    return file
