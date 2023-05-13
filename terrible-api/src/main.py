import xml.etree.ElementTree as ET

from fastapi import FastAPI, Path
from fastapi.responses import Response

app = FastAPI()


@app.get("/IF01/{name}")
async def get(
    name: str = Path(title="名前"),
):
    root = ET.Element("root")

    # 「番号タグ」というどうしようもないゴミ
    nameElement = ET.SubElement(root, "DT0001")
    nameElement.text = name

    birthday = ET.SubElement(root, "DT0002")
    birthday.text = "19700101"

    address = ET.SubElement(root, "DT0003")
    address.text = "神奈川県横浜市以下略"

    gender = ET.SubElement(root, "DT0004")
    gender.text = "1"

    xml_data = ET.tostring(root, encoding="shift_jis", xml_declaration=True)
    response = Response(content=xml_data, media_type="application/xml; charset=shift_jis")
    return response
