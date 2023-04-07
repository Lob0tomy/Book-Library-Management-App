from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ObtainUserTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(TokenObtainPairSerializer, cls).get_token(user)
        token['email'] = user.email
        return token