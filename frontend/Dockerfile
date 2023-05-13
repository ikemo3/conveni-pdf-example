# ビルド用コンテナ
FROM node:20.1.0 as build

WORKDIR /app

# ライブラリのインストール
COPY package.json pnpm-lock.yaml ./
RUN npm install -g pnpm
RUN pnpm install

ENTRYPOINT /app/docker/entrypoint.sh
