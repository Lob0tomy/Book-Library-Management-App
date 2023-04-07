from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from apps.users.models import User
from django.contrib.auth.password_validation import validate_password
from phonenumber_field.validators import validate_international_phonenumber
from phonenumber_field.serializerfields import PhoneNumberField


class UserObtainTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type':'password', 'placeholder':'Password'},
        label='Password'
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type':'password','placeholder':'Repeat Password'},
        label='Repeat Password'
    )
    phone_no = PhoneNumberField(
        required=True,
        validators=[validate_international_phonenumber],
        label='Phone Number',
        region='PL'
    )


    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'phone_no', 'photo']
        extra_kwargs = {
            'first_name':{'required':True},
            'last_name':{'required':True},
        }

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
            photo=validated_data['photo'],
            password=validated_data['password']
        )
        return user