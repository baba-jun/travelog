from django.core.exceptions import PermissionDenied

def root_user_required(view_func):
    """
    Decorator for views that checks if the user is a root user,
    raising a PermissionDenied exception if necessary.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view
