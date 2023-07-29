from django.shortcuts import render

def index(request):
    from django.conf import settings
    return render(
        request,
        'home_index.html',
        {
            'Apps': sorted(
                [app for app in settings.INSTALLED_APPS if not "django" in app],
                key=str.lower,
            ),
        },
    )
