import urllib.request
import urllib.parse
import json
from django.http import JsonResponse, HttpResponse
from kafka import SimpleProducer, KafkaClient

def homepage(request):

	req = urllib.request.Request('http://models-api:8000/api/v1/listing/recent')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)

def listing_det(request, listing_id):
	req = urllib.request.Request('http://models-api:8000/api/v1/listing/' + listing_id)
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)

def login(request):
	post_data = {'username': request.POST['username'], 'password': request.POST['password']}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://models-api:8000/api/v1/users/auth', data=post_encoded, method='POST')	
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)

def logout(request):
	post_data = {'u_id': request.POST['u_id']}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://models-api:8000/api/v1/users/logout', data=post_encoded, method='POST')	
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)



def create_usr(request):
	post_data = {'username': request.POST['username'], 'password': request.POST['password'], 'first_name': request.POST['first_name'], 'last_name': request.POST['last_name'], 'type_of_user': 'general'}
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://models-api:8000/api/v1/users/create', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)


def create_lst(request):
	post_data = {'title': request.POST['title'], 'description': request.POST['description'], 'creator': request.POST['creator'], 'available': request.POST['available'], 'u_id': request.POST['u_id']}
	kafka = KafkaClient('kafka:9092')
	producer = SimpleProducer(kafka)
	some_new_listing = {'title': request.POST['title'], 'description': request.POST['description'], 'creator': request.POST['creator']}
	producer.send_messages(b'new-listings-topic', json.dumps(some_new_listing).encode('utf-8'))
	post_encoded = urllib.parse.urlencode(post_data).encode('utf-8')
	req = urllib.request.Request('http://models-api:8000/api/v1/listing/create', data=post_encoded, method='POST')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	resp = json.loads(resp_json)
	return JsonResponse(resp)
