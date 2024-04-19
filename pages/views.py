from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Page
from .serializers import PageSerializer

def index(request):
    return JsonResponse({"message":"Hi Pages App"})

class PageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer    

@api_view(['GET','POST'])
def page_list_create_api(request):
    if request.method=='GET':
        pages=Page.objects.all()
        serializer=PageSerializer(pages, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT', 'DELETE'])
def page_detail_api(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'GET':
        serializer = PageSerializer(page)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        page.delete()
        return Response(status=204)
