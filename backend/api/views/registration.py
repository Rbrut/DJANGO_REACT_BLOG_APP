from api.models.user import User
from api.serializers.user import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny



class UserRegistration(CreateAPIView):
    ''' 
    User Registration View
    This view allows us to create a new user
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]