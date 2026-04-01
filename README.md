## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para aprofundar conhecimento em:

- Arquitetura em camadas (services pattern)
- Processamento assíncrono com filas
- Organização desacoplada de responsabilidades
- Estrutura preparada para escalabilidade

# 📦 URL Shortener API

Serviço de encurtamento de URLs desenvolvido em **Python/Django** com foco em **boas práticas de backend**, **tarefas assíncronas (Celery + Redis)** e **teste fácil via Postman**.

Uma API simples e robusta que converte URLs longas em versões curtas e gerencia redirecionamentos de forma eficiente.

---

## 🚀 Funcionalidades

- 🎯 Encurtamento de URLs  
- 🔁 Redirecionamento por meio da URL curta  
- ⚡ Processamento assíncrono com **Celery + Redis**  
- 🧠 Organização por camadas (views, services, tasks)  
- 📬 Coleção do **Postman** para testes inclusa  
- 🧩 Preparado para escalabilidade

---

## 🧠 Tecnologias utilizadas

- 🐍 Python  
- 🚀 Django & Django REST Framework  
- 🐇 Celery (fila de tarefas)  
- 🔥 Redis (broker de filas)  
- 📦 SQLite (banco leve para desenvolvimento)  
- 📬 Postman (coleção para testar endpoints)

---

## 📡 Endpoints Principais

> 📌 Consulte a coleção do Postman disponível em `docs/postman` para testar todos os endpoints com exemplos prontos.

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto localmente, certifique-se de ter:

- Python 3.8+  
- Virtualenv (recomendado)  
- Redis rodando localmente ou remotamente (**configurar no `.env`**)

---

## 🛠️ Como rodar o projeto (local)

1. **Clonar repositório**
   ```bash
   git clone https://github.com/nicolas-aires-dev/Url_Shortener.git
   cd Url_Shortener

2. **Ativar ambiente virtual (venv)**
    ```bash
    python -m venv venv
    # Windows
    ./venv/Scripts/Activate.ps1
    # macOS / Linux
    source venv/bin/activate

3. **Instalar dependências**
    ````bash
    pip install -r requirements.txt

4. **Ajustar .env.local**

    Crie um arquivo na raiz do projeto chamado:        
        
        .env.local

    Exemplo:

        DEBUG=True
        SECRET_KEY=local-secret-key

        CELERY_BROKER_URL=redis://localhost:6379/0
        CELERY_RESULT_BACKEND=redis://localhost:6379/0

Certifique-se de que o Redis esteja rodando localmente na porta 6379.

5. **Rodar Migrations**
    ````bash
    python manage.py migrate
    
6. **Iniciar servidor**
    ```bash
    python manage.py runserver

7. **Iniciar workers do Celery**
    ```bash
    celery -A settings worker -l info -Q light_queue


## 🐳 Como rodar o projeto (container)

> O ambiente em container utiliza automaticamente o arquivo .env.

1. **Clonar repositório**
    ````bash
    git clone https://github.com/nicolas-aires-dev/Url_Shortener.git
    cd Url_Shortener

2. **Criar arquivo .env**
    ````bash
    DEBUG=False
    SECRET_KEY=docker-secret-key

    CELERY_BROKER_URL=redis://redis:6379/0
    CELERY_RESULT_BACKEND=redis://redis:6379/0
>No Docker, redis é o nome do serviço definido no docker-compose.yml.

3. **Subir os containers**
    ````bash
    docker compose up --build
    ````

    A aplicação estará disponível em:
    ````bash
    http://localhost:8000
    ````
## ⚙️ Configuração de Ambiente (.env)
O projeto utiliza django-environ para separar configurações por ambiente.

- 🔄 Comportamento padrão
- 🖥 Desenvolvimento local → utiliza .env.local
- 🐳 Docker → utiliza .env

Isso permite manter configurações diferentes para cada contexto sem alterar o código.

---

## 🧪 Testes e Postman

Você pode testar a API usando a coleção do Postman incluída na pasta docs/postman. Basta importar o arquivo no Postman e executar as requisições com suas variáveis de ambiente configuradas.

## 🛡️ Autenticação e Segurança (em breve)

Ainda não há autenticação implementada, mas está nos planos:

- ✅ JWT (JSON Web Tokens) para proteger endpoints
- 🔐 Controle de acesso baseado em usuário

Se quiser contribuir com isso, fique à vontade! 🙌

## 🚧 Melhorias Futuras
- ✅ Integrar Redis como mensagem broker principal
- 📦 Dockerizar a aplicação para ambiente de desenvolvimento/produção
- 🔑 Adicionar autenticação JWT
- 📊 Monitoramento de tarefas Celery
- 📈 Suporte multi-worker para alta carga
    
## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias 💡.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.