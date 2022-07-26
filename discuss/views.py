from datetime import datetime

from django.shortcuts import render, redirect

from first.models import Food
from .forrm import add_comment
from .models import Post, Comments
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def dis(request):
    all_posts = Post.objects.all()
    if request.method == 'POST':
        comment= request.POST.get('comment')
        new_post = Post(text=comment, author=request.user)
        new_post.save()
        return redirect('discuss')
    return render(request, 'discuss.html', {'posts':all_posts})


def add_comments(request,pk):
    item = Food.objects.get(id=pk)
    add_dic = add_comment(instance=item)
    comment_for_this_meal = Comments.objects.filter(fop=item).order_by('time_added')
    print(comment_for_this_meal)
    if request.method =='POST':
        print('post')
        add_dic =add_comment(request.POST, instance=item)
        if add_dic.is_valid():
            print('in valid')
            name = request.user.username
            body = add_dic.cleaned_data.get('body')
            print(body)

            co = Comments(body=body,fop=item, name=name, time_added=datetime.now)
            print(co)
            co.save()
            return redirect('food', pk)
    else:
        return render(request, 'comment.html', {'add': add_dic,
                                                'comments':comment_for_this_meal})