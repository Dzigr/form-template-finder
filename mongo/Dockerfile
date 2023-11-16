FROM mongo

WORKDIR /mongo

COPY seed/ ./seed/
COPY init.sh .

RUN chmod +x init.sh

CMD ["sh", "-c", "./init.sh"]
