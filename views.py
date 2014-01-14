from django.shortcuts import render_to_response

def index(request):
    from django.conf import settings
    return render_to_response('home_index.html', {
            'Apps': sorted(
                [app for app in settings.INSTALLED_APPS if not "django" in app],
                key=str.lower,
                )
            })
