# This project is inspired from my github repo: https://github.com/abdellatifThabet/flask-clean-project-arch-boilerplate


This dockerized flask app has two Rest services:
* store a tiktok user in the database based on data retrieved from tiktok using its username.
* Get a user infos by username or id

Theses services were implemented with the help of [flask] framework and its ecosystem:

* [flask-restx](https://flask-restx.readthedocs.io/en/latest/swagger.html) to auto-generate swagger definition from
  python code.
* [sqlalchemy](https://www.sqlalchemy.org/) ORM for the db connect, and it assists to compose sql queries.
* [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) to connect flask app with
* [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) to auto-generate db migration file.
* [marshmallow] (https://marshmallow.readthedocs.io/en/stable/) for inputs validators and serializers

### Run the server

To run flask server you need docker and docker-compose in your machine, after running the below command try to access to
swagger UI via http://0.0.0.0:5000/api/


```shell
make run
```
If you run the app the very first time you need to generate a db migration file
using : make db-init


```shell
make stop
```
Note: it's recommended to stop all the running containers, sometime other services may take the same port number.

### Generate db migration file

To generate new migration file from the changes in `db_models` you need to run the below command line with a meaningful
message.

```shell
make db-migrate
```

[alembic](https://alembic.sqlalchemy.org/en/latest/) together
with [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
will auto-generate a migration file with the db changes, you will find it under `migrations/versions` prefixed with the datetime of the generation.

Note that each time you run the project using `make run` an upgrade of the migrations will be applied in order to update the db schema.


## TikTok library keeps on giving errors after all, uncomment the call in create_user to see the last given error :(