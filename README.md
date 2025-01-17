# RPA CHALLENGE OCR

# Sobre o projeto

Atividade realizada com base no exercício 'RPA Challenge OCR' proposto no site: [text](https://rpachallengeocr.azurewebsites.net/).

RPA Challenge OCR é uma aplicação web para treinamento de RPA, onde deve ser feito a coleta dos dados disponibilizados na tabela, realizada a validação da data (deve possuir uma data inferior ou igual a data atual) e caso for validado, realizar o download do arquivo PNG com a imagem da fatura e seguir nesse processo fazendo a navegação através de sua paginação.

As pastas utilizadas para execução do robô serão criadas em tempo de execução caso não existirem.

Ao final da coleta dos dados e downloads dos arquivos cuja linha foi validada, será gerado um arquivo CSV com o Número da Fatura, Data da Fatura e a URL da imagem da Fatura na pasta selecionada pelo usuário, e as imagens serão armazenadas em um diretório com o dia e horário da execução.

A verificação dos caminhos onde o arquivo CSV e as Faturas foram salvas pode ser visualizado na pasta LOGS no arquivo diário de log da execução, nele estará maiores detalhes do processo durante sua execução e finalização.


# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Pandas

Selenium

Requests

Demais bibliotecas estão listadas no arquivo 'requirements.txt'

## Sobre o código

O projeto foi desenvolvido utilizando o paradigma Orientado a Objetos, destacando a implementação de padrões de projeto como Singleton e Page Object Model (POM). O arquivo main.py contém todas as funcionalidades do projeto, incluindo a requisição dos arquivos PNG via Requests, a inclusão dos dados capturados no arquivo CSV via Pandas e a interação com o site da atividade, utilizando Selenium para automação de navegação.

### Estrutura do Projeto
No main, o projeto é estruturado como uma máquina de estados (INITIALIZATION, PROCESS, END), emulando o ReFramework do UiPath. Essa abordagem auxilia na criação de automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

### Padrões de Projeto
Singleton: O uso do padrão Singleton garante que apenas uma instância do WebDriver seja criada, centralizando o controle e a manipulação das interações com o navegador. Isso evita a sobrecarga de múltiplas instâncias e melhora a eficiência do sistema.
Page Object Model (POM): A implementação do POM facilita a separação das lógicas de interação com a interface do usuário, tornando o código mais modular e legível. Isso permite que as classes de página sejam reutilizadas e mantidas de forma independente da lógica de negócios.


### Facilidade de Manutenção
O design modular do projeto, aliado ao uso de padrões de projeto como POM e Singleton, proporciona uma facilidade significativa para manutenção e evolução do código.

### Manipulação de Dados
O projeto realiza a leitura, escrita e manipulação de dados de forma eficiente. Utiliza-se o requests para realizar requisições HTTP e o pandas para manipulação de arquivos CSV. A lógica de captura e atualização de dados é clara e organizada, permitindo fácil acesso e modificação.


### Princípios SOLID
Os princípios SOLID estão presentes neste projeto, garantindo que o código seja bem estruturado e fácil de entender. Cada classe e método é responsável por uma única tarefa, promovendo a coesão e reduzindo o acoplamento entre os componentes do sistema. Isso não apenas melhora a legibilidade do código, mas também facilita a realização de testes e a implementação de novas funcionalidades.


### Testes
A realização de testes é essencial no desenvolvimento de Robotic Process Automation (RPA) para garantir a confiabilidade das automações. Os testes unitários, utilizando o framework "pytest", permitem verificar componentes individuais do sistema, assegurando que cada parte funcione corretamente.

Os testes focaram em:

* Requisições HTTP: Verificando a adequação das interações com APIs e o tratamento de erros.
* Manipulação de Arquivos: Garantindo que a leitura, escrita e organização de arquivos estejam corretas.

Esses testes aumentam a qualidade do código, facilitam a manutenção e reduzem o tempo de debugging, promovendo uma cultura de desenvolvimento mais eficiente e sólida.

# Como executar o projeto
Pré-requisitos: Python 3.10+ e possuir o Google Chrome instalado

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
# python -m venv venv
# Ativar ambiente:
# Linux/Mac: source venv/bin/activate
# Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser uma automação web baseada no código fonte do site e utilizando Xpaths, Ids e Class, pode ser que em 
algum momento a automação pare de funcionar caso o site mude.

# Autor
Samael Muniz Picoli
