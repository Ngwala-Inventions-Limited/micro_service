from django.shortcuts import render
import uuid
import json
from .models import Transaction
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def code(seed = None):
    if (not seed) or (type(seed) != str) or (len(seed) < 10):
        seed = str(uuid.uuid4())[:10]

    code = ""
    for character in seed:
        value = str(ord(character))
        code += value

    return code[:20]
    
    
    
@api_view(['POST'])
def Transactionlist(request):
    data = json.loads(request.body) 
    response = []
    
    for set in data:
        requested_uid = set['uid']
        requested_amount = set['amount']
        requested_version = set['version'] 
        
        try:
            # grap stored uid from the database 
            stored_uid = Transaction.objects.get(uid = requested_uid)
            #   check if the transaction is valid
            if requested_version != str(stored_uid.version):
                requested_amount = str(int(requested_amount) + int(stored_uid.amount))
                requested_version = str(stored_uid.version)         
            else: # check for incoming uid that is not on the database and add them
                requested_amount = str(stored_uid.amount)
                    
        except Transaction.DoesNotExist:
            # if uid does not exist add it in the database
            new_transaction = Transaction(uid = requested_uid)
            new_transaction.save()
        
        # compared amount of requested_uid is the same as amount of the stored_uid
        # and change the requested_uid amount
        finally:
            transaction = {"uid": requested_uid, "amount": requested_amount, "version": requested_version}
            
        response.append(transaction)
    return Response(response)