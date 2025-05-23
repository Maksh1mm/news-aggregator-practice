# 1. Базовий образ Python
FROM python:3.13-slim

# 2. Встановлюємо робочу директорію
WORKDIR /app

# 3. Копіюємо залежності
COPY requirements.txt .

# 4. Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо увесь бекенд-код (має бути у папці backend/)
COPY backend/ ./    # Весь бекенд-код

# 6. Копіюємо config.py (наприклад, створений автоматично)
COPY config.py ./   # Якщо config.py генерується в корені проєкту

# 7. Копіюємо .env (якщо існує)
COPY .env ./        # Для секретів або змінних середовища

# 8. Відкриваємо порт
EXPOSE 8000

# 9. Запускаємо uvicorn (FastAPI або подібний фреймворк)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
