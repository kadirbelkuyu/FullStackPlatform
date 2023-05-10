FROM postgres:15

# Çalışma dizinini ayarla
WORKDIR /docker-entrypoint-initdb.d/

# init.sql dosyasını konteynera kopyala
COPY ./init.sql .

# PostgreSQL hizmetini başlat
CMD ["postgres"]
