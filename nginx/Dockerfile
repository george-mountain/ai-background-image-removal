FROM nginx:latest

LABEL maintainer="georgemountain"

COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80 443

ENTRYPOINT [ "nginx" ]

CMD [ "-g", "daemon off;" ]