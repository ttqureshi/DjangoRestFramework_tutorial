# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# urlpatterns = [
#     path("", views.api_root),
#     path("snippets/", views.SnippetList.as_view(), name="snippet-list"),
#     path("snippets/<int:pk>/", views.SnippetDetail.as_view(), name="snippet-detail"),
#     path(
#         "snippets/<int:pk>/highlight",
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight',
#     ),
#     path("users/", views.UserList.as_view(), name="user-list"),
#     path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

###################################################
#       Binding ViewSets to URLs explicitly       #
###################################################
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
# from django.urls import path

# from snippets.views import api_root, SnippetViewSet, UserViewSet

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])


###################################################
#                  Using Routers                  #
###################################################
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a router and register out ViewSets with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]

######## IMPORTANT COMMENT ########
"""
The DefaultRouter class we're using also automatically
creates the API root view for us, so we can now delete
the api_root function from our views module.

For the purpose of reference in the future, I am not
deleting api_root function, just commenting it out.
"""