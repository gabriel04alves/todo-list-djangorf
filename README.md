# TODO List API - Django REST Framework

##### Este projeto foi desenvolvido como parte da disciplina de **Desenvolvimento Web II**, utilizando um template disponibilizado pelo professor [**Marco André Mendes**](https://github.com/marrcandre/template_django_pdm).

#

[![Imagem do Core](core.png)](core.png)

## Descrição

Este é um projeto de API REST para gerenciamento de tarefas, construído com Django e Django REST Framework. Ele permite aos usuários criar, visualizar, atualizar e excluir tarefas e categorias.

## Funcionalidades

- Autenticação de usuário via Passage e JWT.
- Gerenciamento de usuários, tarefas e categorias.
- API documentada com drf-spectacular (OpenAPI 3).
- Filtragem, ordenação e busca de tarefas e categorias.
- Atualização automática de tarefas atrasadas.
- Categorização de tarefas.
- Suporte a upload de arquivos para tarefas e usuários (via Cloudinary ou armazenamento local).
- Configuração para ambientes de desenvolvimento e produção.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/) (para documentação OpenAPI 3)
- [Passage](https://passage.id/) (para autenticação sem senha)
- [djangorestframework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt) (para autenticação JWT)
- [Cloudinary](https://cloudinary.com/) (para armazenamento de mídia na produção)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) (para conexão com PostgreSQL)
- [gunicorn](https://gunicorn.org/) (servidor WSGI)
- [whitenoise](http://whitenoise.evans.io/en/stable/) (para servir arquivos estáticos)
- [python-dotenv](https://github.com/theskumar/python-dotenv) (para gerenciar variáveis de ambiente)
- [PDM](https://pdm.fming.dev/) (gerenciador de pacotes)
- [Black](https://github.com/psf/black) e [isort](https://github.com/PyCQA/isort) (para formatação de código)
- [Pylint](https://www.pylint.org/) (para análise estática de código)
- [Pre-commit](https://pre-commit.com/) (para garantir qualidade do código antes do commit)

## Estrutura do Projeto

```
├── .env.exemplo # Exemplo de arquivo .env
├── .gitignore # Arquivos ignorados pelo Git
├── .isort.cfg # Configurações do isort
├── .pdm-python # Caminho do interpretador Python usado pelo PDM
├── .pre-commit-config.yaml # Configurações do pre-commit
├── .pylintrc # Configurações do Pylint
├── .vscode # Configurações do VSCode
│ └── settings.json
├── Procfile # Para deploy no Heroku
├── app # Diretório principal do projeto Django
│ ├── init.py
│ ├── asgi.py # Configuração ASGI
│ ├── settings.py # Configurações do Django
│ ├── urls.py # URLs do projeto
│ └── wsgi.py # Configuração WSGI
├── build.sh # Script para build da aplicação
├── core.png # Imagem do Core (exemplo)
├── core # Aplicação Django "core"
│ ├── init.py
│ ├── admin.py # Configurações do Django Admin
│ ├── apps.py # Configuração da aplicação
│ ├── authentication.py # Lógica de autenticação
│ ├── migrations # Migrações do banco de dados
│ │ ├── ...
│ │ └── init.py
│ ├── models # Definição dos modelos de dados
│ │ ├── init.py
│ │ ├── categoria.py
│ │ ├── tarefa.py
│ │ └── user.py
│ ├── serializers # Serializadores para a API REST
│ │ ├── init.py
│ │ ├── categoria.py
│ │ ├── tarefa.py
│ │ └── user.py
│ └── views # Views da API REST
│ │ ├── init.py
│ │ ├── categoria.py
│ │ ├── tarefa.py
│ │ └── user.py
├── db.sqlite3 # Banco de dados SQLite (para desenvolvimento)
├── dump.json # Dump dos dados do banco
├── manage.py # Script para gerenciar o Django
├── pdm.lock # Arquivo de lock do PDM
├── pyproject.toml # Configurações do projeto PDM
├── requirements.txt # Lista de dependências
└── scripts # Scripts úteis
├── cria_api.py
└── set_my_ip.py
```

## Configuração Inicial

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/gabriel04alves/todo-list-djangorf
    cd todo-list-djangorf
    ```

2.  **Configurar o ambiente virtual (usando PDM):**

    ```bash
    pdm install
    ```

3.  **Configurar as variáveis de ambiente:**

    - Copie o arquivo `.env.exemplo` para `.env`.
    - Preencha as variáveis de ambiente no arquivo `.env`. É fundamental gerar uma chave secreta robusta e manter o `.env` fora do versionamento (ele já está no `.gitignore`).

    ```bash
    cp .env.exemplo .env
    # Edite .env e preencha as variáveis
    ```

4.  **Executar as migrações:**

    ```bash
    pdm run pre_migrate && pdm run migrate
    ```

5.  **Criar um superusuário (opcional):**

    ```bash
    pdm run createsuperuser
    ```

6.  **Rodar o servidor de desenvolvimento:**

    ```bash
    pdm run dev
    ```

## Variáveis de Ambiente

As seguintes variáveis de ambiente precisam ser configuradas no arquivo `.env`:

- `MODE`: Modo de execução da aplicação (`DEVELOPMENT`, `PRODUCTION`, `MIGRATE`).
- `DEBUG`: Ativa o modo de debug do Django (`True` ou `False`).
- `WEB_CONCURRENCY`: Número de workers do Gunicorn.
- `SECRET_KEY`: Chave secreta do Django. **Gere uma chave forte para produção!**
- `CLOUDINARY_URL`: URL do Cloudinary (necessário para produção com Cloudinary). Ex: `cloudinary://your_api_key:your_api_secret@your_cloud_name`
- `PASSAGE_APP_ID`: ID da aplicação Passage.
- `PASSAGE_API_KEY`: Chave da API Passage.
- `MY_IP`: Endereço IP do seu computador (usado em desenvolvimento para acessar arquivos de mídia).

## Endpoints da aplicação

### **Categorias**

- **GET** `/api/categorias/`  
  Lista todas as categorias.
- **POST** `/api/categorias/`  
  Cria uma nova categoria.
- **GET** `/api/categorias/{id}/`  
  Retorna detalhes de uma categoria específica.
- **PUT** `/api/categorias/{id}/`  
  Atualiza todos os campos de uma categoria.
- **PATCH** `/api/categorias/{id}/`  
  Atualiza parcialmente uma categoria.
- **DELETE** `/api/categorias/{id}/`  
  Remove uma categoria.
- **GET** `/api/categorias/total_by_category/`  
  Retorna o total de tarefas por categoria (relatório customizado).

---

### **Tarefas**

- **GET** `/api/tarefas/`  
  Lista todas as tarefas.
- **POST** `/api/tarefas/`  
  Cria uma nova tarefa.
- **GET** `/api/tarefas/{id}/`  
  Retorna detalhes de uma tarefa específica.
- **PUT** `/api/tarefas/{id}/`  
  Atualiza todos os campos de uma tarefa.
- **PATCH** `/api/tarefas/{id}/`  
  Atualiza parcialmente uma tarefa.
- **DELETE** `/api/tarefas/{id}/`  
  Remove uma tarefa.
- **POST** `/api/tarefas/complete_all_tasks/`  
  Completa todas as tarefas pendentes (ação customizada).
- **POST** `/api/tarefas/update_overdue_tasks/`  
  Atualiza tarefas atrasadas (ação customizada).

---

### **Usuários**

- **GET** `/api/usuarios/`  
  Lista todos os usuários.
- **POST** `/api/usuarios/`  
  Cria um novo usuário.
- **GET** `/api/usuarios/{id}/`  
  Retorna detalhes de um usuário específico.
- **PUT** `/api/usuarios/{id}/`  
  Atualiza todos os campos de um usuário.
- **PATCH** `/api/usuarios/{id}/`  
  Atualiza parcialmente um usuário.
- **DELETE** `/api/usuarios/{id}/`  
  Remove um usuário.
- **GET** `/api/usuarios/me/`  
  Retorna informações do usuário autenticado.

---

### **Autenticação**

- **POST** `/token/`  
  Gera um token JWT para autenticação.
- **POST** `/token/refresh/`  
  Atualiza um token JWT expirado.

---

### **Documentação**

- **GET** `/api/schema/`  
  Retorna o schema OpenAPI 3.0 da API.
- **GET** `/api/swagger/`  
  Interface Swagger UI para testar a API.
- **GET** `/api/redoc/`  
  Interface Redoc para documentação.

---

### Observações:

1. **Padrão REST**:  
   Os endpoints de CRUD (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) seguem o padrão REST.
2. **Ações Customizadas**:  
   Endpoints como `/complete_all_tasks/` e `/update_overdue_tasks/` usam **POST** para ações que não se encaixam em operações CRUD tradicionais.
3. **Autenticação e Documentação**:  
   Os endpoints `/token/`, `/token/refresh/`, `/api/swagger/` e `/api/redoc/` foram incluídos para completar a lista.

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir com este projeto, siga os passos abaixo:

1. **Fork o repositório:**

   Clique no botão "Fork" no canto superior direito da página do repositório.

2. **Clone o seu fork:**

   ```bash
   git clone https://github.com/gabriel04alves/todo-list-djangorf
   cd todo-list-djangorf
   ```

3. **Crie uma branch para a sua feature ou correção:**

   ```bash
   git checkout -b minha-feature
   ```

4. **Faça as alterações desejadas e commit:**

   ```bash
   git add .
   git commit -m "Descrição das alterações"
   ```

5. **Envie as alterações para o seu fork:**

   ```bash
   git push origin minha-feature
   ```

6. **Abra um Pull Request:**

   Vá até a página do repositório original e clique no botão "New Pull Request". Descreva as alterações propostas e envie o PR para revisão.

Agradeço por contribuir!
