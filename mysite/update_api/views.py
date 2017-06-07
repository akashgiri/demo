from rest_framework import generics
from .serializers import NotificationSerializer
from .models import Notifications
from rest_framework.response import Response

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer

    print("queryset: ", queryset)
    def perform_create(self, serializer):
        """Save the post data when creating a new notification."""
        serializer.save()
        return

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
