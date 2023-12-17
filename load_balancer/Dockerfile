FROM python:3.8

WORKDIR /app
COPY load_balancer.py .
RUN pip install Flask
RUN pip install requests

CMD ["python", "load_balancer.py"]
