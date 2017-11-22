from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post, Comment
from django.template import loader
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.contrib.auth.models import User


def post_all(request):
    object_list = Post.objects.order_by('author')
    template = loader.get_template('blog/post_list.html')
    context = {
        'object_list': object_list, 'user': request.user
    }
    return HttpResponse(template.render(context))


def post_view(request, post_id):
    # if request.method == 'GET':
    post = Post.objects.get(id=post_id)
    object_list_com = Comment.objects.filter(post=post)
    template = loader.get_template('blog/post_view.html')
    context = {'object_list_com': object_list_com, 'post': post}
    return HttpResponse(template.render(context))
    # elif request.method == "POST":
    #     author = request.POST.get('author')
    #     text = request.POST.get('text')
    #     date = datetime.datetime.now()
    #     post = Post.objects.get(id=post_id)
    #     Comment.objects.create(author=author, text=text, date=date, post=post)
    #     return HttpResponseRedirect('/blog/posts/%s' % post)

def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        message = request.POST.get('message')
        author = request.user
        # date = request.POST.get('date')
        Post.objects.create(title=title, message=message, author=author, date=datetime.datetime.now())
    return HttpResponseRedirect('/blog/')


def add_com(request, post_id):
    if request.method == "POST":
        author = request.user
        text = request.POST.get('text')
        date = datetime.datetime.now()
        post = Post.objects.get(id=post_id)
        Comment.objects.create(author=author, text=text, date=date, post=post)
    return HttpResponseRedirect(Post.get_absolute_url(post))

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "blog/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/blog/posts"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "blog/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "blog/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/blog"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/blog")
