from rest_framework.filters import SearchFilter, OrderingFilter, BaseFilterBackend


class GenericFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_fields = getattr(view, 'filter_fields', None)
        query_params = request.GET.dict()
        filter_terms = {}
        for field in filter_fields:
            if field in query_params:
                filter_terms[field] = query_params[field]

        if not filter_terms:
            return queryset
        try:
            queryset = queryset.filter(**filter_terms)
        except Exception as e:
            raise e
        return queryset


class CustomSearchFilter(SearchFilter):
    search_param = 'search[value]'


class CustomOrderingFilter(BaseFilterBackend):
    ordering_param = 'order[0][column]'

    def get_ordering(self, request, view):
        params = request.query_params.get(self.ordering_param)
        valid_fields = getattr(view, 'ordering_fields', None)
        if valid_fields and params and params != '0':
            fields = valid_fields[int(params)]
            if request.query_params.get('order[0][dir]') == 'desc':
                fields = '-' + fields
            return fields

    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, view)

        if ordering:
            return queryset.order_by(ordering)
        return queryset

