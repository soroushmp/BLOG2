from django.shortcuts import render , get_object_or_404 ,  redirect
from .models import post, Comment
from .forms import CommentsForm , Form_CooperationRequest


def home(request):
    return render(request , 'Posts/home.html')


def blog(request):
    posts = post.objects.order_by('-created_at')
    return render(request , 'Posts/blog.html' ,{'data' : posts})


def post_def(request , post_id):
    post_data =get_object_or_404(post,pk=post_id)

    comments = post_data.comments.all()
    form = None
    # if request.method == 'POST':
    form = CommentsForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post= post_data
        comment.save()
    else:
        form = CommentsForm()
    return render(request, 'Posts/post.html', {'data': post_data, 'comments': comments, 'form': form})



def CooperationRequest_page(request):
    form = None

    if request.method == 'POST':
        form = Form_CooperationRequest(request.POST)
        if form.is_valid():
            form.save()
            return redirect('save')
    else:
        form = Form_CooperationRequest()
    return render(request, 'Posts/form.html', { 'form': form})
    
            
def save(request):
    return render(request,'Posts/save.html')