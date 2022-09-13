from django.urls import path

from projects.views import (
    # list_projects,
    # show_project,
    # create_project,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
)

urlpatterns = [
    # path("", list_projects, name="list_projects"),
    # path("<int:pk>/", show_project, name="show_project"),
    # path("create/", create_project, name="create_project"),
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
]
