from django.contrib.auth.models import User, Group
import SEL4C.app1.models as modelos
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelos.Admin
        fields = ['username', 'correo', 'firstname', 'lastname']


class EmprendedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = modelos.Emprendedor
        fields = ['username', 'correo', 'firstname','lastname', 'degree', 'institution', 'gender', 'age', 'country', 'studyField']


