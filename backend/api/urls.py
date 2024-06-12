from api.views.registration import UserRegistration
from api.views.post import *
from api.views.token import TokenPairView
from django.urls import path

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('token/', TokenPairView.as_view(), name='token_obtain_pair'),
    path('create/', CreatePost.as_view(), name='create'),
    path('posts/', ListPost.as_view(), name='all_posts'),
    path('<str:username>/posts/', ListPostByUser.as_view(), name='users_post'),
    path('post/<slug:slug>', RetrievePost.as_view(), name='post'),
    path('update/<slug:slug>', UpdatePost.as_view(), name='update'),
    path('delete/<slug:slug>', DeletePost.as_view(), name='create'),
    

]