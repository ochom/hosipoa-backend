from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bugs import models, serializers


class BugsAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Bug.objects.all().order_by('-created')
    serializer_class = serializers.BugSerializer

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, updated_by=self.request.user)


class RepliesAPI(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Replies.objects.all().order_by('-created')
    serializer_class = serializers.RepliesSerializer

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, updated_by=self.request.user)


class BugReplies(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RepliesSerializer

    def get_queryset(self):
        return models.Replies.objects.filter(bug_id=self.kwargs.get('bug_id'))

