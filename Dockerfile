# ---------------------------
# Stage 1: Dev Environment
# ---------------------------
FROM python:3.12-slim AS dev

# Instalar pacotes úteis para desenvolvimento
RUN apt-get update && apt-get install -y \
    git zsh sudo curl vim nodejs npm \
    && useradd -ms /bin/zsh vscode \
    && echo "vscode ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && sudo ./aws/install \
    && npm install -g aws-cdk@2 \
    && cdk --version \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces/EasyOrder

# Instala dependências
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copia o código
COPY . .

# Variáveis para FastAPI / Uvicorn
EXPOSE 8000
ENV PYTHONUNBUFFERED=1

# Atenção! CMD é ignorado ao usarmos o devcontainer do VSCODE!
# Esse comando roda no CI/CD e em produção, apenas.
# Para que o CMD seja executado no devcontainer, adicione ao devcontainer.json as seguintes linhas:
# "runArgs": ["--init"],
# "overrideCommand": false,
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ---------------------------
# Stage 2: Production
# ---------------------------
FROM python:3.12-slim AS prod

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

COPY . .

RUN pip install -r requirements-dev.txt



