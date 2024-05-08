import json

from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, views
from django.db.models import Q
from django.http import Http404

from .models import McFoodInfo
from .serializers import McFoodInfoSerializer


class AllProductsViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    queryset = McFoodInfo.objects.all()
    serializer_class = McFoodInfoSerializer

    # def list(self, request, *args, **kwargs):
    #     # run once to fill in the data and clean it a little
    #     with open('menu\parce_results.txt', 'r') as fb:
    #         parce_results = json.load(fb)
    #     for p in parce_results:
    #         McFoodInfo.objects.create(**p)
    #     for product in self.queryset:
    #         product.name            = product.name.replace('\n','').replace('\t','')
    #         product.description     = product.description.replace('\n','').replace('\t','')
    #         product.calories        = product.calories.replace('\n','').replace('\t','')
    #         product.fats            = product.fats.replace('\n','').replace('\t','')
    #         product.carbs           = product.carbs.replace('\n','').replace('\t','')
    #         product.proteins        = product.proteins.replace('\n','').replace('\t','')
    #         product.unsaturated_fats= product.unsaturated_fats.replace('\n','').replace('\t','')
    #         product.sugar           = product.sugar.replace('\n','').replace('\t','')
    #         product.salt            = product.salt.replace('\n','').replace('\t','')
    #         product.portion         = product.portion.replace('\n','').replace('\t','')
    #         product.save()
    #     return Response()


class ProductViewSet(views.APIView):
    queryset = McFoodInfo.objects.all()
    serializer_class = McFoodInfoSerializer
    lookup_field = '__all__'

    def get(self, request, product_name):
        products = McFoodInfo.objects.filter(Q(name__icontains=product_name)|Q(name__istartswith=product_name)|Q(name__iendswith=product_name)|Q(name__iexact=product_name))
        product_name = product_name.capitalize()
        products2 = McFoodInfo.objects.filter(
            Q(name__icontains=product_name) | Q(name__istartswith=product_name) | Q(name__iendswith=product_name) | Q(
                name__iexact=product_name))

        products = products.union(products2)
        if not products.exists():
            raise Http404(f"No such products that correspond to '{product_name}'")
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)

class ProductDetailViewSet(views.APIView):
    queryset = McFoodInfo.objects.all()
    serializer_class = McFoodInfoSerializer

    def get(self, request, product_name, product_field):
        products = McFoodInfo.objects.filter(
            Q(name__icontains=product_name) | Q(name__istartswith=product_name) | Q(name__iendswith=product_name) | Q(
                name__iexact=product_name))
        product_name = product_name.capitalize()

        products2 = McFoodInfo.objects.filter(
            Q(name__icontains=product_name) | Q(name__istartswith=product_name) | Q(name__iendswith=product_name) | Q(
                name__iexact=product_name))

        products = products.union(products2)
        product = products.first()
        try:
            serializer = self.serializer_class(product)
            res = serializer.data.pop(product_field)
        except AttributeError or KeyError:
            raise Http404(f"No field '{product_field}' for '{product_name}'")
        except Exception as e:
            raise Http404(f"No field '{product_field}' for '{product_name}'")

        return Response(res)