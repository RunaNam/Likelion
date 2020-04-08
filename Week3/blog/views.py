from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogForm
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_detail': blog_detail})


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('detail/'+str(blog.id))
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

