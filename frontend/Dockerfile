FROM python:3.10.13-bullseye

LABEL maintainer="georgemountain"

COPY requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]