import csv


def csv_reader(file_name: str) -> list[dict[str, str | int | float]]:
    with open(file_name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

        for student in students:
            student["ID"] = int(student["ID"])
            student["media"] = float(student["media"])

        return students


def text_reader(file_name: str) -> list[list[str | int]]:
    with open(file_name, encoding="utf-8") as f:
        content = f.readlines()
        goals = []

        for row in content:
            row = row.strip()
            values = row.split(",")
            try:
                values = [int(value) for value in values]
            except ValueError:
                pass
            goals.append(values)

        return goals
