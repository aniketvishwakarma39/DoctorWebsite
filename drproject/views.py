from django.http import HttpResponse
from django.shortcuts import render ,redirect
from myapp.models import Appointment

def home_view(request):
    final=0
    data={}
    try:
        n1= int(request.GET['ani1'])
        n2= int(request.GET['ani2'])
        n3= int(request.GET['ani3'])
        final=n1+n2+n3
        data={
            'n1':n1,
            'n2':n2,
            'n3':n3,
            'output':final
        }
        
    except:
        pass
    return render(request,"index.html",data)

def cal_view(request):
    c=''
    try:
        if request.method == "POST":
            m1=eval(request.POST.get('num1'))
            c=m1*0.033
            
        
    except:
        c= "invalid_error" 
        
    return render(request,"cal.html",{'c': c} )

def cal1_view(request):
    return render(request, "cal1.html")

def cal2_view(request):
    b=''
    try: 
        if request.method == "POST":
            m2=eval(request.POST.get('nam' , 0))
            hcal= request.POST.get('hcal')
            if hcal=="Male":
                b=50+2.3*(m2/2.54-60)
            elif hcal== "Female":
                b=45+2.3*(m2/2.54-60)
    except:
            b="Error"
        
        
    return render(request, "cal2.html", {'b' : b})

def cal3_view(request):
    a=''
    try: 
        if request.method == "POST":
            m3=eval(request.POST.get('nam1' , 0))
            m4=eval(request.POST.get('nam2' , 0))
            a= m4/((m3/100)**2)
    except:
            a="Error"
        
        
    return render(request, "cal3.html", {'a' : a})

def cal4_view(request):
    d=''
    try:
        if request.method=="POST":
            a1= eval(request.POST.get('nav1'))
            a2= eval(request.POST.get('nav2'))
            a3= eval(request.POST.get('nav3'))
            hcal= request.POST.get('hcal')
            if hcal=="Male":
                d = 88.362 + (13.397 * a1) + (4.799 * a2) - (5.677 * a3)
                
            elif hcal=="Female":
                d = 447.593 + (9.247 * a1) + (3.098 * a2) - (4.330 * a3)

    except:
        d="errorfound"

    
    return render(request, "cal4.html", {'d':d})

def Book_view(request):
    
    
    message = ""
    try:
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            date = request.POST.get('date')
            time = request.POST.get('time')
            reason = request.POST.get('reason')
            notes = request.POST.get('notes')

            if not name or not phone or not date or not time or not reason:
                message = "❌ Please fill all required fields."
            else:
                Appointment.objects.create(
                    name=name,
                    phone=phone,
                    email=email,
                    date=date,
                    time=time,
                    reason=reason,
                    notes=notes
                )
                message = "✅ Appointment booked successfully!"

    except Exception as e:
        print("Error booking appointment:", e)
        message = "⚠ Something went wrong. Please try again."

    return render(request, "cal5.html",  {"message": message})

def cal6_view(request):
    return render(request, "cal6.html")