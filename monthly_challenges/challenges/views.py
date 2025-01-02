from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
#from django.template.loader import render_to_string

# Create your views here.

monthly_challenges= {
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day!",
    "april":"Eat no meat for the entire month!",
    "may":"Walk for at least 20 minutes every day!",
    "june":"Learn Django for at least 20 minutes every day!",
    "july":"Eat no meat for the entire month!",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn Django for at least 20 minutes every day!",
    "october":"Eat no meat for the entire month!",
    "november":"Walk for at least 20 minutes every day!",
    "december":None 
}

def index(request):
    #list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
     })

    """for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data= f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)"""

 

"""def january(request):
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
"""

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]  #because it is a list and list start with index zero. So month=1 
    #then month-1=1-1=0 which redirect to January otherwise it is directed to February. 
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenges/january
    return HttpResponseRedirect(redirect_path)


"""def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)
"""

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text":challenge_text,
            "month_name": month
        })
        #response_data = f"<h1>{challenge_text}</h1>"
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        return Http404()   


