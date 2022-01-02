from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
#from .cart import Cart
from .models import Film,Category, Cart, Comment,Cart_detail

from .serializer import FilmSerializer, CategorySerializer, CartSerializer, CommentSerializer,Cart_detailSerializer

class FilmView(APIView):
    def get(self, request):
        serializer = FilmSerializer(Film.objects.all(), many=True)
        return Response({"films": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        film = request.data.get('film')
        # Create an article from the above data
        serializer = FilmSerializer(data=film)
        if serializer.is_valid(raise_exception=True):
            film_saved = serializer.save()
        return Response({"success": "Film '{}' created successfully".format(film_saved.title)})
    def put(self, request, pk):
        saved_film = get_object_or_404(Film.objects.all(), pk=pk)
        data = request.data.get('Film')
        serializer = filmSerializer(instance=saved_film, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            film_saved = serializer.save()
        return Response({
            "success": "Film '{}' updated successfully".format(film_saved.title)
        })
    def delete(self, request, pk):
        # Get object with this pk
        film = get_object_or_404(Film.objects.all(), pk=pk)
        film.delete()
        return Response({
            "message": "Film with id `{}` has been deleted.".format(pk)
        }, status=204)
        
class CategoryView(APIView):
    def get(self, request):
        serializer=CategorySerializer(Category.objects.all(), many=True)
        return Response({"categories": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        category = request.data.get('category')
        # Create an article from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.name)})
    def put(self, request, pk=None):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        data = request.data.get('category')
        serializer = CategorySerializer(instance=saved_category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({
            "success": "Category '{}' updated successfully".format(category_saved.name)
        })
    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({
            "message": "Category with id `{}` has been deleted.".format(pk)
        }, status=204)

class CartView(APIView):
    def get(self, request):
        serializer=CartSerializer(Cart.objects.all(), many=True)
        return Response({"cart": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})
    def post(self, request):
        cart = request.data.get('cart')
        # Create an article from the above data
        serializer = CartSerializer(data=cart)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({"success": "Cart '{}' created successfully".format(cart_saved.id)})
    def put(self, request, pk):
        saved_cart = get_object_or_404(Cart.objects.all(), pk=pk)
        data = request.data.get('cart')
        serializer = CartSerializer(instance=saved_cart, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_saved = serializer.save()
        return Response({
            "success": "Cart '{}' updated successfully".format(cart_saved.id)
        })
    def delete(self, request, pk):
        # Get object with this pk
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart.delete()
        return Response({
            "message": "Cart with id `{}` has been deleted.".format(pk)
        }, status=204)

class CommentView(APIView):
    def get(self, request):
        serializer=CommentSerializer(Comment.objects.all(), many=True)
        return Response({"comment": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        comment = request.data.get('comment')
        # Create an article from the above data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({"success": "Comment '{}' created successfully".format(comment_saved.author)})
    
    def put(self, request, pk):
        saved_comment = get_object_or_404(Comment.objects.all(), pk=pk)
        data = request.data.get('comment')
        serializer = CommentSerializer(instance=saved_comment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()
        return Response({
            "success": "Comment '{}' updated successfully".format(comment_saved.author)
        })
    
    def delete(self, request, pk):
        # Get object with this pk
        comment = get_object_or_404(Comment.objects.all(), pk=pk)
        comment.delete()
        return Response({
            "message": "Comment with id `{}` has been deleted.".format(pk)
        }, status=204)

class Cart_detailView(APIView):
    def get(self, request):
        serializer=Cart_detailSerializer(Cart_detail.objects.all(), many=True)
        return Response({"cart_detail": serializer.data, 'user': str(request.user), 'auth': str(request.auth)})

    def post(self, request):
        cart_detail = request.data.get('cart_detail')
        # Create an article from the above data
        serializer = Cart_detailSerializer(data=cart_detail)
        if serializer.is_valid(raise_exception=True):
            cart_detail_saved = serializer.save()
        return Response({"success": "Cart_detail '{}' created successfully".format(cart_detail_saved.film)})
    
    def put(self, request, pk):
        saved_cart_detail = get_object_or_404(Cart_detail.objects.all(), pk=pk)
        data = request.data.get('cart_detail')
        serializer = Cart_detailSerializer(instance=saved_cart_detail, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cart_detail_saved = serializer.save()
        return Response({
            "success": "Cart_detail '{}' updated successfully".format(cart_detail_saved.film)
        })
    
    def delete(self, request, pk):
        # Get object with this pk
        cart_detail = get_object_or_404(cart_detail.objects.all(), pk=pk)
        cart_detail.delete()
        return Response({
            "message": "Cart_detail with id `{}` has been deleted.".format(pk)
        }, status=204)