from rest_framework import serializers
from blog.models import *
from video.models import *
from accounts.models import Account
from django.contrib.auth import authenticate
from rest_framework import exceptions
from djoser.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Blog
        fields = '__all__'
        extra_fields = ['category.name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Video
        fields = '__all__'
        extra_fields = ['category.name']


class CurrentUser(UserSerializer):
    
    profile_pic = serializers.SerializerMethodField('profile_pic')
    def profile_pic(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request
        
    class Meta(UserSerializer.Meta):
        fields = ['username','email','id','profile_pic']
