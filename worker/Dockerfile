FROM python:3.11.3

# フォントのインストール
RUN apt update && apt install -y fonts-ipaexfont-gothic

# ライブラリのインストール
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

# アプリケーションの実行
COPY . /code/
ENTRYPOINT /code/docker/entrypoint.sh
