"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from personal.views import home_screen_view, rating
from account.views import registration_view, logout_view, login_view, update_view
from story.views import create_story, my_stories, save_story, delete_story_book, make_public, edit_story, view_story, download_story

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('update/', update_view, name='update'),
    path('create/', create_story, name='create'),
    path('stories/', my_stories, name='stories'),
    path('create/save_story/<int:story_book_id>', save_story, name='save_story'),
    path('stories/save_story/<int:story_book_id>', save_story, name='save_story'),
    path('delete/<int:story_book_id>/', delete_story_book, name='delete_story_book'),
    path('req/<int:story_book_id>/', make_public, name='make_public'),
    path('stories/<int:story_book_id>', edit_story, name='edit_story'),
    path('view/<int:story_book_id>', view_story, name='view_story'),
    path('rate/<int:story_book_id>/<str:rate>/', rating, name='rating'),
    path('download/<int:story_book_id>/<str:title>', download_story, name='download_story')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
