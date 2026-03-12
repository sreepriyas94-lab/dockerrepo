FROM python:3.14.2
WORKDIR /Docker
COPY app.py .
CMD ["python3", "app.py"]
