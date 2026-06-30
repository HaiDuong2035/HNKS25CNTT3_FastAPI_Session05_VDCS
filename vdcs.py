from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NewRegistration(BaseModel):
    id: int
    student_id: int
    course_id: int

students = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"},
    {"id": 3, "name": "Le Van C"}
]
courses = [
    {"id": 1, "name": "FastAPI Basic", "capacity": 2},
    {"id": 2, "name": "Python OOP", "capacity": 2}
]
registrations = [
    {"id": 1, "student_id": 1, "course_id": 1},
    {"id": 2, "student_id": 2, "course_id": 1}
]

@app.post('/registrations')
def create_registration(new_registration: NewRegistration):
    for regis in registrations:
        if regis['student_id'] == new_registration.student_id and regis['course_id'] == new_registration.course_id:
            return {
                "detail": "Student already registered this course"
            }

    for course in courses:
        if course['id'] == new_registration.course_id:
            count_regis = 0
            for regis in registrations:
                if regis['course_id'] == course['id']:
                    count_regis += 1
            if course['capacity'] <= count_regis:
                return {
                    "detail": "Course is full"
                }

    registrations.append({
        'id': new_registration.id,
        'student_id': new_registration.student_id,
        'course_id': new_registration.course_id
    })

    return {
        'massage': 'Registration successful',
        'data': {
            'id': new_registration.id,
            'student_id': new_registration.student_id,
            'course_id': new_registration.course_id
        }
    }