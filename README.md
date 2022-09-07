# Data engineering project: data extraction to analysis

# Running the project

## Prerequisites

1. [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/) v1.27.0
2. [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Clone the repo 

```bash
git clone https://github.com/mwacinski/pizzeria-el-analytics.git
```

## Spin up

In your project directory run the following command.
```bash
docker-compose up --build -d
docker ps
```

Wait for about a minute. You can log into

1. Airflow UI at [http://localhost:8080/](http://localhost:8080/)
2. Metabase UI at [http://localhost:3001/](http://localhost:3001/). Use the following credentials

```bash
username: mikey@mail.com
password: !@#password123
```

## Tear down

```bash
docker-compose down --v
```
