from django.urls import path

from tasks.views import (
    # create_task,
    # list_tasks,
    complete_task,
    TaskListView,
    TaskCreateView,
    # TaskUpdateView,
)

urlpatterns = [
    # path("create/", create_task, name="create_task"),
    # path("mine/", list_tasks, name="show_my_tasks"),
    path("<int:pk>/complete/", complete_task, name="complete_task"),
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", TaskListView.as_view(), name="show_my_tasks"),
    # path("<int:pk>/complete/", TaskUpdateView.as_view(), name="complete_task"),
]
