# MVP Alfa 
- Este é o primeiro mvp do projeto que faz upload do pdf, e após a análise, retorna para o usuário o pdf discriminado.


## Como rodar:

* Criação de um virtualenv(no linux, usando python3):
- python -m venv .venv
>o ponto indica que será criado um diretório invisível
<br />

* Ativação deste virtualenv:
- source .venv/bin/activate
>Está linha deverá ser executada no terminal aberto dentro do diretório onde o virtualenv foi criado
<br />

* Com o virtualenv ativo, vamos instalar o django:
- pip install django==2.1
>Desta forma instalamos a versão 2.1 do django. Está versão é a mais estável
<br />

>Como não estou utilizando libs a não ser o django, é desnecessária a criação do requirement.txt
<br />

* Clone o repositório:
- git clone https://github.com/JurisfAI/MVPAlfa.git

- __Na raíz do repositório, rodar:__
    
    
    * __Iniciar o servidor:__
        -python manage.py runserver
        `Desta forma será iniciado o servidor, para sair basta dar ctrl+c no terminal`
        `Acessar http://127.0.0.1:8000/`
        
        <br />
        
    * __Rodar as migrações do banco de dados:__
        -python manage.py migrate
        `Será criado na raiz do diretório um arquivo .sqlite3`
        
        <br />
        
    * __Criar superusuario:__
        -python manage.py createsuperuser
        `Assim, pode-se acessar o admin: http://127.0.0.1:8000/admin`
