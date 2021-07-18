FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /front
COPY requirements.txt /front/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /front
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]