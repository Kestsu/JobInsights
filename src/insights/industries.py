from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    lista = []
    data = read(path)
    for item in data:
        if item["industry"] != '':
            lista.append(item["industry"])

    return list(set(lista))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    lista = []
    for item in jobs:
        if industry == item["industry"]:
            lista.append(item)

    return lista
