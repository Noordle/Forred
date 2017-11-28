from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment
from django.template import loader
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.contrib.auth import login, logout
from django.views.generic.base import View
import json


def post_all(request):
    object_list = Post.objects.order_by('date')
    count_post = Post.objects.filter(author=request.user).count()
    template = loader.get_template('blog/post_list.html')
    context = {
        'object_list': object_list, 'user': request.user, 'count_post' : count_post,
    }
    return HttpResponse(template.render(context))


def post_view(request, post_id):
    if request.method == 'DELETE':
        Post.objects.get(id=post_id).delete()
        return HttpResponseRedirect("/blog/posts/")
    elif request.method == "GET":
        post = Post.objects.get(id=post_id)
        object_list_com = Comment.objects.filter(post=post)
        template = loader.get_template('blog/post_view.html')
        context = {'object_list_com': object_list_com, 'post': post, 'user': request.user}
        return HttpResponse(template.render(context))
    elif request.method == 'PUT':
        post = Post.objects.get(id=post_id)
        changedmessage = json.loads(request.body.decode())
        post.message = changedmessage['message_izm']
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())

def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        message = request.POST.get('message')
        author = request.user
        Post.objects.create(title=title, message=message, author=author, date=datetime.datetime.now())
    return HttpResponseRedirect('/blog/')


def add_com(request, post_id):
    if request.method == "POST":
        author = request.user
        text = request.POST.get('text')
        date = datetime.datetime.now()
        post = Post.objects.get(id=post_id)
        Comment.objects.create(author=author, text=text, date=date, post=post)
    return HttpResponseRedirect(post.get_absolute_url())


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "blog/login.html"
    success_url = "/blog"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/blog/posts"
    template_name = "blog/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/blog")
