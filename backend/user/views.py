import datetime
from copy import copy

from rest_framework import viewsets
from rest_framework.response import Response

from backend.operations.graph import get_distance, main_logic
from backend.user.models import User
from backend.user.serializers import UserSerializer

START_TIME = datetime.datetime(2020, 2, 19, 8, 0, 0)


def calculate_start_stop(route_org):
    start = []
    stop = []
    route = route_org[:]
    current_time = START_TIME
    route.insert(0, {"id": 0, "x": 0, "y": 0, "visit_time": 0})
    route = iter(route)
    ob = next(route)
    previous = copy(ob)
    while route:
        try:
            ob = copy(previous)
            next_ob = copy(next(route))
            previous = copy(next_ob)
            time1 = datetime.datetime.strftime(
                copy(current_time) + datetime.timedelta(minutes=get_distance(ob, next_ob)), "%H:%M"
            )
            start.append(time1)
            current_time = (
                current_time
                + datetime.timedelta(minutes=get_distance(ob, next_ob))
                + datetime.timedelta(minutes=next_ob["visit_time"])
            )
            stop.append(datetime.datetime.strftime(current_time, "%H:%M"))
        except StopIteration:
            break
    return start, stop


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

            start1, stop1 = calculate_start_stop(doc1_obj)
            start2, stop2 = calculate_start_stop(doc2_obj)
            response = {
                "min_time": time,
                "doc1": doc1_obj,
                "doc2": doc2_obj,
                "start_doc1": start1,
                "stop_doc1": stop1,
                "start_doc2": start2,
                "stop_doc2": stop2,
            }
            return Response(response, status=201)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
