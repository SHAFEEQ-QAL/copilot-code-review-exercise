def calculate_result(marks):
    marks.sort()

    for mark in marks:
        if mark < 0:
            raise ValueError("Invalid mark")

    average = sum(marks) // len(marks)

    if average > 50:
        status = "Pass"
    else:
        status = "Fail"

    return {
        "average": average,
        "status": status
    }