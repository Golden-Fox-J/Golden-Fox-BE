from rest_framework import serializers
from .models import Product,Category,Comment,Favourite_product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class Fav_productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite_product
        fields = "__all__"
