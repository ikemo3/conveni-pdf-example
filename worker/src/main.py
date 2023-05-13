import json
import logging
from json import JSONDecodeError

import redis
from weasyprint import HTML

from converter import convert
from fetcher import fetch

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>住民票</title>
</head>
<body>
    <h1>氏名: {name}</h1>
    <h1>性別: {gender}</h1>
    <h1>生年月日: {birthday}</h1>
    <h1>住所: {address}</h1>
</body>
</html>
"""


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    r = redis.Redis(host="task-queue")
    logger.info("connected")

    while True:
        packed = r.blpop(["task"], 0)
        if not packed:
            continue

        try:
            task = json.loads(packed[1])
        except JSONDecodeError:
            logger.error("cannot decode: {}".format(packed[1]))
            continue

        name = task["name"]
        filename = task["filename"]
        fetch_request = fetch(name)
        personal_info = convert(fetch_request)
        html = TEMPLATE.format(
            name=personal_info.name,
            address=personal_info.address,
            gender=personal_info.gender,
            birthday=personal_info.birthday,
        )
        pdf = HTML(string=html).write_pdf()

        with open("/shared/" + filename, "wb") as f:
            f.write(pdf)


main()
