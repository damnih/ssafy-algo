from django.shortcuts import render

def index(request):
   # url로부터 호출받는 view 함수
   # index view 함수의 목적 - 메인 페이지 1개를 응답하는 것
   # 응답 덩어리(객체)는 반드시 함수의 반환 값으로 클라이언트에게 전달됨
   # 내가 지정해주는 거 ㅇㅇ
   # return render(request, 템플릿 경로(문자열)) 
   return render(request, 'articles/index.html')
# 만약 템플릿 폴더 안에 다른 경로 없이 바로 index.html파일이 있다면
# return render(request, 'index.html') 로 쓰면 됨 
# 3줄의 index와 9줄의 index파일은 꼭 이름이 같아야할까? 
# 문법상으로는 달라도 ㄱㅊ함 근데 그냥 헷갈리니깐 맞춰주는 편 
# 
# 