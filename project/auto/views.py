from django.shortcuts import redirect, render, get_object_or_404

from .models import Auto


def auto_list(request):
    autos = Auto.objects.all()
    return render(request,
    'auto_list.html',
    {'autos': autos})

def auto_detail(request, id):
	auto = get_object_or_404(Auto,
	id=id)
	return render(request,
	'auto_detail.html',
	{'auto': auto})
	

def create_auto(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        model = request.POST['model']
        year = request.POST['year']
        color = request.POST['color']
        new_auto = Auto(brand=f"{brand}", model=f"{model}", year=year, color=f"{color}")
        new_auto.save()
        return redirect('/')

    return render(request, 'create_auto.html')


# 