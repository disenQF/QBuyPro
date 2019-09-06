#!/usr/bin/python3
# coding: utf-8
from rest_framework import serializers, viewsets

from actives.models import ActiveModel, ActiveGoodsModel

class ActiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveModel
        fields = ('title', 'start_time', 'end_time', 'img1')


class ActiveGoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActiveGoodsModel
        fields = ('goods', 'active', 'rate')


class ActiveAPIView(viewsets.ModelViewSet):
    queryset = ActiveModel.objects.all()
    serializer_class =  ActiveSerializer


class ActiveGoodsAPIView(viewsets.ModelViewSet):
    queryset = ActiveGoodsModel.objects.all()
    serializer_class =  ActiveGoodsSerializer