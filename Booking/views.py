from django.shortcuts import render
from Booking.models import Movies
from Booking.form import MovieForm


# Create your views here.
def home(request):
    b = Movies.objects.all()
    return render(request,'home.html',{'vmovie':b})


def delete(request,k):
    b = Movies.objects.get(id=k)
    b.delete()
    #return home(request)
    return success(request)


def viewbooking(request,k):
    b = Movies.objects.get(id=k)
    return render(request,'viewbooking.html',context={'b1': b})

def update(request,k):
    b = Movies.objects.get(id=k)
    if (request.method == "POST"):
        form = MovieForm(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
            #return home(request)
            return successfull(request)

    form = MovieForm(instance=b)
    return render(request, 'update.html', context={'f': form})





# def addmovie(request):
#     return render(request,'addmovie.html')




def addmovies(request):
    if (request.method == "POST"):
        t = request.POST['t']
        d = request.POST['d']
        g = request.POST['g']
        p = request.FILES['p']
        b = Movies.objects.create(title=t, director=d, discription=g,image=p)
        b.save()
        return home(request)
    return render(request,'addmovie.html')


def success(request):
        return render(request,'success.html')


def successfull(request):
    return render(request, 'successfull.html')

