from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    uniqueJob = read(path)
    listJob = []

    for job in uniqueJob:
        if job["job_type"] not in listJob:
            listJob.append(job["job_type"])
    return list(set(listJob))


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    list_job = list()

    for job in jobs:
        if job["job_type"] == job_type:
            list_job.append(job)
    return list_job


def get_unique_industries(path):
    jobs = read(path)
    listindustries = []

    for job in jobs:
        if job["industry"] not in listindustries and len(job["industry"]) != 0:
            listindustries.append(job["industry"])
    return listindustries


def filter_by_industry(jobs, industry):
    list_industry = list()

    for job in jobs:
        if job["industry"] == industry:
            list_industry.append(job)
    return list_industry


def get_max_salary(path):
    salaries = read(path)
    newSalary = [
        int(salary["max_salary"])
        for salary in salaries
        if salary["max_salary"].isdigit()
    ]

    return max(newSalary)


def get_min_salary(path):
    salaries = read(path)
    newSalary = [
        int(salary["min_salary"])
        for salary in salaries
        if salary["min_salary"].isdigit()
    ]

    return min(newSalary)


def matches_salary_range(job, salary):
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("Falta a chave min_salary ou max_salary")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("min_salary ou max_salary não é um valor inteiro")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary é maior que max_salary")
    elif type(salary) != int:
        raise ValueError("salary não é um valor inteiro")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    job_list = []
    for job in jobs:
        try:
            matches_salary_range(job, salary)
            if job["min_salary"] <= salary <= job["max_salary"]:
                job_list.append(job)
        except ValueError:
            False
    return job_list
