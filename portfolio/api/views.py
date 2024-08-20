from rest_framework import generics
from django.db.models import Count

from portfolio.api.serializers import PortfolioSerializer
from portfolio.models import Portfolio


class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.annotate(total_portfolios=Count('id'))
    serializer_class = PortfolioSerializer


class PortfolioDetailView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.annotate(total_portfolios=Count('id'))
    serializer_class = PortfolioSerializer
