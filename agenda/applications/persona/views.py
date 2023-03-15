from django.shortcuts import render

from django.views.generic import ListView, TemplateView

#
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView

#
from .models import Person
from .serializers import PersonSerializer


class ListaPersonas(ListView):

    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()



class PersonListView(TemplateView):

    template_name = 'persona/lista.html'


class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__incontains=kword
        )


class PersonCreateView(CreateAPIView):

    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDeleteView(DestroyAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()