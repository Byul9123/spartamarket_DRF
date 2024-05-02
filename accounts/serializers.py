from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction']
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드를 읽기 전용으로 설정

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)  # 비밀번호 해싱 자동 처리
        return user
