FROM python:3 
# pega imagem do python
COPY . /app
# seta a pasta app/ cria e seta as configurações/imagem do Python
USER root
# define que o usuario tem permissoes root
RUN apt-get -y update && apt-get install -y curl gnupg
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN exit
RUN apt-get -y update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18
RUN apt-get update && apt-get install build-essential unixodbc-dev -y
RUN pip install pyodbc && pip install mysql-connector-python
RUN pip install psutil
WORKDIR /app
CMD python3 apipython.py
# valida todos os passos utilizando a imagem e roda o arquivo