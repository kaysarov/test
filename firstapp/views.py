from django.shortcuts import render
from django.utils import timezone
from .models import Post
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import django
import numpy as np
import matplotlib.pyplot as plt


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'firstapp/post_list.html', {'posts': posts})


def simple(request):
    x = np.random.random(1000)
    num_bins = 10
    fig, ax = plt.subplots()
    ax.hist(x, num_bins)
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
