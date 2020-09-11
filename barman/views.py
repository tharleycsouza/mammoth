from django.shortcuts import render

# Create your views here.


def dashboard(request):
    """Dashboard.
    """
    return render(
        request,
        "dashboard.html",
        {
            "nav_active": "dashboard"
        }
    )
