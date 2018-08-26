from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name="detail"),
    path('post/new/', views.BlogCreateView.as_view(), name="new"),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name="post_delete"),
]
