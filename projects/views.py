from projects.models import Project
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# from django.shortcuts import render, redirect
# from projects.forms import ProjectForm
# from django.contrib.auth.decorators import login_required

# @login_required
# def list_projects(request):
#     projects_list = Project.objects.filter(members=request.user)
#     context = {
#         "projects_list": projects_list,
#     }
#     return render(request, "projects/list.html", context)


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"
    context_object_name = "projects_list"


# @login_required
# def show_project(request, pk):
#     project_detail = Project.objects.get(pk=pk)
#     context = {
#         "project_detail": project_detail,
#     }
#     return render(request, "projects/detail.html", context)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"
    context_object_name = "project_detail"


# @login_required
# def create_project(request):
#     if request.method == "POST":
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             project = form.save()
#         return redirect("show_project", pk=project.id)
#     else:
#         form = ProjectForm()

#     context = {"form": form}

#     return render(request, "projects/create.html", context)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.id])
