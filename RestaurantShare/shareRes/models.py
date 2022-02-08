from django.db import models

# Create your models here.

# 카테고리를 저장할 테이블이기 때문에 카테고리명이 저장될 필드만 필요
# 카테고리명은 문자열임(최대 길이는 100글자로 한정)
class Category(models.Model) :
    category_name = models.CharField(max_length=100) # 필드명(열이름) : category_name (shareRes\views.py 에서도 쓸 필드이름임)

# 맛집(Restaurant)을 추가할 테이블 생성
# 추가 내용(5개의 필드(열)를 생성)
# 카테고리(카테고리테이블의 id가 저장), 이름, 링크, 설명(장문 저장 가능하게), 키워드 : 카테고리 제외 나머지는 문자열
class Restaurant(models.Model) :
    category = models.ForeignKey(Category,on_delete=models.SET_DEFAULT,default=5)
    # category에 입력되는 값은 Category 테이블에 있는 id 값이어야 함. 혹시 입력된 id값의 카테고리가 삭제되면 기본 카테고리로 설정 : default=5
    restaurant_name = models.CharField(max_length=100) #맛집 이름
    restaurant_link = models.CharField(max_length=500) #맛집 URL
    restaurant_content = models.TextField() #맛집 설명
    restaurant_keyword = models.CharField(max_length=50) # 키워드

