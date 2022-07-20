from django.views import generic

from information.models import Employ


class EmployListView(generic.ListView):
    model = Employ
