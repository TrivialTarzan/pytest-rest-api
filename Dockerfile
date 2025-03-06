FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# copy the project into the container
COPY . . 
CMD ["pytest", "-v"]
