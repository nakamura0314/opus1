from django import forms
from .models import Day


# fomrs.ModelFormは、モデルから自動的に入力欄を作成してくれる
class DayCreateForm(forms.ModelForm):

    # forms.ModelFormの場合は　「class Meta」で詳細設定
    class Meta:
        model = Day
        fields = '__all__'  # 特定のフィールドだけにしたい場合は('title','text','date')とする
