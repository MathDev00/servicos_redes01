#1, Hello Word DockerFile em Python

FROM alpine:3.14

RUN apk add --update python3

COPY teste.py /home

CMD ["python3", "-m", "http.server", "80"]