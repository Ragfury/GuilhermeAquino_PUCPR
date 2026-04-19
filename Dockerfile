FROM python:3.13.13-alpine3.23

WORKDIR /user/src/app

COPY requirements.txt ./

COPY . .

CMD ["python", "./main.py"]