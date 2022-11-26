import requests

with open("sems", "r") as fs:
    sems = fs.readlines()
    for i, v in enumerate(sems):
        print(f"{i + 1} : {v.strip()}")
    n = int(input(f"Input number of sem: "))
    sem = sems[n - 1].strip()
    m = int(input(f"Input num of tasks in {sem}: "))
    URLS = [[] for _ in range(m)]

with open("reps", "r") as fr:
    reps = [url.strip() for url in fr]

    for rep in reps:
        for i in range(1, m + 1):
            url = f"{rep}/tree/main/{sem}/{i}/tests"
            if requests.get(url, timeout=2).status_code == 404:
                url = f"{rep}/tree/master/{sem}/{i}/tests"
                if requests.get(url, timeout=2).status_code == 404:
                    continue
            URLS[i - 1].append(url + '\n')

    for i, u in enumerate(URLS):
        with open(f"URLS{i + 1}", "w") as file:
            file.writelines(u)
