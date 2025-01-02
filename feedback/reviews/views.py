from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View 
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


# Create your views here.

class ReviewView(CreateView):
    model = Review 
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    """def form_valid(self, form):
        form.save()
        return super().form_valid(form)"""
    

    """def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
        "form": form
    })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
        "form": form
    })"""

"""class ThankYouView(View):
    def get(self, request):
        return render(request, "reviews/thank_you.html")"""


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!!"
        return context


class ReviewListView(ListView):
    template_name ="reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=3)
        return data 


    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context """
    

class SingleReviewView(DetailView):
    template_name ="reviews/single_review.html"
    model = Review



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object 
        request = self.request
        favourite_id = request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context 
        
        
        """"review_id = kwargs["id"]
        selected_review = Review.objects.get(pk=review_id)
        context["reviews"] = selected_review
        return context """

class AddFavouriteView(View):
    def post(self, request):
        review_id  = request.POST["review_id"]
        #fav_review = Review.objects.get(pk=review_id)
        request.session["favourite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)


