FROM node:18-alpine AS base
WORKDIR /usr/src/app
COPY package.json package-lock.json* ./
RUN npm install --production
COPY src ./src

# Default to production; override at build/run time
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

EXPOSE 3000
CMD ["node", "src/index.js"]

