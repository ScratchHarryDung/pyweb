from django.shortcuts import render

# hàm def này mục đích cụ thể là đẻ làm j ạ?
def get_homepage(request):
    return render(request,'index.html')