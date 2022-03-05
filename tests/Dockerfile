FROM python:3.8.10-buster
CMD ["/usr/local/bin/python", "-m", "pip", "install", "--upgrade", "pip"]
WORKDIR /usr/src
RUN apt -yq update
RUN apt -yq upgrade
RUN pip install poetry
COPY pyproject.toml poetry.lock .behaverc ./
COPY acceptance ./
RUN python -m venv /venv
RUN poetry install -vv
CMD ["cd", "tests"]
CMD ["poetry", "run", "behave"]
