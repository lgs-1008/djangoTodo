from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm
from django.http import Http404
#from django.contrib.auth.decorators import login_required
# Create your views here.
def todoView(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.createUser = request.user.username
            item.save()

    items = Todo.objects.filter(createUser = request.user.username).reverse()
    form = TodoForm()
    return render(request, 'todo.html', {'items' : items, 'form' : form})

def todo_delete(request, pk):
    try:
        item = Todo.objects.get(pk=pk)
        if item.createUser == request.user.username:
            item.delete()
        else:
            raise Http404("당신의 Todo가 아닙니다. Not your Todo.")

    except Todo.DoesNotExist:
        raise Http404("???")

    return redirect('todo:todoIndex')
