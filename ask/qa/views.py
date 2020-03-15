from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login, authenticate

from .models import Question
from .forms import AskForm, AnswerForm, UserCreateForm, LoginForm
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answer_set.all()
    answer_form = AnswerForm(initial={'question': question.id})
    if request.POST:
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save(commit=False)
            answer_form.author = request.user
            answer_form.save()
            return HttpResponseRedirect('/question/{pk}/'.format(pk=pk))
    return render(request, 'qa/question_detail.html', {'question': question, 'answers': answers, 'pk': pk, 'form': answer_form})
    


def question_list(request):
    page_number = request.GET.get('page', 1)
    limit = 10
    objects = Question.objects.new()
    paginator = Paginator(objects, limit)
    questions = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'questions': questions})

def popular_question_list(request):
    page_number = request.GET.get('page', 1)
    limit = 10
    objects = Question.objects.popular()
    paginator = Paginator(objects, limit)
    questions = paginator.get_page(page_number)
    return render(request, 'qa/index.html', {'questions': questions})


def post_ask(request):
    if request.POST:
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return HttpResponseRedirect('/question/{question}/'.format(question=question.id))
    form = AskForm()
    return render(request, 'qa/new_post.html', {'form': form})




def signup(request):
    form = UserCreateForm()
    if request.POST:
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            auth = authenticate(username=user.username, password=password)
            if auth is not None:
                auth_login(request, auth)
                return HttpResponseRedirect('/')
    return render(request, 'qa/signup.html', {'form': form})


def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'qa/login.html', {'form': LoginForm()})
