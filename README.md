senha mongodb express: Username:admin and pw:pass

keyfile para comunicação entre o mongodb principal e a replica

mongodb compass para interface


$ docker volume create vol1

$ docker network create net1

$ docker run -d --network net1 -h mongo --name mongo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret -p 27017:27017 -v vol1/data/db mongo



