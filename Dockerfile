#syntax=docker/dockerfile:1

FROM python

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "setup:app", "--host", "0.0.0.0", "--reload"]

