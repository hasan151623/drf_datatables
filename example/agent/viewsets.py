from rest_framework import viewsets

from drf_datatables.filters import CustomSearchFilter, CustomOrderingFilter, GenericFilter
from drf_datatables.paginations import DataTablePagination
from example.agent import serializers
from example.agent.models import TopUp, Agent


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = serializers.AgentSerializer
    pagination_class = DataTablePagination
    filter_backends = (CustomSearchFilter, CustomOrderingFilter, GenericFilter)
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    filter_fields = ['category', 'payment_policy']
    ordering_fields = search_fields + filter_fields
    ordering = ['-id']


class TopUpViewSet(viewsets.ModelViewSet):
    queryset = TopUp.objects.all().select_related('agent', 'created_by', 'approved_by')
    serializer_class = serializers.TopUpSerializer
    pagination_class = DataTablePagination
    filter_backends = (CustomSearchFilter, CustomOrderingFilter, GenericFilter)
    search_fields = ['agent__first_name', 'agent__last_name', 'created_by__first_name', 'created_by__last_name',
                     'approved_by__first_name', 'approved_by__last_name']
    filter_fields = ['payment_mode', 'status']
    ordering_fields = search_fields + filter_fields
    ordering = ['-id']

