import json
import threading

from rest_framework import generics
from .serializers import NotificationSerializer
from .models import Notifications
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from fcm_django.models import FCMDevice

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    
    def perform_create(self, serializer):
        """Save the post data when creating a new notification."""
        serializer.save()
        return

def create_notification():
    threading.Timer(5.0, create_notification).start()
    title = "What's new?"
    message = "Nothing"

    ## create and save notification in database
    new_notification = Notifications(title="What's new?", read_status=False)
    new_notification.save()

    ## send a push notification
    device = FCMDevice.objects.all().first()
    device.send_message(title, message)

create_notification()

def mark_seen(request):
    payload = request.body
    payload = json.loads(payload.decode('utf-8'))
    id_list = payload["data"].split(",")
    for current_id in id_list:
        notification = get_object_or_404(Notifications, pk=current_id)            
        notification.read_status = True
        notification.save()
    return HttpResponse("OK")

"""
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
#class DetailsView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
"""
