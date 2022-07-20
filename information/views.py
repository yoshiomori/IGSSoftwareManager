from django.views import generic
from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated

from information.models import Employee, Department


class EmployeeListView(generic.ListView):
    model = Employee


class DepartmentSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['name']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = getattr(Department, 'objects').all()
    serializer_class = DepartmentSerialize
    permission_classes = [IsAuthenticated]


class EmployeeSerialize(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']

    def create(self, validated_data):
        department = validated_data['department']
        validated_data['department'], created = getattr(Department, 'objects').get_or_create(**department)
        return getattr(Employee, 'objects').create(**validated_data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = getattr(Employee, 'objects').all()
    serializer_class = EmployeeSerialize
    permission_classes = [IsAuthenticated]
