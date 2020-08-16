import django_filters
from django_filters import DateFilter, CharFilter, TimeFilter, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from .models import Link

class LinkFilter(django_filters.FilterSet):
    print("in link filter")
    link_text = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Link
        fields = {
        'id':['iexact'],
        }
