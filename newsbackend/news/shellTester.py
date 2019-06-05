# python manage.py shell
# from news.serializers import NewsSerializer
# from news.models import News


data = {"title": "a", "description": "b", "datestr": "d"}
serializer = NewsSerializer(data=data)
serializer.is_valid()
serializer.save()
serializer.validated_data

data = {
    "title": "test",
    "description": "tb",
    "datestr": "dc",
    # "entities4thisnews": [9,8],
    "entities4thisnews": [
        {
            "entity_type": "PERSON",
            "entity": "Amir",
        },
        {
            "entity_type": "EVENT",
            "entity": "party",
        }
    ]
}

# data = {
#     "title": "g",
#     "description": "g",
#     "datestr": "g",
#     "album_musician": [
#
#         {
#             "entity": "amir",
#             "entity_type": "EVENT"
#         },
#         {
#             "entity": "amir",
#             "entity_type": "EVENT"
#         }
#     ]
# }

data = {
    "title": "g",
    "description": "g",
    "datestr": "g",
    "entities4thisnews": [

        {
            "entity": "amir",
            "entity_type": "EVENT"
        },
        {
            "entity": "amir",
            "entity_type": "EVENT"
        }
    ]
}
