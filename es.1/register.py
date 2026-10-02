import csv


def csv_reader(file_name: str) -> list[dict[str, str]]:
    with open(file_name, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)

        return students
