FROM python:3.11-alpine

COPY requirements.txt ./requirements.txt

WORKDIR /.

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "./main.py", "runserver"] 