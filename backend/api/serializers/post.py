from rest_framework import serializers
from api.models.post import Post
from api.models.category import Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'author.username')
    image = serializers.ImageField(required = False)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = [
            'id',
            'image',
            'author',
            'title',
            'slug',
            'description',
            'category',
            'body',
            'created',
            'modified'
        ]
        # extra_kwargs = {"author": {"read_only": True}}