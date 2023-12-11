from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render, redirect
from .models import FundraiseCause, Donation
from .forms import FundraiseCauseForm, DonationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'donations/about.html')

def causes_list(request):
    causes = FundraiseCause.objects.all()
    return render(request, 'donations/causes_list.html', {'causes': causes})

def cause_detail(request, pk):
    cause = FundraiseCause.objects.get(id=pk)
    return render(request, 'donations/cause_detail.html', {'cause': cause})

def cause_create(request):
    if request.method == 'POST':
        form = FundraiseCauseForm(request.POST, request.FILES)
        if form.is_valid():
            cause = form.save()
            return redirect('cause_detail', pk=cause.pk)
    else:
        form = FundraiseCauseForm()
    return render(request, 'donations/cause_form.html', {'form': form})

def cause_edit(request, pk):
    cause = get_object_or_404(FundraiseCause, pk=pk)
    
    if request.method == 'POST':
        form = FundraiseCauseForm(request.POST, request.FILES, instance=cause)
        if form.is_valid():
            cause = form.save()
            return redirect('cause_detail', pk=cause.pk)
    else:
        form = FundraiseCauseForm(instance=cause)

    return render(request, 'donations/cause_form.html', {'form': form})

def cause_delete(request, pk):
    FundraiseCause.objects.get(id=pk).delete()
    return redirect('causes_list')

def donation_create(request, pk):
    cause = FundraiseCause.objects.get(id=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.cause = cause
            donation.save()
            cause.current_amount += donation.amount
            cause.save()
            return redirect('cause_detail', pk=cause.pk)
    else:
        form = DonationForm()
    return render(request, 'donations/donation_form.html', {'form': form})
