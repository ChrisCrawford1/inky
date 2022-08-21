from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pens.models import Pen


@login_required(login_url="/login")
def home(request):
    pens = Pen.objects.all()
    total_value = 0
    average_price = 0
    last_five_purchased = pens.order_by("-purchased_date")[0:5]
    highest_prices = pens.order_by("-purchase_price")[0:5]

    for pen in pens:
        total_value += pen.purchase_price

    if pens.count() != 0:
        average_price = round(total_value / pens.count())

    return render(
        request,
        "homepage.html",
        {
            "pen_count": pens.count(),
            "ink_count": 10,
            "total_value": "{:,}".format(round(total_value)),
            "average": "{:,}".format(average_price),
            "last_five_purchased": last_five_purchased,
            "highest_prices": highest_prices,
        },
    )
