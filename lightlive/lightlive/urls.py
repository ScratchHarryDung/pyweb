from django.contrib import admin
from django.urls import path, include
from homepage import views as homepage

# đoạn   FROM DJANGO.URLS IMPORT PATH   là mình lấy cái gì ra ạ? tại sao lại có include ở phía sau làm gì ạ?
# đoạn   FROM HOMEPAGE IMPORT VIEW AS HOMEPAGE   thì cái khúc as homepage có cần thiết ko ạ? mạng bảo đó là tên, thì e thắc mắc là tên của cái gì ạ?


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage.get_homepage),
]
