# Use Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN apt-get update -y && pip install -r requirements.txt

# Expose Azure port
EXPOSE 8000

# Run Streamlit using the port assigned by Azure
CMD ["bash", "-c", "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"]
