from django.http import HttpResponse
from django.shortcuts import render
from .forms import my_form
from time import time, sleep
from .models import file_and_pic
import aiohttp
import asyncio

# Create your views here.
def main(request):
    form = my_form()
    context = {'form': form,
               }
    template = 'django_async/main.html'
    if request.method == "POST":
        start_time = time()
        submition = my_form(data=request.POST,files=request.FILES) 
        if submition.is_valid():
            sleep(5)
            submition.save()
            return HttpResponse('Form Submitted: (time in sec %f)' % (time()-start_time))

    return render(request, template, context=context)


# play around async
async def main_async(request):
    async def get_data():
        data = '<h1>this is async</h1>'
        await asyncio.sleep(3)
        return data
    # Removed await so line 32 is going to
    start_time = time()
    data = asyncio.create_task(get_data())
    data2 = asyncio.create_task(get_data())
    await data
    await data2
    end_time = time()
    html_string = '<h2>%f</h2>' % (end_time - start_time)
    piece = str(data.result())+ str(data2.result())
    return HttpResponse(piece+html_string)


def main_sync(request):
    html = """
    <h1>this is sync</h1>
    """

    return HttpResponse(html)