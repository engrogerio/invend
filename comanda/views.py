from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Evento
from app.models import FileExam
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class ComandaView(ListView):

    #template_name = "change_list.html"
    paginate_by = 10
    model = Evento
    context_object_name = "Listagem de Comandas"
    queryset = Evento.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ComandaView, self).get_context_data(**kwargs)
        list_exam = FileExam.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context