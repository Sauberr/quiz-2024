FROM python:3.12.2

RUN apt update && apt install -y supervisor && rm -rf /var/lib/apt/lists/*

RUN apt update
RUN mkdir /quizes

WORKDIR /quizes

COPY ./src ./src
COPY ./commands ./commands

COPY ./requirements.txt ./requirements.txt

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["supervisord", "-n"]