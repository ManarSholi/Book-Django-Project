from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer,BookMiniSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# class Another(View):
#
#     books = Book.objects.filter(is_published=True)
#     output = ''
#
#     for book in books:
#         output += f'We have {book.title} with ID {book.id} <br/>'
#
#     def get(self, request):
#         return HttpResponse(self.output)
#

# def first(request):
#     books = Book.objects.all()
#
#     return render(
#         request,
#         'first_temp.html',
#         {'books': books}
#     )


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
