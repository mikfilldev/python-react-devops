FROM node:18-alpine

WORKDIR /app

COPY .env package*.json .

RUN npm install

RUN npm install -g serve

COPY ./build.sh .

RUN chmod +x ./build.sh
