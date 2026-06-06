FROM node:18.20.5-alpine3.21 AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm config set registry https://mirrors.huaweicloud.com/repository/npm/
RUN npm install
COPY . .
ARG VUE_ENV
ARG VITE_APP_ENV=master
ARG VITE_APP_BASE_URL=/api
ARG VITE_APP_SOCKET_URL=/api/web/socket?
ARG VITE_APP_MINIO_URL=/minio
ARG VITE_APP_MCP_SERVER_NAME=mango-test-platform
ARG VITE_IS_INDEX_WINDOW=false
ENV VUE_ENV=${VUE_ENV}
ENV VITE_APP_ENV=${VITE_APP_ENV}
ENV VITE_APP_BASE_URL=${VITE_APP_BASE_URL}
ENV VITE_APP_SOCKET_URL=${VITE_APP_SOCKET_URL}
ENV VITE_APP_MINIO_URL=${VITE_APP_MINIO_URL}
ENV VITE_APP_MCP_SERVER_NAME=${VITE_APP_MCP_SERVER_NAME}
ENV VITE_IS_INDEX_WINDOW=${VITE_IS_INDEX_WINDOW}
ENV NODE_OPTIONS=--max-old-space-size=4096
RUN npm run build:${VUE_ENV}

FROM nginx:stable-alpine3.20-perl AS production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
