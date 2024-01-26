# Stage 1: Build the application
FROM node:14 as builder
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .

# Stage 2: Create the final image
FROM node:14-alpine
WORKDIR /app
COPY --from=builder /app /app
CMD ["node", "app.js"]
