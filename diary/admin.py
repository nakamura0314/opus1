from django.contrib import admin
from .models import Day

# 下記のようにすることで、Dayモデルをadminで管理することができる
admin.site.register(Day)
