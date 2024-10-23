FROM python:3.12-slim AS build

ENV PYTHONUNBUFFERED=1

RUN pip install poetry==1.8.3
RUN poetry self add poetry-plugin-export

WORKDIR app

COPY pyproject.toml poetry.lock .

RUN poetry export --format requirements.txt --output requirements.txt --no-interaction


FROM python:3.12-slim AS production

WORKDIR app

COPY --from=build app/requirements.txt .
RUN pip install -r requirements.txt --no-deps
RUN rm requirements.txt

COPY server .

CMD ["fastapi", "run", "--port", "8000", "--host", "0.0.0.0", "--app", "fastapi_app", "server.py"]


FROM production AS development
