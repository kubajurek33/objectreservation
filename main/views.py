from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from .models import Reservation, UsersCustomuser
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url="/login")
def home(request):
    #today = str(date.today() + timedelta(days=-1))
    d = datetime.now()
    today = d.strftime("%Y-%m-%d")
    context = {
        'date': today,
    }
    return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {"form": form})\

@login_required(login_url="/login")
def editprofile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Twój profil został zaaktualizowany!')
            return redirect('/home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})

@login_required(login_url="/login")
def ownreservations(request):
    currentuser = request.user.id
    reservations = Reservation.objects.filter(user_id=currentuser)
    context = {
        'reservations': reservations
    }
    return render(request, 'ownreservations.html', context)

@login_required(login_url="/login")
def addreservation(request, date):
    user = request.user
    d = datetime.now()
    today = d.strftime("%Y-%m-%d")
    start_avaible = [
        "15:00","15:30","16:00","16:30","17:00","17:30"
    ]
    end_avaible = [
        "15:30", "16:00", "16:30", "17:00", "17:30","18:00"
    ]
    ts = [
        "15:00","15:30","16:00","16:30","17:00","17:30"
    ]
    te = [
        "15:30", "16:00", "16:30", "17:00", "17:30","18:00"
    ]

    alltimelist = zip(ts, te)
    TimeCheck(start_avaible, end_avaible, date)

    if request.method == "POST":
        if "submit_date" in request.POST:
            if request.POST.get('date') == "":
                return redirect('/addreservation/' + today)
            else:
                return redirect('/addreservation/' + request.POST.get('date'))

    if request.method == "POST":
        print(request.POST.get)
        time_choosed = request.POST.getlist("time")
        if not time_choosed:
            messages.warning(request,'Nie wybrano czasu rezerwacji!')
            return redirect('/addreservation/' + today)
        for i in range(len(time_choosed)-1):
            a = ts.index(time_choosed[i])
            b = ts.index(time_choosed[i+1])
            if b-a != 1:
                messages.warning(request,'Wybierz jeden przedział czasu!')
                print(today)
                return redirect('/addreservation/' + today)
            
        time_start = time_choosed[0]
        num = ts.index(time_choosed[len(time_choosed)-1])
        time_end = te[num]
        g1 = datetime.strptime(time_start, "%H:%M")
        g2 = datetime.strptime(time_end, "%H:%M")
        length = (g2-g1).total_seconds()/3600
        print(length)
        print(length)
        print(length)
        print(length)
        price = length*30
        Reservation.objects.get_or_create(
            time_start = time_start,
            time_end = time_end,
            user = UsersCustomuser.objects.get(id=user.id),
            date = date,
            price=price,
        )
        messages.success(request, "Zarezerwowano obiekt w godzinach od "+time_start+" do "+time_end+"!")
        return redirect('home')

    return render(request, 'reservation.html', {
        'alltimelist':alltimelist,
        'starttime':start_avaible,
        'endtime':end_avaible,
        'today':today,
        'date':date,
    })

def TimeCheck(ts,te, date):
    t1=[]
    t2=[]
    for i in ts:
        if Reservation.objects.filter(date=date, time_start=i).count()>0:
            #obj = get_object_or_404(Reservation, time_start=i)
            obj = Reservation.objects.filter(date=date, time_start=i).first()
            start = obj.time_start
            end = obj.time_end
            a = ts.index(start)
            b = te.index(end)
            for j in range(a, b+1):
                t1.append(ts[j])
                t2.append(te[j])
                print("abcx")

    for x in t1:
        ts.remove(x)
    for y in t2:
        te.remove(y)

    timelist = zip(ts,te)
    return timelist

def redirect_to_today(request):
    d = datetime.now()
    today = d.strftime("%Y-%m-%d")
    return redirect('/addreservation/' + today)