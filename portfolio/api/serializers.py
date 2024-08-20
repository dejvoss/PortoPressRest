from rest_framework import serializers
from portfolio.models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    total_portfolios = serializers.IntegerField()
    class Meta:
        model = Portfolio
        fields = ['title', 'short_description', 'image', 'live_page', 'github_repo', 'created_at', 'total_portfolios']
