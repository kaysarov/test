from django.utils import timezone
from .models import Post
import numpy as np
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'firstapp/post_list.html', {'posts': posts})


def simple(request):
    x = np.random.random(1000)
    return render(request, 'firstapp/simple.html', {'x': x})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'firstapp/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'firstapp/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'firstapp/post_edit.html', {'form': form})
