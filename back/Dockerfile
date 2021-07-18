FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /back


RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

COPY . .
