import pandas

with open(r"E:\pythonProjects\resources\Book1.csv") as raw_data:
    data = pandas.read_csv(raw_data, nrows=183)

languages = {rows["language"]:rows["code"] for index, rows in data.iterrows()}
keys = [keys for keys in languages]

