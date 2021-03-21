FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /src
COPY requirements.txt /src/
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
RUN pip install -r requirements.txt
COPY . /src/