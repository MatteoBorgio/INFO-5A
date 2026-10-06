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
        requests = []

        for row in content:
            row = row.strip()
            values = row.split(",")
            try:
                values = [int(value) for value in values]
            except ValueError:
                pass
            requests.append(values)

        return requests


def find_by_term(
    key: str, term: str | int | float, students: list[dict[str, str | int | float]]
) -> dict[str, str | int | float] | None:
    try:
        for student in students:
            if student[key] == term:
                return student
    except KeyError:
        print("Key is not valid.\n")
    return None


def verify_id(identifier, students: list[dict]) -> bool:
    for student in students:
        if student["ID"] == identifier:
            return True
    return False


def students_in_class(
    c: str, students: list[dict[str, str | int | float]]
) -> list[dict[str, str | int | float]] | None:
    class_students = []
    for student in students:
        if student["classe"] == c:
            class_students.append(student)

    return class_students if len(class_students) > 0 else None


def find_average(students: list[dict[str, int]]) -> float:
    student_averages_sum = 0
    counter = 0
    for student in students:
        student_averages_sum += student["media"]
        counter += 1
    try:
        average = student_averages_sum / counter
        return average
    except ZeroDivisionError:
        return 0


def print_student_record(student: dict[str, str | int | float] | None) -> None:
    if student is not None:
        print(
            f"{student['ID']} {student['cognome']} {student['nome']} {student['classe']} {student['media']}\n"
        )


def main() -> None:
    students = csv_reader("students.csv")
    requests = text_reader("requests.txt")

    print("--- Ricerca per ID ---\n")
    for identifier in requests[0]:
        if verify_id(identifier, students):
            print_student_record(find_by_term("ID", identifier, students))
        else:
            print(f"ID {identifier} non trovato\n")

    print("--- Ricerca per cognome ---\n")
    for surname in requests[1]:
        print_student_record(find_by_term("ID", surname, students))

    print(f"--- Media della classe {requests[2][0]} ---\n")
    if students_in_class(requests[2][0], students) is None:
        print(f"Nessun studente nella classe {requests[2][0]}\n")
    else:
        class_students = students_in_class(str(requests[2][0]), students)
        students_length = len(class_students)
        print(f"Studenti considerati: {students_length}\n")

    print("")
