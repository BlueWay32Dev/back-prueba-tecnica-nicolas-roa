# back-prueba-tecnica-nicolas-roa

prueba-tecnica-NicoRoa-backend
Se realizo un api con Python 3.11 bajo el framework de FastAPI y base de datos MYSQL, esta api se creo bajo el requerimiento de un sistema TODOLIST

La api cuenta con su documentación en Swagger

Para ejecutar la app se debe primero modificar el archivo database.py para incluir el nombre de usuario y pass del usuario MYSQL luego instalar

pip install uvicorn sqlalchemy pydantic mysql-connector-python pip install "fastapi[all]" pip install --upgrade sqlalchemy-utils pip install mysqlclient

uvicorn main:app --reload

Docs: http://localhost:8000/docs

Api: http://localhost:8080/tasks
