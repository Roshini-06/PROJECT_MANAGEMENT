from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Comment, Team
from .forms import TaskForm, ProjectForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Project

from django.shortcuts import render
from .models import Task

@login_required
# views.py
#from django.shortcuts import render
#from tasks.models import Task, Project  # import Task and Project

def dashboard(request):
    tasks = Task.objects.all()
    projects = Project.objects.all()

    # Count by status
    todo_count = tasks.filter(status='todo').count()
    inprogress_count = tasks.filter(status='inprogress').count()
    done_count = tasks.filter(status='done').count()

    context = {
        'tasks': tasks,
        'projects': projects,
        'todo_count': todo_count,
        'inprogress_count': inprogress_count,
        'done_count': done_count,
    }

    tasks = Task.objects.all()  # Or filter by user/project if needed
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

# --------- AUTH ---------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# --------- PROJECT VIEWS ---------
@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form})

@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'tasks/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'tasks/project_confirm_delete.html', {'project': project})


# --------- TASK VIEWS ---------
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = Comment.objects.filter(task=task)
    form = CommentForm()
    return render(request, 'tasks/task_detail.html', {'task': task, 'comments': comments, 'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Add Task'})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Edit Task'})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# --------- COMMENT ---------
@login_required
def add_comment(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', pk=task_id)
    return redirect('task_detail', pk=task_id)


# --------- TEAM ---------
@login_required
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tasks/team_list.html', {'teams': teams})

@login_required
def team_management(request):
    team_members = Team.objects.all()
    return render(request, 'tasks/team_management.html', {'team_members': team_members})


#from django.shortcuts import render, redirect
from .models import Team
from .forms import TeamForm  # we'll define this below
@login_required

@login_required
def team_management(request):
    teams = Team.objects.all()
    return render(request, 'tasks/team_management.html', {'teams': teams})

def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_management')  # ✅ This is correct now
    else:
        form = TeamForm()
    return render(request, 'tasks/team_create.html', {'form': form})

from django.shortcuts import render
from .models import Team

def team_view(request):
    return render(request, 'tasks/team.html')
from .models import Team

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'tasks/team_list.html', {'teams': teams})


# --------- ADMIN PANEL ---------
@login_required
def admin_panel(request):
    total_users = User.objects.count()
    total_projects = Project.objects.count()
    total_teams = Team.objects.count()
    return render(request, 'tasks/admin_panel.html', {
        'total_users': total_users,
        'total_projects': total_projects,
        'total_teams': total_teams
    })

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'tasks/user_list.html', {'users': users})
