# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from  django.views.generic import TemplateView,DetailView,ListView,FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.http.response import Http404
from django.contrib.auth import REDIRECT_FIELD_NAME, login
import urlparse
from .models import Company
from django.contrib.auth.models import UserManager,Group, User
from rules.contrib.views import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *
from django.contrib.auth import logout
# Create your views here.

class LoginAuth(FormView):
    form_class = PlaceholderAuthForm
    redirect_field_name = 'index'
    template_name = 'Login/main.html'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginAuth,self).dispatch(request,*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        #return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect('index')

    def get_success_url(self):
        if self.success_url:
            redirect_to = self.request.GET.get(self.redirect_field_name)
        else:
            redirect_to = self.request.GET.get(self.redirect_field_name)

        return redirect_to

    def get(self, request, *args, **kwargs):
        return super(LoginAuth,self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_class =self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


#class Main(LoginRequiredMixin, PermissionRequiredMixin,ListView):
#    model = Company
#    template_name = "Login/index.html"
#    context_object_name = 'nodes'
#    permission_required = 'Company.view_entry'


class Main(LoginRequiredMixin,ListView):

    model = Company
    template_name = "Login/index.html"
    context_object_name = 'nodes'
    #request.user.groups.filter(name='CompanyEditor').exists()
    #метод  листвиев так, как не устраивает стандартный запрос кверисет
    def get_queryset(self):
        #queryset = super(Main,self).get_queryset()
        #if User.groups(name='CompanyEditors'):
        #group = self.request.user.groups.get().name

        # выдёргиваем из запроса группы пользователя и фильтруем по имени, а екзист проверяет наличие в этом списке данной грпуппы
        if self.request.user.groups.filter(name='CompanyEditors').exists() == True:
        #if user.groups(name='CompanyEditors'):
        # два подчёркивания это доп фильтр к запросу допустим искать этой колонке по id в данном сучае фильтр на наличие вхождения в это группу
            queryset =Company.objects.filter(managers__in=[1,2])

        elif self.request.user.groups.filter(name='CompanyGuest').exists() == True:
            queryset = Company.objects.filter(managers__in=[2])
        return queryset

 #   permission_required = 'Company.view_entry'

class Detail( DetailView):
    model =Company
    #permission_required = 'company.views_entry'
    template_name = 'Login/detail.html'
    context_object_name = 'nodes'


    #def handle_no_permission(self):
     #   return redirect(
      #      to='Login/index.html')

    def get_object(self):
        get= get_object_or_404(Company, slug=self.kwargs['slug'])
        get1=self.request.user.id
        print get1
        #get =Company.objects.get(slug=self.kwargs['slug'])
        #group=self.request.user.groups.filter(name=get.managers.name).exists()

        if get.managers.filter(user__id=self.request.user.id).exists():
        #if get.managers.name == group:
            return get
        else:
            raise Http404()

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("login")