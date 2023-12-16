FROM python:3.8

WORKDIR /app
COPY worker.py .
RUN pip install Flask

CMD ["python", "worker.py"]
