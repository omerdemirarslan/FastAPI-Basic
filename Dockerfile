FROM python:3.9

LABEL maintainer="omerdemirarsln@gmail.com"

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 5555

CMD ["python", "main.py", "--reload=True"]
