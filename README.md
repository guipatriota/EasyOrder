<!-- Área do Banner -->
<div align="center" style="background-color: white; max-width: 100%;">
  <img alt="BANNER com título: DevOps e Integração Contínua" title="Banner_DevOps" src=".readme_docs/Banner_Github_DevOps.png" width="100%" />
</div>

<!-- Título e breve descrição do repositório -->
<div align="center"><h1>Estudo de DevOps: EasyOrder</h1><p><b>Exemplo de projeto em Python com aplicação de ferramentas DevOps para estudos</b></p></div>

<!-- Ícones ou links das tecnologias usadas -->
<p align="center">
  <a href="https://www.atlassian.com/software/jira" title="Jira"><img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Jira_Logo.svg" alt="Jira" width="65px" height="21px"></a>
  +
  <a href="https://code.visualstudio.com" title="VSCode"><img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" alt="VSCode" width="35px" height="21px"></a>
  +
  <a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="35px" height="21px"></a>
  +
  <a href="https://fastapi.tiangolo.com/" title="FastAPI"><img src="https://raw.githubusercontent.com/fastapi/fastapi/refs/heads/master/docs/en/docs/img/logo-margin/logo-teal.svg" alt="FastAPI" height="31px" style="vertical-align: bottom; margin-top: 30px;"></a>
  +
  <a href="https://www.github.com/" title="GitHub" 
   style="display: inline-flex; align-items: center; justify-content: center; 
          width: 28px; height: 28px; border-radius: 0%; background-color: white;">
    <img 
      src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" 
      alt="GitHub" 
      style="width: 28px; height: 28px;"
    >
  </a>
  +
  <a href="https://www.docker.com/" title="Docker"><img src="https://i0.wp.com/blog.kmsigma.com/wp-content/uploads/2025/07/docker-mark-blue-scaled.png" alt="Docker" height="21px"></a>
  +
  <a href="https://www.aws.com/" title="AWS" 
   style="display: inline-flex; align-items: center; justify-content: center; 
          width: 28px; height: 28px; border-radius: 0%; background-color: white;">
    <img 
      src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" 
      alt="AWS" 
      style="width: 28px; height: 28px;"
    >
  </a>
  +
  <a href="https://aws.amazon.com/pt/cdk/" title="AWS CDK"><img src="https://avatars.githubusercontent.com/u/90621382?s=280&v=4" alt="AWS CDK" height="28px"></a>
  +
  <a href="https://aws.amazon.com/pt/ecs/" title="AWS ECS"><img src="https://images.icon-icons.com/2699/PNG/512/amazon_ecs_logo_icon_168660.png" alt="AWS ECS" height="28px"></a>
  +
  <a href="https://github.com/Supervisor/supervisor" title="Supervisor"><img src="https://raw.githubusercontent.com/Supervisor/supervisor/364e2bfa082960fe85a56392d7eaa2701533b7b4/docs/.static/logo_hi.gif" alt="Supervisor" height="28px"></a>
  +
  <a href="https://aws.amazon.com/pt/cloudwatch/" title="AWS CloudWatch"><img src="https://cdn.freebiesupply.com/logos/large/2x/aws-cloudwatch-logo-svg-vector.svg" alt="AWS CloudWatch" height="28px"></a>
</p>

<!-- Escudos de licença e contador de contribuidores -->
<p align="center">
  <a href="https://github.com/guipatriota/EasyOrder/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/guipatriota/EasyOrder?color=%237159c1&logoColor=%237159c1&style=flat" alt="Contributors">
  </a>
  <a href="https://opensource.org/license/gpl-3-0">
    <img src="https://img.shields.io/github/license/guipatriota/EasyOrder?color=%23BD0000" alt="License">
  </a>
</p>
<p align="center">
  <a>
    <img src="https://img.shields.io/github/actions/workflow/status/guipatriota/EasyOrder/ci.yml?branch=main" alt="Build Status">
  </a>
  <a>
    <img src="https://img.shields.io/github/deployments/guipatriota/EasyOrder/production?label=deploy" alt="Deploy">
  </a>
  <a href="https://github.com/guipatriota/EasyOrder/releases">
    <img src="https://img.shields.io/github/release/guipatriota/EasyOrder?label=release" alt="Release">
  </a>
  <a>
    <img src="https://img.shields.io/badge/python-3.12-blue.svg" alt="Python">
  </a>
  <a>
    <img src="https://img.shields.io/badge/docker-ready-blue" alt="Docker">
  </a>
