from django.shortcuts import render
from account.models import Account

# Create your views here.
def home_screen_view(request):
	# print(request.headers)
	context = {}
	# context['some_string'] = "this is some string that I'm passing to the view"
	# context['some_number'] = 3151351

	# context = {'some_string' :  "This is some string text passing from the view personal app",
    # 'some_number' : 12334
    # } 

	# list_of_values = []
	# list_of_values.append("first entry")
	# list_of_values.append("second entry")
	# list_of_values.append("third entry")
	# list_of_values.append("fourth entry")
	# list_of_values.append("fifth entry")
	# context['list_of_values'] = list_of_values
	accounts = Account.objects.all()
	context['accounts'] = accounts
	return render(request, "personal/home.html", context)
	# return render(request, "base.html", {})



