from django.shortcuts import render

# 메인페이지 보여주는 함수
def showmain(request):
    return render(request, 'main/mainpage.html')

# 
