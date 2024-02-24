from django.contrib import admin
from django.urls import path, include

# Импорт настроек и статических файлов Django
from django.conf import settings
from django.conf.urls.static import static

# Определение маршрутов приложения
urlpatterns = [
    # Маршрут для административной панели Django
    path('admin/', admin.site.urls),

    # Включение маршрутов приложения 'main'
    path('', include('main.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
