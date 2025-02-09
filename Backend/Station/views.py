from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db import OperationalError, connection

from .models import Station
from .serializers import StationSerializer

# Create your views here.
@api_view(['GET'])
def get_all_station(request):
    if check_database_status():
        stations = Station.objects.values('id', 'stationName', 'trainLine', 'isOperating')
        return Response(stations)
    else:
        return Response(
            {"error": "Database is currently unavailable. Please try again later."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    # except DatabaseError:
    #     return Response(
    #         {"error": "Database error occured while fetching stations."},
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #     )
    # except Exception as e:
    #     return Response(
    #         {"error": f"An unexpected error occured: {str(e)}"},
    #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #     )

@api_view(['GET'])
def get_station(request, id):
    station = get_object_or_404(Station, id = id)
    serializer = StationSerializer(station)
    return Response(serializer.data)


def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False