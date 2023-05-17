# conveni-pdf-example

## これは何?

コンビニで住民票を印刷しようとしたときに誤交付しないための仕組みを実現したものです。

## 起動方法

```sh
docker-compose up --build -d
```

http://localhost:5173 でアクセスしてください。

## 構成要素

- api: API
  - request/名前: 住民票を発行する。住民票のPDFが入るURLを返す
  - get/ファイル名: 住民票のPDFを返す。まだ作成途中の時は404。
- database: PostgreSQL
- frontend: フロントエンド
- task-queue: apiからworkerに渡すためのキュー
- terrible-api: 謎のAPI
  - IF01: 個人情報(ダミー)をXMLで返す
- worker: PDFを作成するワーカー

## 制限事項

- セキュリティは考慮していません(誤交付を避けるのがメインなので)
- エラー処理を考えていません。
- ワーカーは同時に動きません。

## ライセンス

MIT
