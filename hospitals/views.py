# hospitals/views.py
#from django.shortcuts import render
#from .models import Hospital
#from django.http import HttpResponse
#from pathlib import Path
#BASE_DIR = Path(__file__).resolve().parent.parent

#def map_view(request):
 #   hospitals = Hospital.objects.all()
  #  return render(request, 'map.html', {'hospitals': hospitals})
# hospitals/views.py
#from django.views import View
from django.shortcuts import render,redirect, get_object_or_404
from pathlib import Path
from .models import Hospital
from .forms import HospitalForm
BASE_DIR = Path(__file__).resolve().parent.parent
def hospital_map(request):
    hospitals = Hospital.objects.all()
    return render(request, 'index.html', {'hospitals': hospitals})
def hospital_detail(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    return render(request, 'hospital_detail.html', {'hospital': hospital})
def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})
def add_hospital(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital-map')  # Redirect to the map or another page upon successful form submission
    else:
        form = HospitalForm()

    return render(request, 'add_hospital.html', {'form': form})