import typing
from django.contrib.auth.backends import ModelBackend
from api.models import Person
from api import services


class CheckPasswordBackend(ModelBackend):
    def authenticate(self,
         request=None, phone_number=None, password=None
    ) -> typing.Optional[Person]:
        print("my auth executed")
        person = services.find_person_by_phone_number(phone_number=phone_number)

        if person is None:
            print("person is none")
            return None

        return person if person.password==password else None

    def get_user(self, person_id) -> typing.Optional[Person]:
        try:
            return Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return None