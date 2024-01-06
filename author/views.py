from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AutherSerializer


class AuthorCreate(APIView):
    def post(self, request):
        data = request.data
        serializer = AutherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Auther created sucessfully"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetails(APIView):
    def get(self, request, *args, **kwargs):
        try:
            params_id = self.kwargs.get("id")
            author = Author.objects.get(id=params_id)

            serializer = AutherSerializer(instance=author)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For book table
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreate(APIView):
    def post(self, request):
        data = request.data
        author_id = data.get("author_id")
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return Response(
                {"error": "Author not found."}, status=status.HTTP_404_NOT_FOUND
            )

        data = {
            "title": data.get("title"),
            "author": author_id,
            "publication_date": data.get("publication_date"),
        }

        title = data.get("title")
        publication_date = data.get("publication_date")
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            Book.objects.create_book(
                title=title, author_id=author_id, publication_date=publication_date
            )
            return Response(
                {"message": "Book created sucessfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetails(APIView):
    def get(self, request, *args, **kwargs):
        try:
            book_id = self.kwargs.get("id")
            book = Book.objects.get(id=book_id)
            serializer = BookSerializer(instance=book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
