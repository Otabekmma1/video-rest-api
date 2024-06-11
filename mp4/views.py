from .models import DowloandVideo
from .serializers import VideoSerializer

from rest_framework import viewsets, permissions

class VideoApiList(viewsets.ModelViewSet):
    queryset = DowloandVideo.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

