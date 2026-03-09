from django.urls import path, include
from .views.templates_views import (
    TodoListView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
)
from .views.api_views import (
    TodoListAPI,
    TodoCreateAPI,
    TodoRetrieveAPI,
    TodoUpdateAPI,
    TodoDeleteAPI,
    TodoViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("view", TodoViewSet, basename="todo")

app_name = "todo"

urlpatterns = [
    # HTML 템플릿 뷰
    path("list/", TodoListView.as_view(), name="list"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("detail/<int:pk>/", TodoDetailView.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo_Update"),
    # 기존 API 뷰
    path("api/list/", TodoListAPI.as_view(), name="todo_api_list"),
    path("api/create/", TodoCreateAPI.as_view(), name="todo_api_create"),
    path("api/retrieve/<int:pk>/", TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    path("api/update/<int:pk>/", TodoUpdateAPI.as_view(), name="todo_api_update"),
    path("api/delete/<int:pk>/", TodoDeleteAPI.as_view(), name="todo_api_delete"),
    # ViewSet (CRUD 통합)
    path("viewsets/", include(router.urls)),
]
