# ---------------------------
# Stage 1: Dev Environment
# ---------------------------
FROM python:3.12-slim AS dev

# ---- Volta "system-wide" ----
# Instalaremos o Volta em /usr/local/volta (acessível por todos)
# Variáveis do Volta: onde será instalado e exposto no PATH
ENV VOLTA_HOME=/usr/local/volta
ENV PATH=$VOLTA_HOME/bin:$PATH

# Variáveis para FastAPI / Uvicorn
ENV PYTHONUNBUFFERED=1

# Cria pasta de logs do supervisor
RUN mkdir -p /var/log/supervisor

# Pacotes base (Instala o Supervisor para time de Operações)
RUN apt-get update && apt-get install -y \
    curl unzip ca-certificates git zsh sudo vim supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala AWS CLI v2
RUN curl -fsSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws \
    && aws --version

#-------------------------------------
# Instalação do AWS CDK:
#   - usa Volta + Node LTS
#-------------------------------------
# Instala Volta no diretório "system-wide"
# (usamos --skip-setup para não tocar nos dotfiles;
# configura PATH global manualmente)
RUN mkdir -p "$VOLTA_HOME" \
    && curl -fsSL https://get.volta.sh | bash -s -- --skip-setup \
    && volta --version \
    # Garante que todos os usuários conseguem ler/executar
    && chmod -R a+rX "$VOLTA_HOME" \
    # Exporta VOLTA_HOME/ PATH para todos os shells de login
    && printf 'export VOLTA_HOME=%s\nexport PATH=$VOLTA_HOME/bin:$PATH\n' "$VOLTA_HOME" > /etc/profile.d/volta.sh \
    && echo 'export VOLTA_HOME=/usr/local/volta' >> /etc/zsh/zshrc \
    && echo 'export PATH=$VOLTA_HOME/bin:$PATH'  >> /etc/zsh/zshrc

# Instala CDK
# usando Node LTS instalado pelo Volta (visível a todos)
RUN volta install node \
    && node --version && npm --version \
    && npm install -g aws-cdk@2 \
    && cdk --version \
    # Symlinks para garantir acesso mesmo sem shell de login (serviços/CI)
    && ln -sf "$VOLTA_HOME/bin/volta" /usr/local/bin/volta \
    && ln -sf "$VOLTA_HOME/bin/node"  /usr/local/bin/node  \
    && ln -sf "$VOLTA_HOME/bin/npm"   /usr/local/bin/npm   \
    && ln -sf "$VOLTA_HOME/bin/npx"   /usr/local/bin/npx   \
    && ln -sf "$VOLTA_HOME/bin/cdk"   /usr/local/bin/cdk

# Usuário de desenvolvimento
RUN useradd -ms /bin/zsh vscode \
    && echo "vscode ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /workspaces/EasyOrder

# Instala dependências
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copia o código
COPY . .

# Supervisor config
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Expondo a porta 8000 para o uvicorn, servidor do fastapi
EXPOSE 8000

# Atenção! CMD é ignorado ao usarmos o devcontainer do VSCODE!
# Esse comando roda no CI/CD e em produção, apenas.
# Para que o CMD seja executado no devcontainer, adicione ao devcontainer.json as seguintes linhas:
#   "runArgs": ["--init"],
#   "overrideCommand": false,
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Supervisor iniciará o uvicorn:
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# ---------------------------
# Stage 2: Production
# ---------------------------
FROM python:3.12-slim AS prod

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copia dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia apenas código necessário para produção
COPY src ./src

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------------------------
# Stage 3: Test
# ---------------------------
FROM prod AS test

# Inclui código completo e deps de dev para testes/linters
COPY . .
RUN pip install -r requirements-dev.txt



