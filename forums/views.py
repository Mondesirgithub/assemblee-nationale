from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Post, Comment, Reply
from .utils import update_views
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from comptes.models import Depute
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
    forums = Category.objects.all()
    num_posts = Post.objects.all().count()
    num_users = Depute.objects.all().count()
    num_categories = forums.count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "forums":forums,
        "num_posts":num_posts,
        "num_users":num_users,
        "num_categories":num_categories,
        "last_post":last_post,
        "title": "Forum de l'assemblee nationale"
    }
    return render(request, "forums/forums.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    author = request.user
    author.num_post = Post.objects.filter(user=author).count()
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, _ = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, _ = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)

    comments = post.comments.all().order_by('-date')

    context = {
        "post":post,
        "comments": comments,
        "title": "Assemblee Nationale: "+post.title,
    }
    
    update_views(request, post)

    return render(request, "forums/detail.html", context)


def posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(approved=True, categories=category)
    print("POSTS =>", posts)
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) 

    context = {
        "posts":posts,
        "forum": category,
        "title": "L'Assemblee Nationale: Posts"
    }

    return render(request, "forums/posts.html", context)


def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            author = request.user
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("forums:home")
        
    context.update({
        "form": form,
        "title": "L'Assemblee Nationale: Create New Post"
    })
    return render(request, "forums/create_post.html", context)



def latest_posts(request):
    posts = Post.objects.all().filter(approved=True)[:10]
    context = {
        "posts":posts,
        "title": "L'Assemblee Nationale: Latest 10 Posts"
    }

    return render(request, "forums/latest-posts.html", context)

def search_result(request):
    return render(request, "forums/search.html")