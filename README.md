# 🔗 URL Shortener API

Serviço de encurtamento de URLs desenvolvido em Python, com foco em organização de responsabilidades e preparação para processamento assíncrono.

O projeto utiliza Celery para estruturação de tarefas em background, com evolução planejada para uso de Redis como broker de filas e Docker para containerização da aplicação.

---

## 🚀 Funcionalidades

- Encurtamento de URLs
- Redirecionamento a partir da URL encurtada
- Estruturação de tarefas assíncronas com Celery
- Organização em camadas (views, services, tasks)
- Base preparada para escalabilidade

---

## 🧠 Arquitetura

O projeto segue uma separação clara de responsabilidades:

- **Views:** recebem e tratam requisições HTTP
- **Services:** concentram regras de negócio
- **Tasks:** responsáveis por processamento assíncrono (Celery)

Essa abordagem permite desacoplamento e facilita a evolução para execução em background com filas.

---

## ⚙️ Tecnologias utilizadas

- Python
- Django / Django REST Framework *(ajustar se necessário)*
- Celery
- sqlite3 *(ou outro banco que você estiver usando)*
- Docker *(planejado)*

---

## 🔄 Processamento assíncrono (em evolução)

O projeto utiliza Celery para definição de tarefas assíncronas.

Atualmente, as tasks estão em desenvolvimento para execução em background. A evolução planejada inclui:

- Integração com Redis como broker de filas
- Execução desacoplada via workers
- Processamento de tarefas em larga escala

---

## 📦 Próximos passos

- [ ] Integração com Redis (message broker)
- [ ] Containerização com Docker
- [ ] Autenticação (JWT)
- [ ] Monitoramento de tarefas
- [ ] Escalabilidade com múltiplos workers

---

## 🔐 Autenticação (planejado)

A API ainda não possui autenticação implementada.

Está planejada a adição de autenticação baseada em JWT para controle de acesso e segurança dos endpoints.

---

## 🧪 Testes da API

A API pode ser testada utilizando a coleção do Postman incluída no repositório.

---

## 📂 Como rodar o projeto

```bash
# Clonar repositório
git clone https://github.com/nicolas-aires-dev/Url_Shortener

# Entrar na pasta
cd Url_Shortener

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Windows:
./venv/Scripts/Activate.ps1
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar projeto
python manage.py runserver