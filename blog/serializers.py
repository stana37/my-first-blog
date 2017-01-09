from rest_framework import serializers
from blog.models import Comment, Post, Blog

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text', 'created_date', 'published_date')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created_date', 'approved_comment')

class BlogSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    comment = CommentSerializer()
    class Meta:
        model = Blog
        fields = ('id', 'post', 'comment')
