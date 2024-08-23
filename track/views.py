from django.shortcuts import render,redirect
from .forms import PantryForm
# from .firebase import  get_all_items,add_item
# from .firebase import upload_image
# rom .firbase_orm import  FirebaseModel
from .models import Data
# from firebase_orm.models import FirebaseModel
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from django.shortcuts import get_object_or_404
# Use a service account.
cred = credentials.Certificate('firebase/firebase.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def add_item_to_firebase(items):
    doc_ref=db.collection('items').document(str(items.id))
    doc_ref.set({
        'Item Name':items.item_name,
        'Quantity':items.quantity,
        'Manufacturing Date':datetime.combine(items.Manufacturing_date, datetime.min.time()),  # Convert to datetime
        'Expiration Date':datetime.combine(items.Expiration_date, datetime.min.time()),  # Convert to datetime,
    })
# def add_item_to_firebase(items):
#     item = FirebaseModel(
#         Item_Name=items['Item_Name'],
#         Quantity=items['Quantity'],
#         Manufacturing_date=items['Manufacturing_date'],
#         Expiration_date=items['Expiration_date'],
#     )
#     item.save()
#
#
# # Create your views here.
# def sync_data_from_firebase(request):
#     firebase_data = FirebaseModel.objects.all()
#     for item in firebase_data:
#         Data.objects.update_or_create(
#             item_name=item.Item_Name,
#             defaults={
#                 'quantity': item.Quantity,
#                 'manufacturing_date': item.Manufacturing_date,
#                 'expiration_date': item.Expiration_date,
#             }
#         )
#     # Optionally redirect to another page
#     return redirect('item_list')
def item_list(request):
    items=Data.objects.all()
    return render(request,'index.html',{'items':items})


def add_item_view(request):
    if request.method=="POST":
        form=PantryForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.save()
            add_item_to_firebase(item)
            return redirect('item_list')
    else:
        form=PantryForm()
    return render(request,'add_item_view.html',{'form':form})

# def delete_item(request, item_id):
#
#     item = get_object_or_404(Data, pk=item_id)
#
#     if request.method=="POST":
#         db.collection('items').document(str(item.id)).delete()
#
#         # Delete the item from Django's database
#         item.delete()
#
#         return redirect('item_list')
#     return render(request,'delete_item.html',{'item':item})
#
# def reduce_quantity(request, item_id):
#     # Get the item from Django's database
#     item = get_object_or_404(Data, id=item_id)
#
#     # Reduce the quantity
#     if item.quantity > 0:
#         item.quantity -= 1
#         item.save()
#
#         # Update Firestore with the reduced quantity
#         doc_ref = db.collection('items').document(str(item.id))
#         doc_ref.update({'Quantity': item.quantity})
#
#     return redirect('item_list')
# pantry/views.py


def increase_quantity(request, item_id):
    item = get_object_or_404(Data, id=item_id)
    item.quantity += 1
    item.save()
    doc_ref = db.collection('items').document(str(item.id))
    doc_ref.update({'Quantity': item.quantity})
    return redirect('item_list')

def decrease_quantity(request, item_id):
    item = get_object_or_404(Data, id=item_id)
    if item.quantity > 0:
        item.quantity -= 1
        item.save()

        doc_ref = db.collection('items').document(str(item.id))
        doc_ref.update({'Quantity': item.quantity})
    return redirect('item_list')

def delete_item(request, item_id):
    item = get_object_or_404(Data, id=item_id)
    db.collection('items').document(str(item.id)).delete()
    item.delete()
    return redirect('item_list')
