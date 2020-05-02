import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from DynamicTable.models import  Details
# Create your views here.

def HomePage(request):
    data=Details.objects.all()
    return render(request,"homepage.html",{"data":data})


@csrf_exempt
def insert(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            details=Details()
            details.First_Name=dic_single['First_Name']
            details.Last_Name=dic_single['Last_Name']
            details.City=dic_single['City']
            details.save()
        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(response_data,safe=False)
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
        return JsonResponse(response_data,safe=False)
@csrf_exempt
def update_details(request):
    data=request.POST.get("data")
    dict_data=json.loads(data)
    try:
        for dic_single in dict_data:
            details=Details.objects.get(id=dic_single['id'])
            details.First_Name=dic_single['First_Name']
            details.Last_name=dic_single['Last_Name']
            details.City=dic_single['City']
            details.save()
        response_data={"error":False,"errorMessage":"Updated Successfully"}
        return JsonResponse(response_data,safe=False)
    except:
        response_data={"error":True,"errorMessage":"Failed to Update Data"}
        return JsonResponse(response_data,safe=False)



@csrf_exempt
def delete_details(request):
    id=request.POST.get("id")
    try:
        details=Details.objects.get(id=id)
        details.delete()
        response_data={"error":False,"errorMessage":"Deleted Successfully"}
        return JsonResponse(response_data,safe=False)
    except:
        stuent_data={"error":True,"errorMessage":"Failed to Delete Data"}
        return JsonResponse(response_data,safe=False)

        
def insert_table(request):
    return render(request,"table.html")
