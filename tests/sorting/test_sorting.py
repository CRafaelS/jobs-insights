from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    dict_jobs_values = read("src/jobs.csv")
    sort_by(dict_jobs_values, "min_salary")

    assert dict_jobs_values[0]["min_salary"] == "19857"
