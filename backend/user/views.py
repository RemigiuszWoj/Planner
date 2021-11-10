from rest_framework import viewsets
from rest_framework.response import Response

from backend.operations.graph import main_logic
from backend.user.models import User
from backend.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        if request.data.get("flag", False):
            way, time = main_logic(request.data)
            doc1, doc2 = way.replace("[", "").replace("]", "").replace(" ", "").split("-")
            response = {
                "min_time": time,
                "doc1": doc1,
                "doc2": doc2,
            }
            return Response(response, status=201)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
