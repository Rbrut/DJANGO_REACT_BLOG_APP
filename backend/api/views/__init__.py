from api.views.registration import UserRegistration
from api.views.token import TokenPairView
from api.views.post import *

all = [
    UserRegistration,
    TokenPairView,
    CreatePost,
    ListPost,
    ListPostByUser,
    RetrievePost,
    UpdatePost,
    DeletePost,
]