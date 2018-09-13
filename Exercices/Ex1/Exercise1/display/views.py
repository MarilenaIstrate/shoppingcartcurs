from django.shortcuts import render
from .models import Users

# Create your views here.
def users_list(request):
    all_users = Users.objects.all()
    print(all_users)
    context = {
        'all_users': all_users,
    }
    return render(request, 'display/show_users.html', context)