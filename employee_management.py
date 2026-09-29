employees = [
    {
        "id": 101,
        "name": "Khalid",
        "role": "Developer",
        "department": "IT",
        "skills": {"Python", "Django", "SQL"}
    },
    {
        "id": 102,
        "name": "Rahul",
        "role": "Tester",
        "department": "QA",
        "skills": {"Python", "Selenium"}
    }
]


def display_employees():
    for employee in employees:
        print(
            employee["id"],
            "-",
            employee["name"],
            "-",
            employee["role"]
        )


def find_employee(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None


def add_employee(employee_id, name, role, department, skills):
    employee = {
        "id": employee_id,
        "name": name,
        "role": role,
        "department": department,
        "skills": set(skills)
    }

    employees.append(employee)


def update_role(employee_id, new_role):
    employee = find_employee(employee_id)

    if employee:
        employee["role"] = new_role
        print("Role updated.")
    else:
        print("Employee not found.")


def delete_employee(employee_id):
    employee = find_employee(employee_id)

    if employee:
        employees.remove(employee)
        print("Employee deleted.")
    else:
        print("Employee not found.")


def add_skill(employee_id, skill):
    employee = find_employee(employee_id)

    if employee:
        employee["skills"].add(skill)
        print("Skill added.")
    else:
        print("Employee not found.")


display_employees()