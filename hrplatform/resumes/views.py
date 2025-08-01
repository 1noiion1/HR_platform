from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import ResumePermission
from users.models import Role

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [ResumePermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if not hasattr(user, 'profile'):
            return Resume.objects.none()

        if user.profile.role in [Role.ADMIN, Role.HR]:
            return Resume.objects.all()

        return Resume.objects.filter(user=user)