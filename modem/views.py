from django.shortcuts import render, redirect
from .forms import AmtcForm, AmtcModel_EskiForm
from .models import AmtcModel, AmtcModel_Eski

def index(request):
	form = AmtcForm()
	if request.method == 'POST':
		form = AmtcForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')
	try:
		obj = AmtcModel.objects.latest('id')
	except:
		obj = None

	soni = AmtcModel.objects.all().count()
	if soni > 100:
		AmtcModel.objects.all().delete()

	context = {'form':form, 'obj':obj}
	return render(request, 'index.html', context)

def last30(request):
	form = AmtcModel.objects.all().order_by('-id')[:30]
	context = {'form':form}
	return render(request, 'last30.html', context)

def eski_olt(request):
	form = AmtcModel_EskiForm()
	if request.method == 'POST':
		form = AmtcModel_EskiForm(request.POST)

		if form.is_valid():
			form.save()
	try:
		obj = AmtcModel_Eski.objects.latest('id')
	except:
		obj = None
	context = {'form':form, 'obj':obj}
	return render(request, 'eski_olt.html', context)

def last30_eski(request):
	form = AmtcModel_Eski.objects.all().order_by('-id')[:30]
	context = {'form':form}
	return render(request, 'eski_last30.html', context)