from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    lista = []
    data = read(path)
    for item in data:
        try:
            lista.append(int(item["max_salary"]))
        except (ValueError):
            pass

    lista.sort()
    lista.reverse()

    return lista[0]


# if __name__ == "__main__":
#     print(get_max_salary("data/jobs.csv"))


def get_min_salary(path: str) -> int:
    lista = []
    data = read(path)
    for item in data:
        try:
            lista.append(int(item["min_salary"]))
        except (ValueError):
            pass
    lista.sort()

    return lista[0]


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    max = "max_salary"
    min = "min_salary"

    try:
        if int(job[min]) > int(job[max]):
            raise ValueError
        return int(job[max]) >= int(salary) >= int(job[min])
    except (ValueError, KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:

    lista = []
    for item in jobs:
        try:
            if matches_salary_range(item, salary):
                lista.append(item)
        except (ValueError):
            pass
    return lista


# if __name__ == "__main__":
#     b = [
#         {"max_salary": 0, "min_salary": 10},
#         {"max_salary": 10, "min_salary": 100},
#         {"max_salary": 10000, "min_salary": 200},
#         {"max_salary": 15000, "min_salary": 0},
#         {"max_salary": 1500, "min_salary": 0},
#         {"max_salary": -1, "min_salary": 10},
#     ]
#     print(filter_by_salary_range(b, 100))
