from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .form import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'allalbum'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album;
    fields = ['artist','album_title','genre','logo']

class AlbumUpdate(UpdateView):
    model = Album;
    fields = ['artist','album_title','genre','logo']

class AlbumDelete(DeleteView):
    model = Album;
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class=UserForm
    template_name='music/registation_form.html'
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #cleaned
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()