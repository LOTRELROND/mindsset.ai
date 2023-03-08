from django.shortcuts import render,redirect
from .models import Post,FavItem,Visiter
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    posts = Post.objects.filter(active=True)

    context = {
        'posts':posts,
    }
    return render(request, "index.html", context)

@login_required()
def updateFav(request):

    data = json.loads(request.body.decode('utf-8'))
    postId = data['postId']
    action = data['action']
    print(action)
    print(postId)

    post = Post.objects.get(id = postId)
    favItem, created = FavItem.objects.get_or_create(post = post, user=request.user.visiter)
    favItem.save()

    if action == 'remove':
        favItem.delete()


    return JsonResponse('item was added', safe =False)

   
@login_required
def createvisitor(request):
    if request.method == "POST":
            username2 = request.POST["username"]
            print(username2)
            new = Visiter.objects.create(user=request.user, username=username2)
            new.save()
            return redirect("index")
    context={}
    return render(request, "createvisitor.html", context)

@login_required
def fav(request):
    favs = FavItem.objects.filter(user = request.user.visiter)
    context = { 
        'favs':favs,
    }
    return render(request, "fav.html",context)

