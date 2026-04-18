from pydantic import BaseModel, ValidationError, Field, field_validator, ConfigDict
from typing import List

class Teacher(BaseModel):
    name: str    
    age: int

class Student(BaseModel):
    name: str
    age: int = 20 # deÄŸer yoksa 20 yazar
    lectures: List[str]
    teachers: List[Teacher] = []

    model_config = ConfigDict(validate_assignment=True)


    @field_validator("lectures")
    @classmethod
    def validate_lectures(cls, v):
        if len(v) < 3:
            raise ValueError("En az 3 ders olmalÄ±")
        return v





data = {
    "name": "ouz",
    "age": 25,
    "lectures": ["Math", "Physics", "Chemistry"],
    "teachers": [
        {"name": "bora", "age": 30},
        {"name": "deniz", "age": 40}
    ]
}


student1 = Student(**data)
print(student1)

student1.no = 12312
print(student1)


# ÖZET: Öðretmen-öðrenci veri modelleri üzerinden; Pydantic ile nested (iç içe) veri doðrulamayý ve liste kýsýtlamalarýný (validator) pratik ediyoruz.
