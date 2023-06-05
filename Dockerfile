FROM mcr.microsoft.com/devcontainers/python:0-3.10

WORKDIR /usr/src

COPY requirements.txt ./
COPY python_boilerplate ./python_boilerplate

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "python_boilerplate.main:app", "--host=0.0.0.0", "--port=80"]