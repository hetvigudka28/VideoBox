from django.shortcuts import render, redirect
from videoapp import models
from videoapp.models import Videos

# Create your views here.
def homepage(request):
    videos=Videos.objects.all()
    return render(request,'homepage.html',{"videos":videos})

def upload(request):
    if request.method=="POST":
        title= request.POST["title"]
        desc = request.POST['desc']
        thumbnail =  request.FILES['thumbnail']
        video =  request.FILES['video']
        videosobj=Videos(user=request.user, title=title, description=desc, thumbnail=thumbnail, video=video)
        videosobj.save();
        return redirect('homepage')

    return render(request, 'upload.html')

def video(request,pk):
    video = Video.objects.get(pk=pk)
    print(video)
    return render(request,'videoView.html',{'video':video})
