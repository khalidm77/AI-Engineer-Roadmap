employees = [
    {
        "id": 101,
        "name": "Khalid",
        "skills": {"Python", "Django", "SQL"}
    },
    {
        "id": 102,
        "name": "Rahul",
        "skills": {"Python", "Java"}
    }
]

def get_employee_skills():
    for employee in employees:
        print(employee["name"]),
        for skill in employee["skills"]:
            print(skill)

get_employee_skills()
              