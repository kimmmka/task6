from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import FilmView, CategoryView, CartView, CommentView, Cart_detailView

app_name = "mycineomatica"

urlpatterns = [
    path('films/', FilmView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('cart/', CartView.as_view()),
    path('cart_detail/', Cart_detailView.as_view()),
    path('comment/', CommentView.as_view()),
    path('films/<int:pk>', FilmView.as_view(), name='film')
]
