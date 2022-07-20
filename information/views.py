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


def set_department_in_validated_data(validated_data):
    department = validated_data['department']
    validated_data['department'], created = getattr(Department, 'objects').get_or_create(**department)


class EmployeeSerialize(serializers.ModelSerializer):
    department = serializers.CharField(source='department.name')

    class Meta:
        model = Employee
        fields = ['name', 'email', 'department']

    def create(self, validated_data):
        set_department_in_validated_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        set_department_in_validated_data(validated_data)
        return super().update(instance, validated_data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = getattr(Employee, 'objects').all()
    serializer_class = EmployeeSerialize

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action != 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

