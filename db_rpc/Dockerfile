FROM python:3.8-alpine
RUN apk add --no-cache build-base
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# CMD nameko run rpc --broker amqp://guest:guest@localhost:5672
CMD nameko run rpc --broker amqp://guest:guest@rabbitmq:5672