from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ReviewsForm
from .models import Review

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewsForm()
        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewsForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form": form
        })


# def review(request):
#     # if request.method == "POST":
#     #     entered_username = request.POST["username"]

#     #     # if entered_username == "" and len(entered_username) <= 100:
#     #     #     return render(request, "reviews/review.html", {"has_error": True})
#     #     print(entered_username)
#     #     return HttpResponseRedirect("/thank-you")
#     # return render(request, "reviews/review.html")

#     if request.method == "POST":
#         form = ReviewsForm(request.POST)
#         # existing_data = Review.objects.get(pk=1) # for updating data
#         # form = ReviewsForm(request.POST, intance=existing_data) # for updating data

#         if form.is_valid():
#             form.save()  # you can cause of modelform
#             # # print(form.cleaned_data)
#             # review = Review(
#             #     user_name=form.cleaned_data["user_name"],
#             #     review_text=form.cleaned_data["review_text"],
#             #     rating=form.cleaned_data["rating"])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewsForm()

#     return render(request, "reviews/review.html", {
#         "form": form
#     })


def thank_you(request):
    return render(request, "reviews/thank_you.html", {"has_error": False})
