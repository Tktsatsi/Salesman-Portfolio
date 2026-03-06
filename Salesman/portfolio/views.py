from django.shortcuts import render,redirect
from .models import Career,SoldCar,Review
from .forms import ReviewForm
from datetime import date

def home(request):

    careers = Career.objects.all()
    cars = SoldCar.objects.all().order_by("-year_sold")
    reviews = Review.objects.all().order_by("-created_at")

    total_cars = SoldCar.objects.count()
    total_reviews = Review.objects.count()
    dealerships = Career.objects.values('dealership').distinct().count()

    start = Career.objects.order_by("start_year").first()
    years_experience = date.today().year - start.start_year if start else 0

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "careers":careers,
        "cars":cars,
        "reviews":reviews,
        "form":form,
        "total_cars":total_cars,
        "total_reviews":total_reviews,
        "dealerships":dealerships,
        "years_experience":years_experience
    }

    return render(request,"index.html",context)
