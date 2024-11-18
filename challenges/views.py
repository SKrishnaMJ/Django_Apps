from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenge = {
    "january": "Apply to more than 10 jobs per day",
    "february": "Get atleast 14 interviews in this month!",
    "march": "Get an offer letter by the end of this month!",
    "april": "Start looking at cars to buy (a Merc model)",
    "may": "Prepare for graduationd and start looking at 1bhk/2bhk apartments around the office location",
    "june": "Move to your new apartment in the new city and start your new chapter in life",
    "july": "Buy your first Merc",
    "august": "Get your mum and dad to the US to live with you for however long they can",
    "september": "Start working on your podcast studio",
    "october": "Celebrate because your H1B got approved",
    "november": "Your loans are all cleared, so time to celebrate again",
    "december": "Run an ULTRA!"

}


def index(request):
    items = ""
    months = list(monthly_challenge.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("challenge-by-month", args=[month])
        items += f"<li><a href =\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")
    redirect_month = months[month-1]
    redirect_path = reverse("challenge-by-month", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge_by_name(request, month):
    try:
        capitalized_month = month.capitalize()
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, "month": capitalized_month
        })
    except:
        return HttpResponseNotFound("<h1>Resource not supported!</h1>")
