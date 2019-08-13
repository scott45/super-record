FROM python:3.7-alpine

LABEL application='superrecord'

LABEL maintainer='Anyama Richard'

WORKDIR /app

# update system and install dependencies
RUN apk update && apk add --no-cache bash \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps \
    && pip install pipenv 

#copy source code to app dir
COPY src/ /app/

ADD scripts/start.sh /app/

# add execute permission
RUN chmod +x start.sh

# install app dependencies from the pipfile
RUN pipenv install --skip-lock --system

CMD bash -c "source start.sh"
