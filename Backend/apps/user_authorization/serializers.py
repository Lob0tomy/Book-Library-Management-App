from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from apps.users.models import User
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.validators import validate_international_phonenumber
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth import login


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        style={'input_type':'email', 'placeholder':'E-mail*', 'hide_label':'True'}
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type':'password', 'placeholder':'Hasło*', 'hide_label':'True'},
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type':'password','placeholder':'Powtórz hasło*', 'hide_label':'True'},
    )

    phone_no = PhoneNumberField(
        required=True,
        validators=[validate_international_phonenumber],
        style={'input_type':'number', 'placeholder':'Numer telefonu*', 'hide_label':'True'},
        region='PL'
    )

    first_name = serializers.CharField(
        required=True,
        style={'placeholder':'Imię*', 'hide_label':'True'}
    )

    last_name = serializers.CharField(
        required=True,
        style={'placeholder':'Nazwisko*', 'hide_label':'True'}
    )


    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'phone_no']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({'password':'Passwords must match'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_no=validated_data['phone_no'],
            password=validated_data['password']
        )
        return user