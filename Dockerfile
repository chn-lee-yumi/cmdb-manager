FROM python:3-alpine
WORKDIR /src
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn","cmdb_manager.wsgi"]