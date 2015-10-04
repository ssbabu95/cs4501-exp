import urllib.request
import urllib.parse
import json
from django.http import JsonResponse

def homepage(request):

	req = urllib.request.Request('http://10.0.2.2:8001/api/v1/listing/recent')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)

def listing_det(request, listing_id):
	req = urllib.request.Request('http://10.0.2.2:8001/api/v1/listing/' + listing_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)

