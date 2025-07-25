from django.shortcuts import redirect, render
from .forms import Admission, EnquiryForm, ContactMessageForm

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # replace with actual thank you page
    else:
        form = EnquiryForm()
    return render(request, 'enquiry.html', {'form': form})


def faculties(request):
    return render(request, 'faculties.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def submit_enquiry(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # or show a success message
    return redirect('enquiry')

def policy(request):
    return render(request, 'policy.html')

def admission(request):
    if request.method == 'POST':
        data = request.POST
        admission = Admission(
            name=data.get('name'),
            address=data.get('address'),
            contact=data.get('contact'),
            mail=data.get('mail'),
            dob=data.get('dob'),
            gender=data.get('gender'),
            occupation=data.get('occupation'),
            guardian_name=data.get('gname'),
            guardian_occupation=data.get('goccupation'),
            guardian_contact=data.get('gcontact'),

            institute1=data.get('institute1'),
            class_sem1=data.get('class_sem1'),
            stream1=data.get('stream1'),
            passing_year1=data.get('passing_year1'),
            percentage1=data.get('percentage1'),

            institute2=data.get('institute2'),
            class_sem2=data.get('class_sem2'),
            stream2=data.get('stream2'),
            passing_year2=data.get('passing_year2'),
            percentage2=data.get('percentage2'),

            institute3=data.get('institute3'),
            class_sem3=data.get('class_sem3'),
            stream3=data.get('stream3'),
            passing_year3=data.get('passing_year3'),
            percentage3=data.get('percentage3'),

            subjects=data.get('subjects'),
            references=','.join(request.POST.getlist('reference')),  # multiple checkboxes
            refname=data.get('refname')
        )
        admission.save()
        return redirect('thank_you')  # add this url pattern

    return render(request, 'admission.html')


def gallery(request):
    image_range = range(1, 26)
    return render(request, 'gallery.html', {'image_range': image_range})

def term_serv(request):
    return render(request, 'terms_serv.html')

def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # optional success page
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

def subject(request):
    return render(request, 'subject.html')

def thank_you(request):
    return render(request, 'thank_you.html')