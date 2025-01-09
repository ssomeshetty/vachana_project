from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# vachanas/views.py
from django.http import HttpResponse

def some_view(request):
    return HttpResponse("Hello, this is some view!")

from django.db.models import Q
from .models import Vachana


@login_required
def vachana_list(request):
    # Get the search query from the GET request
    search_query = request.GET.get('search', '')

    # Filter the Vachanas based on the search query, if any
    vachanas = Vachana.objects.all()

    if search_query:
        vachanas = vachanas.filter(
            Q(author__name__icontains=search_query) |  # Filter by author name (case-insensitive)
            Q(category__icontains=search_query) |  # Filter by category (case-insensitive)
            Q(content__icontains=search_query)  # Filter by content (case-insensitive)
        )
        

    return render(request, 'vachanas/vachana_list.html', {'vachanas': vachanas, 'search_query': search_query})


from django.shortcuts import redirect, get_object_or_404

@login_required
def like_vachana(request, vachana_id):
    vachana = get_object_or_404(Vachana, id=vachana_id)
    # Add the logged-in user to the list of users who liked this Vachana
    vachana.likes.add(request.user)

    # Track the 'liked' activity
    Activity.objects.create(user=request.user, activity_type='liked')

    return redirect('vachanas:vachana_list')



from .forms import VachanaForm
from users.models import Activity
@login_required
def create_vachana(request):
    if request.method == 'POST':
        form = VachanaForm(request.POST)
        if form.is_valid():
            # Save the Vachana with the current user as the sender
            vachana = form.save(commit=False)
            vachana.sender = request.user  # Set the user who created the Vachana
            vachana.save()
            # Track the 'created' activity
            Activity.objects.create(user=request.user, activity_type='created')
        
            return redirect('vachanas:vachana_list')  # Redirect to Vachana list page
    else:
        form = VachanaForm()

    return render(request, 'vachanas/create_vachana.html', {'form': form})