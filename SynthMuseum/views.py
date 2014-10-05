from django.shortcuts import render, get_object_or_404
from django.views import generic

from SynthMuseum.models import StandardSynthesizer

#def index(request):
#    synths = StandardSynthesizer.objects.all().order_by('manufacturer', 'name')
#    context = {'synths': synths}
#    return render(request, 'SynthMuseum/index.html', context)

def detail(request, m, n):
    synth = get_object_or_404(StandardSynthesizer, manufacturer__iexact=m, name__iexact=n)
    return render(request, 'SynthMuseum/detail.html', {'synth': synth})

class IndexView(generic.ListView):
    model = StandardSynthesizer
    template_name = 'SynthMuseum/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'].order_by('manufacturer', 'name')
        return context
