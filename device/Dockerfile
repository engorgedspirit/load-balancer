FROM python:3.8

WORKDIR /app
COPY device.py .
RUN pip install Flask
RUN pip install requests

CMD ["python", "device.py"]
