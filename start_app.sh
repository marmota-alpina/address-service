#!/bin/bash

docker compose down

if [ "$(docker volume ls | grep address_service_postgres_data)" ]; then
    echo "Removendo volume existente"
    docker volume rm address_service_postgres_data
fi

docker compose up -d --build
echo "Aplicação iniciada com sucesso"
exit 0