FROM python:3.9-slim
WORKDIR /app
COPY server.py .
COPY index.html .
EXPOSE 8000
CMD ["python","server.py"]
