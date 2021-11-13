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
            nd1 = [int(i) for i in doc1.split(",")]
            nd2 = [int(i) for i in doc2.split(",")]
            doc1_obj = []
            doc2_obj = []
            for idx in nd1:
                for instance in User.objects.all().filter(id=idx):
                    doc1_obj.append(UserSerializer(instance).data)
            for idx in nd2:
                for instance in User.objects.all().filter(id=idx):
                    doc2_obj.append(UserSerializer(instance).data)

            response = {
                "min_time": time,
                "doc1": doc1_obj,
                "doc2": doc2_obj,
            }
            print(response, flush=True)
            return Response(response, status=201)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
