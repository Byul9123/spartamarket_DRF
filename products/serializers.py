from rest_framework import serializers
from .models import Product
from accounts.models import CustomUser

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        return super().create(validated_data)
