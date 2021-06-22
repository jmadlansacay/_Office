import re

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import is_safe_url
from ims_main.models import user_detail
from ims.Utils import getuname


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
   

class GetLoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        USER_NAME = getuname(request)
        redirect_to = settings.ERROR_URL
     
        if len(user_detail.objects.filter(username=USER_NAME)) == 0:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(redirect_to)

        