FROM node:22-alpine
WORKDIR /app
COPY apps/frontend/package.json apps/frontend/package-lock.json* ./
RUN npm install
COPY apps/frontend .
CMD ["npm", "run", "dev"]
