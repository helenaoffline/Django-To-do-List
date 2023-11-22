from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import NewTodo, TodoGroup
from django.contrib.auth.mixins import LoginRequiredMixin

#todosviews
class NewTodoListView(LoginRequiredMixin,ListView):
    model=NewTodo
    template_name='home.html'
    context_object_name='newtodos'
    
class NewTodoCreateView(CreateView):
    model=NewTodo
    template_name='crud/create.html'
    fields="__all__"
    success_url=reverse_lazy('home')
    def form_valid(self, form): 
        if 'group_id' in form.cleaned_data:
            form.instance.group_id = form.cleaned_data['group_id']
        return super().form_valid(form)
    
class NewTodoUpdateView(UpdateView):
    model = NewTodo
    template_name = 'crud/update.html'  # Substitua pelo seu template desejado
    fields = "__all__"
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        if 'group_id' in form.cleaned_data:
            form.instance.group_id = form.cleaned_data['group_id']
        return super().form_valid(form)

class NewTodoDeleteView(DeleteView):
    model=NewTodo
    template_name='home.html'
    success_url=reverse_lazy('home')
    def form_valid(self, form):
            
            response = super().delete(self.request, *self.args, **self.kwargs)
            print("NewTodo excluído com sucesso!")
            return response



#groupviews
class TodoGroupCreateView(CreateView):
    model=TodoGroup
    template_name='home.html'
    fields="__all__"
    success_url=reverse_lazy('home')
    def form_valid(self, form): 
        form.instance.group_id=self.kwargs['group_id']
        return super().form_valid(form)
class TodoGroupUpdateView(UpdateView):
    model=TodoGroup
    template_name='home.html'
    fields="__all__"
    success_url=reverse_lazy('home')
class TodoDeleteView(DeleteView):
    model=TodoGroup
    #template_name='home.html'
    success_url=reverse_lazy('home')













# views logins
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            #login(request, user)
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

