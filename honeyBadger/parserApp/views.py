from django.http import HttpResponse
from parserApp.models import Customer
from parserApp.parser import writeInModels
from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count

def index(request):
	# Customer.objects.all().delete()
	# writeInModels()
	totalCount = Customer.objects.count()
	totalAmount = Customer.objects.aggregate(Sum('amount'))
	totalName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__lt = 2)
	totalOnceName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__lt = 2)
	totalTwiceName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__lt = 3).filter(count_status__gt = 1)
	totalThriceName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__lt = 4).filter(count_status__gt = 2)
	totalFourName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__lt = 5).filter(count_status__gt = 3)
	totalFiveName = Customer.objects.values('name').annotate(count_status = Count('name')).filter(count_status__gt = 4)
	totalOnceCount = totalOnceName.count()
	totalTwiceCount = totalTwiceName.count()
	totalThriceCount = totalThriceName.count()
	totalFourCount = totalFourName.count()
	totalFiveCount = totalFiveName.count()
	context = {'totalCount': totalCount, 'totalAmount': totalAmount, 'totalName': totalName, 'totalOnceName': totalOnceName,
	'totalTwiceName':totalTwiceName, 'totalThriceName': totalThriceName, 'totalFourName': totalFourName,'totalFiveName':totalFiveName,
	'totalOnceCount': totalOnceCount,'totalTwiceCount':totalTwiceCount, 'totalThriceCount': totalThriceCount,
	'totalFourCount': totalFourCount,'totalFiveCount':totalFiveCount,
	}
	return render(request, 'parserApp/index.html', context)