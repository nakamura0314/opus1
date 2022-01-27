from django.db import models

# djangoでは、datetime.nowの代わりに、timezone.nowで現在日付・時刻を取得する
from django.db import models
from django.utils import timezone

# class 関数名(models.Model):、これはモデルを作る際の定型文


class Day(models.Model):
    """内部的には下記のようなidが存在する、自動的に作成される
    primary_keyは、titleやtextなどに付与することもできる

    id=models.AutoField(primary_key=True)"""
    # 各フィールドの第一引数は、その文字列を指定できる
    # これはその機能の説明とする
    # CharFieldは一文で収まりそうな場合
    title = models.CharField('タイトル', max_length=200)
    # TextFieldは複数行の文字列を保存したい場合
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    """
    python manage.py makemigrations アプリ名
    モデルの変更を伝える

    python manage.py migrate
    変更や作成したモデルを実際に反映させる
    """

    def __str__(self):
        return self.title
