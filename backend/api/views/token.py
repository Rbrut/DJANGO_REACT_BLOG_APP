from api.serializers.token import TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenSerializer