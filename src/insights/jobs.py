from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode='r', encoding="utf-8") as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:
    lista = []
    data = read(path)
    for item in data:
        lista.append(item["job_type"])

    return list(set(lista))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    lista = []
    for item in jobs:
        if job_type == item["job_type"]:
            lista.append(item)

    return lista
