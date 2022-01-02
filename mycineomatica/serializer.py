from rest_framework import serializers
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Cart, Comment, Cart_detail, Category, Film

class FilmSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Film.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.film = validated_data.get('film', instance.film)
        instance.place = validated_data.get('place', instance.place)
        instance.row = validated_data.get('row', instance.row)
        instance.save()
        return instance

    class Meta:
        model=Film
        fields = ('id', 'film','place','row')

class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance
    class Meta:
        model=Category
        fields = ('id', 'name', 'slug')

class Cart_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_detail 
        fields=('id','cart_id', 'quantity', 'film')
    def create(self, validated_data):
        return Cart_detail.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.cart_id = validated_data.get('cart_id', instance.cart_id)
        instance.film = validated_data.get('film', instance.films)
        instance.save()
        return instance


class CartSerializer(serializers.ModelSerializer):
    '''total_sum=serializers.IntegerField(default=0)
    status = serializers.CharField(max_length=200)
    user = serializers.CharField(source='user.username')
    if(status=='new'):
        serializer = Cart_detailSerializer(data=cart_detail)
    '''
    def create(self, validated_data):
        return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.total_sum = validated_data.get('total_sum', instance.total_sum)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
    class Meta:
        model=Cart
        fields=( 'id', 'user','total_sum', 'status')

class CommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.content = validated_data.get('content', instance.content)
        instance.creation_date = validated_data.get('creation_date', instance.creation_date)
        instance.replies = validated_data.get('replies', instance.replies)
        instance.film = validated_data.get('film', instance.film)
        instance.save()
        return instance
    class Meta:
        model=Comment
        fields=('id', 'author', 'rate', 'content', 'creation_date', 'replies', 'film')