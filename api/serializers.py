from .models import Person
from .models import Contact
from rest_framework import serializers

# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = ('contact_name', 'contact_phone_number', 'spam')



class SignUpSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length = 32)
    password =  serializers.CharField(max_length = 16)
    phone_number= serializers.CharField(max_length = 16)
    confirm_password=serializers.CharField(max_length = 16)
    email=serializers.EmailField()
    contact_id=serializers.IntegerField()
    class Meta:
        model = Person
        fields = ('name','password','confirm_password','phone_number','email','contact_id')

    def create(self,validated_data):
        del validated_data['confirm_password']
        user = Person.objects.create_user(**validated_data)
        return user


    def validate(self,value):

        if value.get('password') != value.get('confirm_password'):
            raise serializers.ValidationError('Both the passwords does not match')
        return value

class ContactSerializer(serializers.ModelSerializer):

    contact_name = serializers.CharField(max_length = 32)
    contact_phone_number= serializers.CharField(max_length = 16)
    class Meta:
        model = Contact
        fields = ('contact_name','contact_phone_number')

    def create(self,validated_data):
        contact = Contact.objects.create(**validated_data)
        return contact


    def validate(self,value):
        return value