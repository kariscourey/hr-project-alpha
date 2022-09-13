from django.shortcuts import redirect  # , render
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# from tasks.forms import TaskCreateForm  # , TaskUpdateForm


# @login_required
# def list_tasks(request):
#     tasks_list = Task.objects.filter(assignee=request.user)
#     context = {
#         "tasks_list": tasks_list,
#     }
#     return render(request, "tasks/list.html", context)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks_list"


# @login_required
# def create_task(request):
#     if request.method == "POST":
#         form = TaskCreateForm(request.POST)
#         if form.is_valid():
#             task = form.save()
#         return redirect("show_project", pk=task.project.id)
#     else:
#         form = TaskCreateForm()

#     context = {"form": form}

#     return render(request, "tasks/create.html", context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


@login_required
def complete_task(request, pk):
    # Get is_completed value from template
    completed = request.POST.get("is_completed")

    # Update is_completed value for instance (filtered)
    Task.objects.filter(id=pk).update(is_completed=completed)

    return redirect("show_my_tasks")
