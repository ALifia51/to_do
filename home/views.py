from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    # dict ={
    
    #     "name" : "Alifia ",
    #     "ID" : 20201051 ,
    #     "Courses" : ["cse 310","cse 309","cse 311"],
    #     "mark" :  mk
    # }
    return render(request, "home.html")
def about_view(request): 
    return render(request, "about.html")
# def home_view(request ): 
#     return render(request,"about.html" )