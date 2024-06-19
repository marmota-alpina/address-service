#!/bin/bash
DB_USER=$POSTGRES_USER
DB_NAME=$POSTGRES_DB
# Definir os diretórios de backup e restauração
BACKUPS_DIR=/var/tmp/backups
RESTORE_DIR=/docker-entrypoint-initdb.d

#Checar se o diretório de backup existe
if [ ! -d $BACKUPS_DIR ]; then
    echo "Diretório de backup não encontrado"
    exit 1
fi
# Checar se o diretório de restauração existe
if [ ! -d $RESTORE_DIR ]; then
    echo "Diretório de restauração não encontrado"
    exit 1
fi
# Checar se o diretório de backup contém arquivos
if [ ! "$(ls -A $BACKUPS_DIR)" ]; then
    echo "Diretório de backup está vazio"
    exit 1
fi
# Combinar as partes do backup em um único arquivo
cat $BACKUPS_DIR/part_* > $RESTORE_DIR/002_backup.sql

# Executar o script de restauração no databse address_db
psql -U "$DB_USER" -d "$DB_NAME" -f $RESTORE_DIR/002_backup.sql

# Remover o arquivo de backup
rm $RESTORE_DIR/002_backup.sql