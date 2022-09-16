import typing

from .models import Person

# def create_person(email: str, name: str, password: str) -> Person:
#     return Person.objects.create_user(email=email, name=name, password=password)

def find_person_by_phone_number(phone_number: str) -> typing.Optional[Person]:
    try:
        return Person.objects.get(phone_number=phone_number)
    except Person.DoesNotExist:
        return None