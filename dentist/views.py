from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'home.html', {})
def contact(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #send an email
        send_mail(
            your_name,
            subject,
            message,
            email,
            ['wambuakenitious@gmail.com']

        )
        return render(request, 'contact.html', {'your_name':your_name})

    else:
        return render(request, 'contact.html', {})
def doctors(request):
    return render(request, 'doctors.html', {})

# Create your views here.
def blog(request):
    return render(request, 'blog.html', {})

def services(request):
    return render(request, 'services.html', {})

def doctors(request):
    return render(request, 'doctors.html', {})

def about(request):
    return render(request, 'about.html', {})

def appointment(request):
    if request.method == "POST":
        appointment_name = request.POST['appointment_name']
        appointment_email = request.POST['appointment_email']
        appointment_type = request.POST['appointment_type']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']
        phone = request.POST['phone']

        #send an email
        #appointment ='Name:" + appointment_name + " Phone: " +phone + "Email:" + appointment_email + "Appointment:" +appointment_type+ "Date" +appointment_date+ "Time:"+appointment_time'
        #send_mail(
       #     'Appointment Request',
           # appointment,
          #  appointment_email,
          #  ['wambuakenitious@gmail.com']

      #  )

        return render(request, 'appointment.html',{
            'appointment_name': appointment_name,
            'appointment_email': appointment_email,
            'appointment_type': appointment_type,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            'phone': phone

        })
    else:
        return render(request, 'home.html', {})


