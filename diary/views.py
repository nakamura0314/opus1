from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day

# generic.ListViewで一覧作成
# 一覧表示させたいモデルをmodelに格納


class IndexView(generic.ListView):
    model = Day
    """template_name='diary/my_list.html'
    上記のようにしてtemplateを指定することもできる
    template_nameの指定がない場合は、
    モデルを定義したアプリケーション名/モデル名_list.html
    で探している"""
    # ページング処理の際のオブジェクトがtemplateに3件ずつ渡される
    # この場合、一つのページに三件だけデータを渡すようにする
    paginate_by = 3


# generic.CreateViewでデータの作成処理
# LoginRequiredMixinを引数に含むと、これはログイン必須となる
class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    # どのフォームを使うかの指定
    # fields='__all__'とすることもできる
    form_class = DayCreateForm
    # データの追加に成功した場合に、リダイレクトさせるページを指定
    success_url = reverse_lazy('diary:index')


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('diary:index')


class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
    model = Day
