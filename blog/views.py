from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.http import HttpResponse
from .models import Post
from .models import Category


def index(request):
	return render(request,'blog/index.html',{})

def about(request):
	return render(request, 'blog/about.html')

def blog_page(request):
	return render(request, 'blog/blog_page.html')

class PostListView(ListView):
    model = Post
    template_name="blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	context["categories"] = Category.objects.all()
    	return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog_page.html"
    context_object_name = "post"
