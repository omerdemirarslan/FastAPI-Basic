FROM python:3.9


RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

RUN pip install --upgrade pip

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY entrypoint.sh /entrypoint-sh

RUN sed -i 's/\r$//g' /entrypoint-sh

RUN chmod +x /entrypoint-sh

COPY start.sh /start-sh

RUN sed -i 's/\r$//g' /start-sh

RUN chmod +x /start-sh

# copy application code to WORKDIR
COPY . /app

ENTRYPOINT ["/entrypoint-sh"]