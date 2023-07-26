FROM python:3.11-slim

WORKDIR /opt

COPY requirements.txt /opt/requirements.txt
RUN pip install -r requirements.txt

COPY . /opt

CMD ["python", "main.py"]
