import json

from rest_framework.response import Response
from rest_framework import viewsets, mixins

from .models import McFoodInfo
from .serializers import McFoodInfoSerializer


class AllProductsViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    queryset = McFoodInfo.objects.all()
    serializer_class = McFoodInfoSerializer

    # def list(self, request):
    #     serialized = self.serializer_class(self.queryset, many=True).data
    #     return Response(serialized)
    #
    # def list(self, request, *args, **kwargs):
        # run once to fill in the data
        # with open('menu\parce_results.txt', 'r') as fd:
        #     data = json.load(fd)
        #
        # for entry in data:
        #     unsaturated_fats = entry['unsaturated fats']
        #     entry['unsaturated_fats'] = unsaturated_fats
        #     del entry['unsaturated fats']
        #     McFoodInfo.objects.create(**entry)
        # return Response(data=self.queryset)