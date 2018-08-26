from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name= 'blog/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'    
    success_url = reverse_lazy('index')


class BlogUpdateView(UpdateView):
    model = Post
    fields =['title', 'body']
    template_name = 'blog/post_new.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('index')    
