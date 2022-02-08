from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request) :
    # Category 테이블에 있는 모든 데이터를 추출
    categories = Category.objects.all()
    # Restaurant 테이블에 있는 모든 데이터를 추출
    restaurants = Restaurant.objects.all()

    # html 파일에서 사용할 dic 구성
    content = {'categories' : categories, 'restaurants' : restaurants}

    # return HttpResponse("메인 페이지 입니다.")
    # 구성한 dict를 html 파일로 넘겨서 rendering 진행 - 카테고리 데이터, 레스토랑 데이터가 html 파일로 전달됨
    return render(request, 'shareRes/index.html', content) # html 파일을 찾을 때는 무조건 Templates 디렉터리 안에서 찾는

def restaurantDetail(request) :
    # return HttpResponse("음식점 세부 내용 페이지 입니다.")
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request) :
    # Category table의 Category명을 가져와서 화면에 출력
    # Category table의 Category명을 가져오기
    categories = Category.objects.all()
    # dict로 구성
    content = {'categories' : categories}
    # return HttpResponse("음식점 등록 페이지 입니다.")
    # 생성한 dict content를 html 파일로 전송해서 렌더링 진행
    return render(request, 'shareRes/restaurantCreate.html', content)
    # restaurantCreate.html 파일로 content가 전송되므로
    # restaurantCreate.html 파일에 장고 프론트코드를 추가해서 content 내용이 출력되게 해야 함


def Create_restaurant(request) :
    # 사용자가 입력한 카테고리, 맛집이름, 관련링크, 상세내용, 장소키워드를 얻어와서 변수에 저장한 다음
    # 카테고리
    cate_id = request.POST['resCategory']
    # ValueError: Cannot assign "'5'": "Restaurant.category" must be a "Category" instance.
    category = Category.objects.get(id=cate_id) # 해당 id 데이터가 Category 테이블에 없으면 Null 값이 반환
    # 만약 category 값이 Null이면 기본그룹이 저장됨

    # 맛집 이름
    name = request.POST['resTitle']
    # 관련 링크
    link = request.POST['resLink']
    # 상세 내용
    content = request.POST['resContent']
    # 장소키워드
    keyw = request.POST['resLoc']

    # DB 내의 테이블에 저장할 때는 models.py 파일 내의 class를 활용
    # 테이블객체변수 = 클래스명(필드명=값, 필드명=값, ....)
    new_rest = Restaurant(category=category,
                          restaurant_name=name,
                          restaurant_link=link,
                          restaurant_content=content,
                          restaurant_keyword=keyw)
    # 테이블객체변수.save()
    new_rest.save() # db 테이블에 저장

    # 아래 문장에 추가해서 강제응답하도록 코드를 수정하시오.
    # return HttpResponse("입력한 데이터를 DB에 저장했습니다." + " " + cate_id + " " + name + " " + " " + link + " "+ content + " "+ keyw) # 강제응답

    # db 저장이 완료된 후 저장된 내용을 표시하기 위해 페이지 이동 -> http://127.0.0.1:8000 url로 이동(index로 이름지어져 있음)
    return HttpResponseRedirect(reverse('index')) # index 함수 수정해서 db 반영되게 해야 함

def categoryCreate(request) :
    # Category 테이블에 저장되어 있는 모든 데이터를 db로부터 얻어오기(select)
    categories = Category.objects.all() # 해당 테이블의 모든 데이터 가져오기
    # html 파일에 rendering 하기 위해 dict 구성
    content = {'categories' : categories}
    # return  HttpResponse("분류 등록 페이지 입니다.")
    return render(request, 'shareRes/categoryCreate.html', content)
    # categoryCreate.html 파일로 content data가 같이 전송됨 -
    # html 파일을 장고 프론트코드를 추가해서 전달된된content가 반영되게 수정

def Create_category(request) : # 새로운 카테고리 생성 함수, http://127.0.0.1:8000/categoryCrate/create url 요청에 의해 응답하는 함수
    category_name = request.POST['categoryName'] # 사용자가 입력한 값 얻어오기(post 방식으로 전송되었으므로 .POST[] 사용)
    # DB에 저장
    new_category = Category(category_name=category_name) # Category = models.py에서 만든 테이블(클래스) 이름(맨위에 models.py import 필요) / 빨간 category_name : 필드명
    new_category.save() # db에 저장
    return HttpResponseRedirect(reverse('index')) # db 저장 후에 http://127.0.0.1:8000(기본화면에) 재 요청하는 코드
    # 재 요청된 후에는 새로 추가돈 카테고리가 화면에 출력되도록 index 함수를 수정
    # return HttpResponse(category_name + "값이 새 카테고리로 DB에 저장되었습니다.")

def Delete_category(request) :
    # 사용자가 특정 카테고리의 삭제버튼을 누르면 응답하는 함수
    # categoryId 이름의 변수에 삭제하고자 하는 category id 값을 전달해 준다.
    cate_id = request.POST['categoryId'] # hidden 태그에 의해 전달된 id 값 얻어오기
    # db에서 삭제하기 위해 get 함수를 이용 행당 id의 객체를 얻는다.
    del_cate = Category.objects.get(id=cate_id) # 클라이언트에서 전달된 category id 값과 일치한 레코드(행)를 추출(접근) # 모두 가져올 땐 all, 하나만 가져올 땐 get
    del_cate.delete() # 추출된 레코드를 최종 삭제
    # 카테고리 삭제 후 카테고리 추가하는 페이지를 재요청
    return HttpResponseRedirect(reverse('cateCreatePage'))


