FROM python:3.8

WORKDIR /app
COPY server.py .
RUN pip install Flask
RUN pip install requests

CMD ["python", "server.py"]
