from django.urls import path
from .views import *

urlpatterns = [
    path("author_list/", AuthorListCreateView.as_view(), name="Auther-list"),
    path("authorcreate/", AuthorCreate.as_view(), name="Authorcreate"),
    path("authordetalis/<int:id>/", AuthorDetails.as_view(), name="Authordetals"),
    path("book_list/", BookListCreateView.as_view(), name="Book-list"),
    path("bookcreate/", BookCreate.as_view(), name="Bookcreate"),
    path("bookdetalis/<int:id>/", BookDetails.as_view(), name="Bookdetals"),
]
