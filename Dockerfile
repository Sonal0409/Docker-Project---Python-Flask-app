
FROM python:3.12-slim
 
# Set working directory
WORKDIR /app
 
# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy app code
COPY app.py .
 
# Create volume mount point
VOLUME ["/data"]
 
# Expose port
EXPOSE 5000
 
# Run app
CMD ["python", "app.py"]

