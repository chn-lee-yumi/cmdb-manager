FROM python:3
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn","cmdb_manager.wsgi"]