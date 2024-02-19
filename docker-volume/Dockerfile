FROM alpine:3.14

VOLUME /var/www/html

RUN apk --no-cache add nginx
CMD ["nginx", "-g", "daemon off;"]

# comando para acessar (pode ser qualquer porta disponivel!) sudo docker run -d -p 83:83 -v /var/www/html:/var/www/html docker-vlexit