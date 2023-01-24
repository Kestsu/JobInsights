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
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
