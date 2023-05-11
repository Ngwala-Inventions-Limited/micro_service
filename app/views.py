import uuid
from .models import Transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


def code(seed = None):
    if (not seed) or (type(seed) != str) or (len(seed) < 10):
        seed = str(uuid.uuid4())[:10]

    code = ""
    for character in seed:
        value = str(ord(character))
        code += value

    return code[:20]
    
@api_view(['GET'])
def index(request, format=None):
    return Response(("Access control is Online"))
    

@api_view(['GET'])
def get_trans(request, format=None):
    response = []
    for set in Transaction.objects.all():
        stored_uid = set.uid
        stored_amount = int(set.amount)
        stored_version = set.version
        
        transaction = {
            stored_uid : stored_amount,
            "vers": stored_version
            }
        
        response.append(transaction)
        
    return Response(response)
    
    
@api_view(['GET'])
def get_user(request, format=None):
    # data = json.loads(request.body)
    request_uid = request.GET.get('uid')
    json_response = {}
    
    try:
        stored = Transaction.objects.get(uid = request_uid)
            
        json_response = {request_uid : int(stored.amount), "vers": stored.version}
    except Transaction.DoesNotExist:
           new_user = Transaction(uid = request_uid)
           new_user.save()
           return Response({"message": "saved!"}, status=status.HTTP_200_OK)    
              
    return Response(json_response)

