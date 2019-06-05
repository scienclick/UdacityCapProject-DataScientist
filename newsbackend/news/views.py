from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import News
from .models import Entity

from .serializers import NewsSerializer
from .serializers import EntitySerializer
from django_filters import rest_framework as filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    name = 'news-list'

    filter_fields = (
    )

    ordering_fields = (
        'timestamp',

    )
    search_fields = (
        'title',
        'description',
    )


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    name = 'news-detail'


class EntityFilter(filters.FilterSet):
    # 5 / 23 / 2019
    from_timestamp_date = DateTimeFilter(
        field_name='timestamp', lookup_expr='gte')
    to_timestamp_date = DateTimeFilter(
        field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Entity
        fields = (
            'entity_type',
        )

class EntityList(generics.ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    name = 'entity-list'

    filter_class = EntityFilter


    ordering_fields = (
        'timestamp',
    )
    search_fields = (
        'entity',
    )


class EntityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    name = 'entity-detail'


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    # permission_classes = (
    #     IsAdminUser,
    # )


    def get(self, request, *args, **kwargs):
        return Response({
            'news': reverse(NewsList.name, request=request),
            'entity': reverse(EntityList.name, request=request),

        })