</p>

<!-- Descrição do repositório e demais dados -->
## Descrição

**EasyOrder** é um sistema de exemplo para gerenciamento de pedidos online, desenvolvido com **FastAPI** e estruturado para seguir boas práticas e ilustrar o ciclo completo **DevOps**, passando por **Plan, Develop, Build, Test, Release, Deploy, Operações e Monitoramento**.

## Professor

| [<img src="https://avatars3.githubusercontent.com/u/60905310?s=460&v=4" width="75px;"/>](https://github.com/guipatriota) |
| :------------------------------------------------------------------------------------------------------------------------: |

| [Prof. Guilherme Patriota](https://github.com/guipatriota)

# 📦 EasyOrder

## 📜 Sumário
- [Visão Geral](#-visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Arquitetura](#-arquitetura)
- [Instalação e Execução](#-instalação-e-execução)
- [Testes](#-testes)
- [CI/CD](#-cicd)
- [Pre-commit](#-pre-commit)
- [Deploy](#-deploy)
- [Documentação](#-documentação)
- [Capturas de Tela](#-capturas-de-tela)
- [Estudo Sobre o Ciclo DevOps](#-estudo-sobre-o-ciclo-devops)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 📖 Visão Geral
O **EasyOrder** foi criado como parte de um projeto de ensino para ilustrar:
- **Práticas de DevOps, incluindo CI/CD no GitHub Actions**
- Uso de **FastAPI** para construção de APIs modernas e rápidas
- Estruturação limpa do código com separação de responsabilidades
- Conteinerização com **Docker**
- Testes unitários e de integração com **pytest**
- Desenvolvimento em container utilizando **Dev Containers** do VSCode

---

## 🛠 Tecnologias Utilizadas
- **Gestão de projeto**: Jira
- **Linguagem**: Python 3.12
- **Framework**: FastAPI
- **IDE base**: VSCode
- **Versionamento**: Github
- **Controle de qualidade**: Pré-commit com black, isort, flake8, script personalizado e pytest com code coverage 
- **Testes**: pytest + GitHub Actions
- **Documentação**: sphinx + GitHub Actions + GitHub Pages
- **Containerização**: Docker
- **Dev Container**: VSCode + devcontainer.json
- **CI/CD**: GitHub Actions
- **Banco de Dados**: Em memória (para demonstração, via `memory_db.py`)
- **Infra**: AWS ECS Fargate + CloudWatch via IaC em Python (AWS CDK)
- **Operações**: Supervisor + htop no container
- **Monitoramento**: AWS CloudWatch + Grafana

---

## 🏛️ Arquitetura
```
EasyOrder/
│
├── src/
│   ├── main.py # Ponto de entrada da aplicação
│   ├── db/ # Banco de dados (simulado)
│   ├── models/ # Modelos de dados
│   └── routes/ # Rotas da API
│
├── docs/
│   └── screenshots/ # Prints de tela para documentação
│
├── infra/
│   ├── app.py # AWS CDK em Python para deploy da infraestrutura em nuvem
│   └── easyorder_stack.py # Stack da infra utilizada
│
├── tests/ # Testes unitários e de integração
├── Dockerfile # Configuração de imagem Docker
├── .github/
│   └── workflows/
│     ├── ci.yml # Pipeline CI
│     ├── cd.yml # Pipeline CD
│     └── docs.yml # Pipeline CD de documentação
│
├── .flake8 # Configuração do linter
├── pyproject.toml # Configurações do projeto, do black (formatador de código) e do isort (ordenador de imports)
├── .pre-commit-config.yaml # Configuração das ações pré-commit
├── supervisord.conf # Configuração do supervisor para iniciar serviços automaticamente
├── requirements.txt # Dependências do projeto
└── requirements-dev.txt # Dependências do projeto para desenvolvimento
```
---

## 🚀 Instalação e Execução

### 1️⃣ Pré-requisitos
- **Docker** instalado e rodando
- **Visual Studio Code** instalado
- Extensão **Dev Containers** instalada ([VSCode Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers))

### 2️⃣ Clonar o repositório
```bash
git clone https://github.com/guipatriota/EasyOrder.git
cd EasyOrder
```

### 3️⃣ Abrir no Dev Container
1. Abra o projeto no VSCode ou IDE compatível:
```bash
code .
```

2. Pressione `F1` → **Dev Containers: Reopen in Container**
O VSCode irá:
- Construir a imagem a partir do Dockerfile usando o target `dev`. Isto fará:
  - Montagem do workspace dentro do container
  - Instalação de todas as dependências definidas no `requirements.txt` e `requirements-dev.txt`
  - Inicializará o servidor com `uvicorn`

### 4️⃣ Executar a aplicação dentro do container
No terminal integrado do VSCode (já dentro do container):
Obs.: Este comando já deve rodar automaticamente. Faça-o apenas se o servidor da API não estiver funcionando.
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```
A API estará disponível em: `http://127.0.0.1:8000`
A documentação interativa do Swagger: `http://localhost:8000/docs`

---

## 🧪 Testes
```bash
pytest tests/ --maxfail=1 --disable-warnings -v
```
---

## ⚙️ CI/CD
Este projeto já possui pipeline configurado no **GitHub Actions**:
- **Lint**: Executa verificação de atendimento aos padrões de projeto
- **Build**: Executa testes automaticamente a cada push
- **Deploy**: Pode ser configurado para AWS, Heroku ou outros provedores

---

## 🔍 Pre-commit

O **pre-commit** é uma ferramenta que garante que o código siga padrões de qualidade **antes de ser commitado** no Git.  
Ele executa automaticamente uma série de verificações e formatações para manter o projeto consistente e evitar problemas no pipeline.

### 📌 Motivação
- Padronizar código (formatação, imports, estilo)
- Evitar commits com erros de lint ou testes quebrados
- Garantir que todos contribuidores sigam as mesmas regras
- Reduzir falhas no CI/CD

### 📥 Instalação inicial
1. Instale o pre-commit:
```
pip install pre-commit
```

2. Instale os hooks configurados:
```
pre-commit install --hook-type pre-commit --hook-type pre-push
```

3. Para rodar manualmente em todos os arquivos:
```
pre-commit run --all-files
```

### ⚙️ Hooks configurados neste projeto
- **Black** → Formata o código automaticamente.
- **isort** → Organiza imports de forma consistente com o Black.
- **Flake8** (+ plugins) → Detecta problemas de estilo, nomes e boas práticas.
- **check-docstrings-length** → Verifica tamanho de docstrings (script local).
- **pytest com cobertura** (pre-push) → Executa testes e falha se a cobertura for menor que 75%.

⚠️ Se um hook modificar arquivos, o commit será interrompido. Você precisará revisar as alterações, adicioná-las novamente com `git add` e repetir o commit.

---

## 🌐 Deploy
**Link de Deploy**: [https://easyorder.example.com](https://easyorder.example.com)
---

## 📖 Documentação
**Link da Doc**: [https://guipatriota.github.io/EasyOrder/](https://guipatriota.github.io/EasyOrder/)
1. Para abrir servidor da documentação:
```
python -m http.server 8001 --directory docs/_build/html
```

2. Para compilar documentação atualizada:
```
pip install -r docs/requirements-docs.txt
pip install -e .
python -m sphinx.ext.apidoc -f -o docs/api src
sphinx-build -b html docs docs/_build/html 
```
---

## 🖼 Captura de Tela

![Tela Inicial](docs/screenshots/home.jpg)  

---

## 👨‍🏫 Estudo Sobre o Ciclo DevOps

### 📚 Ciclo DevOps no EasyOrder

#### 1️⃣ Plan – Planejamento
- **Ferramenta:** Jira  
- Usado para organizar backlog, sprints e tarefas do projeto.  

#### 2️⃣ Develop – Desenvolvimento
- **Ferramentas:** VSCode + GitHub  
- Commits automatizados com hooks de pré-commit.

#### 3️⃣ Build – Construção
- **Ferramenta:** Docker + DevContainer VSCode  

#### 4️⃣ Test – Testes
- **Ferramenta:** pytest + GitHub Actions  

#### 5️⃣ Release – Versionamento
- **Ferramenta:** GitHub Tags  

#### 6️⃣ Deploy – Publicação
- **Ferramenta:** GitHub Actions + AWS CDK + ECS Fargate  

#### 7️⃣ Operações
- **Ferramentas:** Supervisor + Dockerfile  

#### 8️⃣ Monitoramento
- **Ferramenta:** AWS CloudWatch + Grafana

---

### 📚 Guia de Estudo DevOps — EasyOrder

Este projeto foi expandido para servir como **guia prático de DevOps**, cobrindo todas as fases do ciclo e listando **comandos úteis** para cada ferramenta.

#### 1️⃣ Plan — Jira
Ferramenta usada para planejamento e organização.
- **Dica**: utilize boards no Jira para organizar as fases do projeto.
---
---
#### 2️⃣ Develop — VSCode + GitHub + Pre-commit
Ambiente de desenvolvimento com automação de qualidade de código.
```bash
# Executar formatação automática
black .

# Organizar imports
isort .

# Rodar linter
flake8 .

# Verificar docstrings
python scripts/check_docstrings.py

# Rodar pre-commit manualmente
pre-commit run --all-files
```
---
---
#### 3️⃣ Build — Docker + Dev Containers
Criação e gerenciamento de containers de desenvolvimento.
```bash
# Construir imagem do devcontainer
docker build -t easyorder-dev --target dev .

# Abrir container no VSCode
Dev Containers: Reopen in Container
```
---
---
#### 4️⃣ Test — pytest + GitHub Actions
Automatização de testes unitários e de integração.
```bash
# Rodar testes localmente
pytest tests/ -v --disable-warnings --maxfail=1
```
---
---
#### 5️⃣ Release — GitHub Tags
Versionamento semântico.
```bash
# Criar nova tag de release
git tag v1.0.0
git push origin v1.0.0
```
---
---

#### 6️⃣ Deploy — GitHub Actions + AWS CDK + ECS/ECR
Provisionamento de infraestrutura e deploy automático.
```bash
# Síntese da stack CDK
cd infra
cdk synth -c imageTag=v1.0.0

# Deploy manual
cdk deploy EasyOrderStack --require-approval never
```
---
---
#### 7️⃣ Operações — Supervisor + Systemd + Logs
##### Supervisor (para containers - rodar com sudo ou root)
```bash
# Verificar status dos serviços
supervisorctl status

# Iniciar/parar/reiniciar serviço
supervisorctl start fastapi
supervisorctl stop fastapi
supervisorctl restart fastapi

# Ver logs em tempo real
supervisorctl tail -f fastapi
supervisorctl tail -f fastapi stderr
```

##### Systemd (para servidores Linux - rodar com sudo ou root)
```bash
# Gerenciar serviços
systemctl start fastapi
systemctl stop fastapi
systemctl restart fastapi
systemctl status fastapi

# Habilitar serviço na inicialização
systemctl enable fastapi
systemctl disable fastapi

# Recarregar configs
systemctl daemon-reload
```

##### Diagnóstico do sistema
```bash
# Monitorar uso de CPU, memória, processos
htop

# Visualizar portas e conexões
ss -tulnp
```
---
---
#### 8️⃣ Monitoramento — AWS CloudWatch + Grafana
- **CloudWatch**: coleta logs do Supervisor e Systemd para monitoramento.
- **Grafana**: conecta-se ao CloudWatch para visualização em dashboards.
```bash
# Enviar logs para CloudWatch (exemplo)
aws logs create-log-group --log-group-name EasyOrderLogs
aws logs create-log-stream --log-group-name EasyOrderLogs --log-stream-name FastAPI
aws logs put-log-events --log-group-name EasyOrderLogs --log-stream-name FastAPI --log-events file://logs.json
```
---

## 🤝 Contribuindo
Contribuições são bem-vindas!  
Para contribuir:
1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Envie um push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

## 📄 Licença
Este projeto está licenciado sob a [GNU General Public License, versão 3](LICENSE).

