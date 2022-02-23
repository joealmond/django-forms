from multiprocessing import context
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView


from .forms import ReviewsForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    # fields = "__all__"
    form_class = ReviewsForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"  # note the url

# class ReviewView(FormView):
#     form_class = ReviewsForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"  # note the url

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

    # def post(self, request):
    #     form = ReviewsForm(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })


# class ReviewView(View):
#     def get(self, request):
#         form = ReviewsForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewsForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })


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

# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "reviews/thank_you.html", {"has_error": False})


# def thank_you(request):
#     return render(request, "reviews/thank_you.html", {"has_error": False})


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4) # whay 4?
    #     return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         slected_review = Review.objects.get(pk=review_id)
#         # reviews = Review.objects.all()
#         context["review"] = slected_review
#         return context


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review  # "Review" is reference al lower case in the template
