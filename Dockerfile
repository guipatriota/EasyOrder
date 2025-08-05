# FROM python:3.12-slim
FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Atenção! CMD é ignorado ao usarmos o devcontainer do VSCODE!
# Esse comando roda no CI/CD e em produção, apenas.
# Para que o CMD seja executado no devcontainer, adicione ao devcontainer.json as seguintes linhas:
# "runArgs": ["--init"],
# "overrideCommand": false,
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
