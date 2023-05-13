from dataclasses import dataclass
from datetime import date, datetime
from xml.etree import ElementTree as ET


@dataclass
class PersonalInfo:
    name: str
    birthday: date
    address: str
    gender: str


def convert(utf8text: str) -> PersonalInfo:
    root = ET.fromstring(utf8text)
    name = root.findtext("DT0001")
    birthday = datetime.strptime(root.findtext("DT0002"), "%Y%m%d")
    address = root.findtext("DT0003")
    gender = "男" if root.findtext("DT0004") else "女"
    return PersonalInfo(name=name, birthday=birthday, address=address, gender=gender)
