# Sistema de Envio de Documentos 
- Este é um sistema que permite o cadastro do usuário, o usuário então pode fazer upload de arquivos pdf. Estes arquivos serão então tratados pela equipe admin, que possui acesso aos arquivos, e ao tratá-los, os arquivos serão enviados de volta. Todos os arquivos do usuário poderão ser acessados por ele a qualquer momento.
- Neste sistema eu estudo a implementação de um sistema de envio de emails, assim como o uso do signals para a ocorrência de ações automáticas, relacionadas a eventos do sistema.  


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
>Desta forma instalamos a versão 2.1 do django.

<br />

* Clone o repositório:
- git clone https://github.com/victor-s-santos/sistema-de-upload-de-documentos.git

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
