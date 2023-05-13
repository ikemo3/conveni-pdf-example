import json
import os
from datetime import datetime

import psycopg2
import redis
from fastapi import FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, PlainTextResponse

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def build_pdf_url(filename):
    return f"http://localhost:8000/get/{filename}"


def build_pdf_filename(id):
    """idを使った重複しないファイル名"""
    now = datetime.now()
    formatted_now = now.strftime("%Y%m%d%H%M%S")
    return f"{formatted_now}_{id}.pdf"


@app.get("/request/{name}", response_class=PlainTextResponse)
async def request(
    name: str = Path(title="名前"),
):
    r = redis.Redis(host="task-queue")

    info = dict(
        host="database",
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DB"),
    )
    with psycopg2.connect(**info) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT NEXTVAL('request_id')")
            id = cursor.fetchone()[0]
            pdf_filename = build_pdf_filename(id)
            pdf_url = build_pdf_url(pdf_filename)
            request_data = json.dumps(dict(name=name, filename=pdf_filename))

            cursor.execute(
                "INSERT INTO request (id, pdf_url, request_data) values (%s, %s, %s)", (id, pdf_url, request_data)
            )

    r.rpush("task", request_data)
    return pdf_url


@app.get("/get/{filename}", response_class=FileResponse)
async def read_file(filename: str):
    file_path = f"/shared/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return file_path
