from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
            image=request.FILES.get('image')
        )
        return redirect('post_list')
    return render(request, 'posts/post_form.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.author = request.POST['author']
        post.content = request.POST['content']
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('post_detail', id=post.id)
    return render(request, 'posts/post_form.html', {'post': post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')
