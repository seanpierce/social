import json
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator\

@method_decorator(csrf_exempt, name='dispatch')
class CSRFExemptView(View):
    
    def Response(self, data, status):
        try:
            return HttpResponse(json.dumps(data), status=status, content_type='application/json')
        except Exception as e:
            return HttpResponse('Unable to create API response', status=500, content_type='application/json')