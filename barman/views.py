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


def pg_register(request):
    """PG_register.
    """
    return render(
        request,
        "pg_register.html",
        {
            "nav_active": "pg_register"
        }
    )
