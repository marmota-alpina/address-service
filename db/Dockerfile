# Estágio de construção inicial usando Alpine Linux para preparar o arquivo SQL de backup
FROM alpine:3.7 as source

RUN apk add --no-cache git

WORKDIR /app

# Clonar o repositório do endereço do serviço
RUN git clone https://github.com/marmota-alpina/address_service.git

# Verificar se o diretório de backups existe
RUN ls -la /app/address_service/db/backups

# Concatenar arquivos de backup (se o diretório existir)
RUN cd /app/address_service/db/backups && cat part_* > /app/002_backup.sql

# Estágio final usando a imagem oficial do PostgreSQL
FROM postgres:latest

# Copiar o arquivo SQL de backup do estágio de construção inicial para o diretório de inicialização do PostgreSQL
COPY --from=source /app/002_backup.sql /docker-entrypoint-initdb.d/002_backup.sql
