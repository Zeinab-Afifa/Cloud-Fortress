FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN useradd -m appuser && chown -R appuser /app
USER appuser
EXPOSE 8080
CMD ["python", "app.py"]
