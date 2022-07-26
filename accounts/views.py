from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.
from accounts.models import Contact, Reserve, Table
from first.models import Order, Food


def registration(request):
    if request.method=='POST':
        print('in post')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if (password==password2):
           if User.objects.filter(username=username).exists():
               print('one')
               messages.info(request,'username already taken')
               return redirect('register')
           # elif User.objects.filter(email=email).exists():
           #     print('email already taken')
           else:
              print('ok')
              user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
              print(user.first_name)
              # user.save()
              messages.info(request,'user sucessfully created')
              login(request)
              return redirect('login')
        else:
            print('user not created')
            messages.error(request, 'user not created')
        return redirect('register')

    else:

        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'invalid password or username')
            return redirect('login')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dash.html')

def logout1(request):
    logout(request)
    return redirect('home')

def contact(request):
    foods = Food.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        quantity = request.POST.get('quantity')
        meal = request.POST.get('meal')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        name = request.POST.get('first_name')

        print(message)
        if request.user.is_authenticated:
            user_id= request.user.id
            has_contacted = Contact.objects.all().filter(user_id= user_id)
            if has_contacted:
                message.error(request, 'you have already made an order for this food')
                return redirect('food'+ user_id)

        order = Order(
          # food=meal,
          quantity=quantity,
          address=address,
          message= message,
          email= email,
          phone=phone,
          name=name
        )
        order.save

        send_mail(
            'The food order',
            'Thank you, you have made an order for the' + " " + meal + 'table',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        send_mail(
            'The food order',
            name+" " + ' made an order for the meal' + " " + meal,
            settings.EMAIL_HOST_USER,
            ['ndamlami470@gmail.com'],
            fail_silently=False,
        )
        print('good mail')
        return redirect('home')

    else:
        return render(request,'contact.html', )


def reservation(request):
   rev = Reserve.objects.all()
   if request.method == 'POST':
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         name= request.POST.get('name')
         date = request.POST.get('reserve_date')
         message = request.POST.get('message')
         user_id = request.POST.get('user_id')
         tablename = request.POST.get('tablename')

         if request.user.is_authenticated:
             user_id = request.user.id
             has_contacted = Contact.objects.all().filter(user_id=user_id)
             if has_contacted:
                 message.error(request, 'you have already made an inquirfy for this house')
                 return redirect('food' + user_id)

             reserve = Reserve(
               # food=meal,
               message=message,
               email=email,
               phone=phone,
               reserve_date=date,
               tablename=Reserve.tablename.name,
               name=name

               )
             reserve.save()

             send_mail(
               'The table order',
               'Thank you' + " " +name + " "+'you have made an order for the' +" "+ tablename +'table',
                settings.EMAIL_HOST_USER,
               [email,'ndamlami470@gmail.com'],
               fail_silently=False,
             )

             send_mail(
                 'The table order',
                  name + " " + ' made an order for the table' + " " + tablename,
                  settings.EMAIL_HOST_USER,
                  ['ndamlami470@gmail.com'],
                  fail_silently=False,
             )
              # print('good mail')
             return redirect('home')

         else:
          return render(request, 'reserve.html', {'rev':rev} )





