from pk_app.serializers import CurrencySerializer
from pk_app.models import Currency
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination


class CurrencyPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 2


class currencies(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = CurrencyPagination


class currency(ListCreateAPIView):
   serializer_class = CurrencySerializer

   def get_queryset(self):
      queryset = Currency.objects.filter(pk=self.kwargs['id'])
      return queryset