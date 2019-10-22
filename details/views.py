from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm

from details.models import score, attendance


def scores(request):
    user = request.user
    scores = score.objects.filter(user=user)
    scores_dict = {"scores":scores}
    return render(request, 'details/scores.html', scores_dict)


def attendances(request):
    user = request.user
    attendances = attendance.objects.filter(user=user)
    attendances_dict = {"attendances":attendances}
    return render(request, 'details/attendance.html', attendances_dict)


def userinfo(request):
   return render(request, 'details/userinfo.html')


def editinfo(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('userinfo')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form':form}
        return render(request, 'details/editinfo.html', args)



