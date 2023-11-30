FROM python:3.8-slim
WORKDIR /app
COPY produce.py .
COPY requirements.txt .
COPY producepod.yaml .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["python", "produce.py"]
