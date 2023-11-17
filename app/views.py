from django.shortcuts import render

# Create your views here.
def fun(request):
    return render(request,'cals.html')



def advcals(request):
    m=""
    try:
        if request.method=="POST":
            x1=int(request.POST.get("number1"))
            x2=int(request.POST.get("number2"))
            operation=request.POST.get("opr")

            if operation=="+":
                m=x1+x2
            elif operation=="-":
                m=x1-x2
            elif operation=="*":
                m=x1*x2
            elif operation=="/":
                m=x1/x2

    except:
        m="invalid Operation"
    print(m)
    return render(request,"cals.html",{"Result":m})
