from django.db import models
from django.shortcuts import resolve_url

class Board(models.Model):
    title = models.CharField(max_length=100)  # 게시글의 제목
    content = models.TextField()  # 게시글의 내용
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', null=True, blank=True)  # 게시글의 이미지
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간
    updated_at = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):  # 객체를 문자열로 표현할 때 사용
        return f'제목: {self.title}, 작성날짜: {self.created_at}, 수정날짜: {self.updated_at}'
    def get_absolute_url(self):  # 이 객체의 상세 페이지 URL을 반환
        return resolve_url('post:detail', pk=self.id)