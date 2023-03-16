from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import *
from .models import *


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class WorkerListCreateView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
class WorkerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkListCreateView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
class WorkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
class StatusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


@api_view(['GET'])
def get_status(request):
    return Response('Ура, всё прошло успешно!', status = status.HTTP_200_OK)
