#/bin/bash
# pipenv shell
# uvicorn main:app --host 0.0.0.0 --port 80


#"${UID}:$(cut -d: -f3 < <(getent group docker))"

# docker image remove --force synthetic-data-api && docker-compose up

docker-compose up