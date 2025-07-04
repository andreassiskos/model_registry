FROM python:3.10

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs models

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
