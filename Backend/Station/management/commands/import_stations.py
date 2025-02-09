import csv
from django.core.management.base import BaseCommand
from Station.models import Station

class Command(BaseCommand):
    help = 'Import products from a CSV file into the database'
    
    def handle(self, *args, **kwargs):
        with open('./Station/management/commands/stations.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Station.objects.create(
                    id=row['id'], 
                    stationName=row['stationName'], 
                    trainLine=row['trainLine'], 
                    leftETA=10, 
                    rightETA=3, 
                    leftCurrentDensity="Heavy", 
                    rightCurrentDensity="Light", 
                    leftHistory="", 
                    rightHistory="", 
                    cctv="", 
                    isOperating=True, 
                    stationIMG=""
                )
        self.stdout.write(self.style.SUCCESS("succefully imported"))