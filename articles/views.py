from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models


# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Article
    fields = ['title', 'body', ]
    login_url = 'login'
    template_name = 'article_edit.html'


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    login_url = 'login'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = models.Article
    template_name = 'article_create.html'
    fields = ['title','body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)