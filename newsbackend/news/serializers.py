from .models import *
from rest_framework import serializers
# from drf_writable_nested import WritableNestedModelSerializer

class EntitySerializer(serializers.ModelSerializer):
    # news = serializers.SlugRelatedField(queryset=News.objects.all(),
    #                                     slug_field='pk', )
    # read_only_fields = ('news',)
    # news_title = serializers.ReadOnlyField(source='news.title')

    class Meta:
        model = Entity
        fields = (
            # 'url',
            "id",
            'releventnews',
            # 'news_title',
            'entity',
            'entity_type',
            'timestamp',
        )


class NewsSerializer(serializers.ModelSerializer):
    entities4thisnews = EntitySerializer(many=True,required=False)

    # entities4thisnews = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='entity-detail',
    # )
    class Meta:
        model = News

        fields = (
            # "url",
            "id",
            "title",
            "description",
            "datestr",
            'timestamp',
            'entities4thisnews',
        )

    # read_only_fields = ('entities4thisnews',)
    def create(self, validated_data):
        entity_data = validated_data.pop('entities4thisnews')
        news = News.objects.create(**validated_data)
        for an_entity in entity_data:
            Entity.objects.create(releventnews=news, **an_entity)
        return news
