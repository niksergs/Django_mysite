from django.http import Http404

from rest_framework.views import APIView        # Импорт базового класса
from rest_framework import mixins               # Импорт миксинов
from rest_framework import generics             # Импорт дженериков
from rest_framework import filters              # Импорт фильтров для организации поиска
from rest_framework import permissions          # Импорт параметров доступа к представлению
from .permissions import IsAuthorOrReadOnly     # Импорт кастомных параметров доступа к представлению
from django_filters.rest_framework import DjangoFilterBackend   # Импорт django-filter
from rest_framework.response import Response
from rest_framework import status

from blog.models import Post
from .serializers import PostSerializer


"""Базовые классы"""
# class PostList(APIView):
#     """Представление для отображения списка постов модели Post,
#     на основе базового класса"""
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetail(APIView):
#     """Представление для отображения конкретного объекта модели Post,
#     на основе базового класса"""
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         queryset = self.get_object(pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""Миксины"""
# class PostList(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                generics.GenericAPIView):
#     """Представление на отображение списка постов и создание экземпляра записи поста модели Post
#     на основе миксинов"""
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class PostDetail(mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  generics.GenericAPIView):
#     """Представление на отображение, обновление и удаление конкретного поста модели Post
#         на основе миксинов"""
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


"""Дженерики - переопределенные базовые классы"""
class PostList(generics.ListCreateAPIView):
    """Представление на отображение списка постов и создание экземпляра записи поста модели Post
    на основе дженериков"""
    permission_classes = [IsAuthorOrReadOnly]       # Определяем права доступа к данному представлению
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Устанавливаем фильтрацию, если она не установлена по умолчанию в настройках
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']                   # Определяем поля подлежащие фильтрации
    search_fields = ['body', 'author__username']    # Определяем поля поддерживающие поиск
    # search_fields = ['body', 'author__profile__bio']
    ordering_fields = ['author_id', 'publish']      # Определяем поля поддерживающие упорядочивание
    ordering = ['body']                             # Определяем поля упорядочивающиеся по умолчанию

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Представление на отображение, обновление и удаление конкретного поста модели Post
    на основе дженериков"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]  # Определяем права доступа к данному представлению
    # Данное представление будет доступно только пользователям с правами администратора
    # permission_classes = [permissions.IsAdminUser]    # Определяем права доступа к данному представлению


class UserPostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)
