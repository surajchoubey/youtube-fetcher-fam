FROM python:3.9-slim

# Install curl and Node.js
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    apt-get install -y npm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN npm -v

RUN npm install

RUN npm run build

EXPOSE 5001

CMD ["python3", "index.py"]
