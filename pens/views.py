from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.views.defaults import page_not_found

from brands.models import Brand
from pens.forms import PenForm
from pens.models import Pen


@login_required(login_url="/login")
@require_http_methods(["GET", "POST"])
def create_pen(request):
    if request.method == "GET":
        form = PenForm()
        return render(request, "create_pen.html", {"form": form})
    elif request.method == "POST":
        submitted_form = PenForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            #  validate the form, fetch the model instance and overwrite the
            #  initial id in the cleaned data to insert into the new model db instance.
            cleaned_data = submitted_form.cleaned_data
            fetched_brand = Brand.objects.get(id=cleaned_data.get("brand"))
            cleaned_data["brand"] = fetched_brand
            Pen.objects.create(**submitted_form.cleaned_data)

            return redirect("view_pens")
        else:
            return render(request, "create_pen.html", {"form": submitted_form})


@login_required(login_url="/login")
@require_http_methods(["GET"])
def show_pen(request, id):
    try:
        pen = Pen.objects.get(id=id)
        pen_as_dict = pen.__dict__
        pen_as_dict["brand"] = pen.brand_id
        form = PenForm(initial=pen.__dict__)

        return render(request, "show_pen.html", {"pen": pen, "form": form})
    except ObjectDoesNotExist as e:
        return page_not_found(request, e)


@login_required(login_url="/login")
@require_http_methods(["POST"])
def update_pen(request, id):
    try:
        update_data = PenForm(request.POST, request.FILES)

        if update_data.is_valid():
            cleaned_data = update_data.cleaned_data

            stored_pen = Pen.objects.get(id=id)
            stored_pen.name = cleaned_data.get("name")
            stored_pen.nib_size = cleaned_data.get("nib_size")
            stored_pen.nib_material = cleaned_data.get("nib_material")
            stored_pen.description = cleaned_data.get("description")
            stored_pen.colour = cleaned_data.get("colour")
            stored_pen.purchase_price = cleaned_data.get("purchase_price")
            stored_pen.purchased_date = cleaned_data.get("purchased_date")
            stored_pen.purchase_currency = cleaned_data.get("purchase_currency")

            # Not sure how else to do this with Django forms
            # TODO: Refactor forms away from Django forms to traditional html and validator methods
            if cleaned_data.get("image") is None:
                cleaned_data.pop("image")
            else:
                stored_pen.image = cleaned_data.get("image")

            stored_pen.save(update_fields=cleaned_data.keys())

        return redirect("view_pens")

    except ObjectDoesNotExist as e:
        return page_not_found(request, e)


@login_required(login_url="/login")
@require_http_methods(["GET"])
def view_pens(request):
    pens = Pen.objects.order_by("brand__name")
    return render(request, "view_pens.html", {"pens": pens})
