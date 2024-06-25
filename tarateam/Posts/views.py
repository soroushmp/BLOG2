from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentsForm, Form_CooperationRequest
from .models import Post


def homepage_render(request):
    return render(request, 'home.html')


def blogs_render(request):
    blogs = Post.objects.order_by('-created_at')
    return render(request, 'blogs.html', {'blogs': blogs})


def blog_render(request, pk):
    selected_blog = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = selected_blog
            comment.save()
    else:
        form = CommentsForm()
    return render(request, 'blog.html', {'blog': selected_blog, 'form': form})


def cooperation_request_page(request):
    if request.method == 'POST':
        form = Form_CooperationRequest(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'درخواست شما با موفقیت افزوده شد')
        else:
            messages.error(request, 'درخواست شما با مشکل روبرو شد')

    else:
        form = Form_CooperationRequest()
    return render(request, 'form.html', {'form': form})
