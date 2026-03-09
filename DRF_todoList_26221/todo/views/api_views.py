from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from ..models import Todo
from ..serializers import TodoSerializer


class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


class TodoRetrieveAPI(APIView):
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(TodoSerializer(todo).data)


class TodoUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoSerializer(todo).data)


class TodoDeleteAPI(APIView):
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
