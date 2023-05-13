FROM python:3.11.3

# ライブラリのインストール
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# アプリケーションの実行
COPY . /code/
ENTRYPOINT /code/docker/entrypoint.sh
