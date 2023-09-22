from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import SEL4C.app1.models as models
import SEL4C.app1.serializers as serializers


class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class AdminViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer


class EmprendedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Usuarios to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Emprendedor.objects.all()
    serializer_class = serializers.EmprendedorSerializer

