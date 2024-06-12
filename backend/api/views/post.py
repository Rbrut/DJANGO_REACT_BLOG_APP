from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from api.models.post import Post
from api.models.user import User
from django.shortcuts import get_object_or_404
from api.serializers.post import PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class ListPostByUser(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username )
        return Post.objects.filter(author=user)

class RetrievePost(RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Post.objects.get(slug=slug)
    
class UpdatePost(UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Post.objects.get(slug=slug, author=self.request.user)

class DeletePost(DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Post.objects.get(slug=slug, author=self.request.user)


