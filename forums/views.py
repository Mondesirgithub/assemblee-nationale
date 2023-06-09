from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm, ForumForm
from django.contrib.auth.decorators import login_required
from comptes.models import Depute
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages



@login_required
def home(request):
    if request.user.identifiant == "":
        return redirect("loginDepute")
    
    form = ForumForm()
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            author = request.user
            new_forum = form.save(commit=False)
            new_forum.user = author
            new_forum.save()
            form.save_m2m()
            return redirect("forums:home")
        
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = Depute.objects.all().count()
    num_categories = forums.count()
    num_comments = Post.objects.all().count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []
        
        
    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_comments":num_comments,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "Forum de l'assemblee nationale",
        "form": form
    }
    return render(request, "forums/forums_list.html", context)


@login_required
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = request.user
    author.num_post = Post.objects.filter(user=author).count()
    reponses = None
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        if comment == "":
            messages.error(request, "Le commentaire ne doit pas être vide !")
        else:
            new_comment, _ = Comment.objects.get_or_create(user=author, content=comment)
            post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        if reply == "":
            messages.error(request, "La reponse ne doit pas etre vide !")
        else:
            commenr_id = request.POST.get("comment-id")
            comment_obj = Comment.objects.get(id=commenr_id)
            new_reply, _ = Reply.objects.get_or_create(user=author, content=reply)
            comment_obj.replies.add(new_reply.id)

    comments = post.comments.all().order_by('-date')
    
    context = {
        "post":post,
        "comments": comments,
        "title": "Assemblee Nationale: "+post.title,
        'reponses': reponses
    }
    
    update_views(request, post)

    return render(request, "forums/details_forum.html", context)


def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    form = PostForm(request.POST or None)
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    if request.method == "POST":
        if form.is_valid():
            author = request.user
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect(request.path)
        
    context = {
        "posts":posts,
        "forum": category,
        "form": form,
        "title": "L'Assemblee Nationale: Posts"
    }

    return render(request, "forums/posts.html", context)



def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "L'Assemblee Nationale: Latest 10 Posts"
    }

    return render(request, "forums/latest-posts.html", context)


def search_result(request):
    return render(request, "forums/search.html")