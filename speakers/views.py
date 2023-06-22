from django.shortcuts import render,redirect
from speakers.models import Speaker
from speakers.forms import SpeakerForm

# Create your views here.
def speak(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
        else:
            form = SpeakerForm()
        return render(request,'index.html',{'form':form})
    return render(request,'index.html',{'form':form})

def show(request):
    speakers = Speaker.objects.all()
    return render(request,'show.html',{'speakers':speakers})

def edit(request,id):
    speaker = Speaker.objects.get(id=id)
    return render(request,'edit.html',{'speaker': speaker})

def update(request,id):
    speaker = Speaker.objects.get(id=id)
    form =SpeakerForm(request.POST,instance=speaker)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'speaker':speaker})

def delet(request,id):
    speaker = Speaker.objects.get(id=id)
    speaker.delete()
    return redirect("/show")
