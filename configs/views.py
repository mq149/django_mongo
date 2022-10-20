from datetime import datetime
from djangomongo import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConfigSerializer
import pymongo
from bson.json_util import dumps


class ConfigList(APIView):

    def __init__(self):
        client = pymongo.MongoClient()
        db = client[settings.MONGODB_DBNAME]
        self.collection = db[settings.MONGODB_CONFIG_COLLECTION_NAME]
        print(settings.MONGODB_DBNAME, settings.MONGODB_CONFIG_COLLECTION_NAME)

    def get(self, request):
        config_cursor = self.collection.find()
        list_cursor = list(config_cursor)
        configs = eval(dumps(list_cursor))
        return Response(configs)

    def post(self, request):
        config_serializer = ConfigSerializer(data=request.data)
        if config_serializer.is_valid():
            config_serializer.validated_data['created_at'] = datetime.now()
            self.collection.insert_one(config_serializer.validated_data)
            return Response(config_serializer.data, status=status.HTTP_201_CREATED)
        return Response(config_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

