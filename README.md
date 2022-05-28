# fastapi-clean-architecture

## description
Base FastAPI project for applying general RestAPI Application cases.

## concept
1. Minimal functionality.
2. Convincing architecture.
3. Easy to read.
4. Compatibility.
5. Versatility.

## base models
1. user
2. post [user (1 : n) post]
3. tag [post (n : n) tag]

## integrated with
1. python3.9+
2. fastapi 0.78.0
3. database
   1. MySQL5.7+
   2. Migration with alembic
   3. pytest with real DB
   4. Load with two ways (eager, lazy)
   5. Modeling with schema (1:1, 1:n, n:n)
4. dependency-injector
   1. service-repository pattern
5. JWT authentication
   1. role separation each enpoint
6. deployment
   1. container environment(k8s, docker)
   2. raw WAS(Web Application Server)

## commands
1. db
   1. `alembic upgrade head`: apply every migrations
   2. `alembic downgrade base`: rollback every migrations
2. server
   1. `uvicorn app.main:app --reload`: base
   2. options
      1. host: `--host 0.0.0.0`
      2. port: `--port 8000`

## sample env
```dotenv
ENV=dev
MYSQL_USER=root
MYSQL_PASSWORD=qwer1234
MYSQL_HOST=localhost
MYSQL_PORT=3306
```
