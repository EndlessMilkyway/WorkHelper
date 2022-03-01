"""
    GNU Newsletter Work Helper
    
    Use Modules: tkinter, datetime, os
    Version: 0.1
    Email: freekyr7529@gmail.com
    
    Copyright (C) 2022, Yeong Ryeol Kim from Gyeongsang National University
    MIT License
"""

# 필요 모듈 import
import tkinter as tk
from datetime import datetime

# GUI 프로그램 뼈대 및 파일 생성 함수
class WorkHelper(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        
        self.parent = parent
        self.section1()
        self.section2()
        self.section3()
        
        genandsaveButton = tk.Button(self.frame3, text="파일 생성 및 저장", font=("나눔바른고딕", 15), overrelief="groove", command=self.GenerateFile)
        genandsaveButton.place(x=90, y=530, width=200)
        
        img = tk.PhotoImage(file='example.png')
        examplePhoto = tk.Label(self, image=img)
        examplePhoto.place(x=1280, y=20)
        examplePhoto.image = img
        
        copylightLabel = tk.Label(self, text="Copyright (C) 2022, Yeong Ryeol Kim from Gyeongsang National University", font=("나눔바른고딕", 12) ,fg="black")
        copylightLabel.place(x=480, y=630)
    
    def section1(self):
        self.frame1 = tk.Frame(self, width=400, height=600, relief="ridge", bd=2)
        self.frame1.place(x=20, y=20)
        
        menuLabel = tk.Label(self.frame1, text="1. 상단메뉴", font=("나눔바른고딕", 18) ,fg="black")
        menuLabel.place(x=15, y=15)
        
        menuEntry1 = tk.Entry(self.frame1)
        menuEntry1.insert(0, "https://newgh.gnu.ac.kr/main/main.do")
        menuEntry1.place(x=20, y=50, width=360, height=25)
        
        menuEntry2 = tk.Entry(self.frame1)
        menuEntry2.insert(0, "https://newgh.gnu.ac.kr/new/main.do?mi=5419")
        menuEntry2.place(x=20, y=80, width=360, height=25)
        
        menuEntry3 = tk.Entry(self.frame1)
        menuEntry3.insert(0, "https://newgh.gnu.ac.kr/fund/main.do")
        menuEntry3.place(x=20, y=110, width=360, height=25)
        
        menuEntry4 = tk.Entry(self.frame1)
        menuEntry4.insert(0, "https://newgh.gnu.ac.kr/main/cm/cntnts/cntntsView.do?mi=1065&cntntsId=1185")
        menuEntry4.place(x=20, y=140, width=360, height=25)
        
        menuEntry5 = tk.Entry(self.frame1)
        menuEntry5.insert(0, "https://newgh.gnu.ac.kr/research/main.do")
        menuEntry5.place(x=20, y=170, width=360, height=25)
        
        noticeLabel = tk.Label(self.frame1, text="2. 공지사항", font=("나눔바른고딕", 18) ,fg="black")
        noticeLabel.place(x=15, y=205)
        
        noticeEntry1 = tk.Entry(self.frame1)
        noticeEntry1.place(x=20, y=240, width=360, height=25)
        
        noticeEntry2 = tk.Entry(self.frame1)
        noticeEntry2.place(x=20, y=270, width=360, height=25)
        
        noticeEntry3 = tk.Entry(self.frame1)
        noticeEntry3.place(x=20, y=300, width=360, height=25)
        
        noticeEntry4 = tk.Entry(self.frame1)
        noticeEntry4.place(x=20, y=330, width=360, height=25)
        
        noticeEntry5 = tk.Entry(self.frame1)
        noticeEntry5.place(x=20, y=360, width=360, height=25)
        
        edupolicyLabel = tk.Label(self.frame1, text="3. 교육정책", font=("나눔바른고딕", 18) ,fg="black")
        edupolicyLabel.place(x=15, y=395)
        
        edupolicyEntry1 = tk.Entry(self.frame1)
        edupolicyEntry1.place(x=20, y=430, width=360, height=25)
        
        edupolicyEntry2 = tk.Entry(self.frame1)
        edupolicyEntry2.place(x=20, y=460, width=360, height=25)
        
        edupolicyEntry3 = tk.Entry(self.frame1)
        edupolicyEntry3.place(x=20, y=490, width=360, height=25)
        
        edupolicyEntry4 = tk.Entry(self.frame1)
        edupolicyEntry4.place(x=20, y=520, width=360, height=25)
        
        edupolicyEntry5 = tk.Entry(self.frame1)
        edupolicyEntry5.place(x=20, y=550, width=360, height=25)

    def section2(self):
        self.frame2 = tk.Frame(self, width=400, height=600, relief="ridge", bd=2)
        self.frame2.place(x=440,y=20)
        
        parkLabel = tk.Label(self.frame2, text="4. 개척광장", font=("나눔바른고딕", 18) ,fg="black")
        parkLabel.place(x=15, y=15)
        
        parkEntry1 = tk.Entry(self.frame2)
        parkEntry1.place(x=20, y=50, width=360, height=25)
        
        parkEntry2 = tk.Entry(self.frame2)
        parkEntry2.place(x=20, y=80, width=360, height=25)
        
        parkEntry3 = tk.Entry(self.frame2)
        parkEntry3.place(x=20, y=110, width=360, height=25)
        
        parkEntry4 = tk.Entry(self.frame2)
        parkEntry4.place(x=20, y=140, width=360, height=25)
        
        parkEntry5 = tk.Entry(self.frame2)
        parkEntry5.place(x=20, y=170, width=360, height=25)
        
        alumniLabel = tk.Label(self.frame2, text="5. 교직원 동문 소식", font=("나눔바른고딕", 18) ,fg="black")
        alumniLabel.place(x=15, y=205)
        
        alumniEntry1 = tk.Entry(self.frame2)
        alumniEntry1.place(x=20, y=240, width=360, height=25)
        
        alumniEntry2 = tk.Entry(self.frame2)
        alumniEntry2.place(x=20, y=270, width=360, height=25)
        
        alumniEntry3 = tk.Entry(self.frame2)
        alumniEntry3.place(x=20, y=300, width=360, height=25)
        
        alumniEntry4 = tk.Entry(self.frame2)
        alumniEntry4.place(x=20, y=330, width=360, height=25)
        
        alumniEntry5 = tk.Entry(self.frame2)
        alumniEntry5.place(x=20, y=360, width=360, height=25)
        
        academiaLabel = tk.Label(self.frame2, text="6. 학술행사", font=("나눔바른고딕", 18) ,fg="black")
        academiaLabel.place(x=15, y=395)
        
        academiaEntry1 = tk.Entry(self.frame2)
        academiaEntry1.place(x=20, y=430, width=360, height=25)
        
        academiaEntry2 = tk.Entry(self.frame2)
        academiaEntry2.place(x=20, y=460, width=360, height=25)
        
        academiaEntry3 = tk.Entry(self.frame2)
        academiaEntry3.place(x=20, y=490, width=360, height=25)
        
        academiaEntry4 = tk.Entry(self.frame2)
        academiaEntry4.place(x=20, y=520, width=360, height=25)
        
        academiaEntry5 = tk.Entry(self.frame2)
        academiaEntry5.place(x=20, y=550, width=360, height=25)        

    def section3(self):
        self.frame3 = tk.Frame(self, width=400, height=600, relief="ridge", bd=2)
        self.frame3.place(x=860,y=20)
        
        bottomMenuLabel = tk.Label(self.frame3, text="7. 하단메뉴", font=("나눔바른고딕", 18) ,fg="black")
        bottomMenuLabel.place(x=15, y=15)
        
        bottomMenuEntry1 = tk.Entry(self.frame3)
        bottomMenuEntry1.insert(0, "https://web.facebook.com/pioneeringGNU/")
        bottomMenuEntry1.place(x=20, y=50, width=360, height=25)
        
        bottomMenuEntry2 = tk.Entry(self.frame3)
        bottomMenuEntry2.insert(0, "https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?mi=1121&bbsId=1204")
        bottomMenuEntry2.place(x=20, y=80, width=360, height=25)
        
        bottomMenuEntry3 = tk.Entry(self.frame3)
        bottomMenuEntry3.insert(0, "https://www.youtube.com/channel/UCruDceKvt2W6iZcP04JIZJw")
        bottomMenuEntry3.place(x=20, y=110, width=360, height=25)
        
        bottomMenuEntry4 = tk.Entry(self.frame3)
        bottomMenuEntry4.insert(0, "https://blog.naver.com/gnujinju")
        bottomMenuEntry4.place(x=20, y=140, width=360, height=25)
        
        bottomMenuEntry5 = tk.Entry(self.frame3)
        bottomMenuEntry5.insert(0, "https://www.youtube.com/watch?v=1sjGCQ88LoI")
        bottomMenuEntry5.place(x=20, y=170, width=360, height=25)
        
        hotnewsLabel = tk.Label(self.frame3, text="8. 핫뉴스", font=("나눔바른고딕", 18) ,fg="black")
        hotnewsLabel.place(x=15, y=205)
        
        hotnewsEntry1 = tk.Entry(self.frame3)
        hotnewsEntry1.place(x=20, y=240, width=360, height=25)
        
        hotnewsEntry2 = tk.Entry(self.frame3)
        hotnewsEntry2.place(x=20, y=270, width=360, height=25)
        
        hotnewsEntry3 = tk.Entry(self.frame3)
        hotnewsEntry3.place(x=20, y=300, width=360, height=25)
        
        numLabel = tk.Label(self.frame3, text="이번 호수", font=("나눔바른고딕", 18) ,fg="black")
        numLabel.place(x=15, y=335)
        
        numEntry = tk.Entry(self.frame3)
        numEntry.place(x=20, y=370, width=360, height=25)

    def GenerateFile(self):
        file1 = open(file='newsletter_'+ today_process +'_1.html', mode='w', encoding='UTF-8')
        file1.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ko">
  <head>
    <title>경상국립대학교 뉴스레터 제280호</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  </head>

  <body>
    <table cellpadding="0" cellspacing="0" width="100%">
      <tr>
        <td align="center">
          <table cellpadding="0" cellspacing="0" border="0" width="770px">
            <tr>
              <td width="770" height="555" style="font-size: 0">
                <img
                  src="main_280_1_01.jpg"
                  alt=""
                  width="770"
                  height="555"
                  usemap="#Map1"
                  border="0"
                />
                <map name="Map1">
                  <area
                    shape="rect"
                    coords="40, 430, 170, 555"
                    href="https://newgh.gnu.ac.kr/main/main.do"
                    target="_blank"
                    alt="경상대학교"
                  />
                  <area
                    shape="rect"
                    coords="187, 430, 310, 555"
                    href="https://newgh.gnu.ac.kr/new/main.do?mi=5419"
                    target="_blank"
                    alt="입학안내"
                  />
                  <area
                    shape="rect"
                    coords="327, 430, 450, 555"
                    href="https://newgh.gnu.ac.kr/fund/main.do"
                    target="_blank"
                    alt="발전기금"
                  />
                  <area
                    shape="rect"
                    coords="467, 430, 592, 555"
                    href="https://newgh.gnu.ac.kr/main/cm/cntnts/cntntsView.do?mi=1065&cntntsId=1185"
                    target="_blank"
                    alt="취업뉴스"
                  />
                  <area
                    shape="rect"
                    coords="607,430,730,555"
                    href="https://newgh.gnu.ac.kr/research/main.do"
                    target="_blank"
                    alt="산학협력바로가기"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="987" style="font-size: 0">
                <img
                  src="main_280_1_02.jpg"
                  alt=""
                  width="770"
                  height="987"
                  usemap="#Map2"
                  border="0"
                  href="http://www.gnu.ac.kr/"
                />
                <map name="Map2">
                  <!--개척광장 1~8번-->
                  <area
                    shape="rect"
                    coords="36,672,255,815"
                    href="https://newsis.com/view/?id=NISX20220207_0001749258&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,825,255,845"
                    href="https://newsis.com/view/?id=NISX20220215_0001760022&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,845,255,865"
                    href="https://newsis.com/view/?id=NISX20220213_0001757009&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,865,255,885"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494124"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,890,255,910"
                    href="http://www.gndomin.com/news/articleView.html?idxno=305626#0BNb"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,910,255,930"
                    href="https://www.nocutnews.co.kr/news/5705382"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,932,255,953"
                    href="https://www.cnbnews.com/news/article.html?no=531971"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,953,255,975"
                    href="https://www.youtube.com/watch?v=1sjGCQ88LoI"
                    target="_blank"
                  />


                  <!--교직원,동문 소식 1~8번-->
                  <area
                    shape="rect"
                    coords="276,672,495,815"
                    href="http://www.idomin.com/news/articleView.html?idxno=786003"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,825,495,845"
                    href="https://www.mk.co.kr/opinion/contributors/view/2022/02/135144/"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,845,495,865"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494049"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,865,495,885"
                    href="https://www.hani.co.kr/arti/opinion/column/1030910.html"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,890,495,910"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493844"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,910,495,930"
                    href="http://www.idomin.com/news/articleView.html?idxno=785232"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,932,495,953"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494011"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,953,495,975"
                    href="https://newsis.com/view/?id=NISX20220217_0001762491&cID=10812&pID=10800"
                    target="_blank"
                  />

                  <!--학술행사 1~8번-->
                  <area
                    shape="rect"
                    coords="516,672,735,815"
                    href="http://www.gndomin.com/news/articleView.html?idxno=306362"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,825,735,845"
                    href="http://www.lecturernews.com/news/articleView.html?idxno=89825"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,845,735,865"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494086"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,865,735,885"
                    href="http://www.kyosu.net/news/articleView.html?idxno=84913"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,890,735,910"
                    href="http://www.lecturernews.com/news/articleView.html?idxno=89772"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,910,735,930"
                    href="http://www.gndomin.com/news/articleView.html?idxno=305697#0BNb"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,932,735,953"
                    href="http://www.veritas-a.com/news/articleView.html?idxno=406152"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,953,735,975"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493945"
                    target="_blank"
                  />

                  <!--핫뉴스 1~3번-->
                  <area
                    shape="rect"
                    coords="35,55,365,300"
                    href="https://newsis.com/view/?id=NISX20220214_0001757319&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,55,740,167"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493500"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,188,740,301"
                    href="https://www.mk.co.kr/news/it/view/2022/02/114449/"
                    target="_blank"
                  />

                  <!--공지사항 +아이콘-->
                  <area
                    shape="rect"
                    coords="334,357,364,387"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?bbsId=1028&mi=1126"
                    target="_blank"
                  />
                  <!--공지사항 1~5번-->
                  <area
                    shape="rect"
                    coords="25,405,362,440"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2119794"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,440,362,480"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2119384"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,480,362,520"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2122972"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,520,362,560"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?nttSn=2122543&mi=1127"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,560,362,600"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2122345"
                    target="_blank"
                  />

                  <!--교육정책 +아이콘-->
                  <area
                    shape="rect"
                    coords="720,357,750,387"
                    href="https://newgh.ac.kr/"
                    target="_blank"
                  />
                  <!--교육정책 1~5번-->
                  <area
                    shape="rect"
                    coords="410,405,750,440"
                    href="https://www.donga.com/news/article/all/20220208/111659725/1"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,440,750,480"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494218"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,480,750,520"
                    href="http://www.newsgn.com/321888"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,520,750,560"
                    href="http://www.gndomin.com/news/articleView.html?idxno=306363"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,560,750,600"
                    href="http://www.idomin.com/news/articleView.html?idxno=785086"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="423" style="font-size: 0">
                <img
                  src="main_280_1_03.jpg"
                  alt=""
                  width="770"
                  height="423"
                  usemap="#Map3"
                  border="0"
                />
                <map name="Map3">
                  <area
                    coords="427,320,560,345"
                    href="newsletter@gnu.ac.kr"
                    shape="rect"
                    target="_blank"
                  />
                  <area
                    coords="562,390,621,408"
                    href="newsletter@gnu.ac.kr"
                    shape="rect"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="35,26,164,76"
                    href="https://web.facebook.com/pioneeringGNU/"
                    target="_blank"
                    alt="페이스북"
                  />
                  <area
                    shape="rect"
                    coords="186,26,290,76"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?mi=1121&bbsId=1204"
                    target="_blank"
                    alt="웹진"
                  />
                  <area
                    shape="rect"
                    coords="310,26,428,76"
                    href="https://www.youtube.com/channel/UCruDceKvt2W6iZcP04JIZJw"
                    target="_blank"
                    alt="유튜브"
                  />
                  <area
                    shape="rect"
                    coords="445,26,567,76"
                    href="https://blog.naver.com/gnujinju"
                    target="_blank"
                    alt="블로그"
                  />
                  <area
                    shape="rect"
                    coords="585,26,750,76"
                    href="https://www.youtube.com/watch?v=1sjGCQ88LoI"
                    target="_blank"
                    alt="주간 GNU뉴스"
                  />
                  <area
                    coords="604, 320, 736, 345"
                    href="http://www.gnu.ac.kr"
                    shape="rect"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>''')
        file1.close()
        
        file2 = open(file='newsletter_'+ today_process +'_2.html', mode='w', encoding='UTF-8')
        file2.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ko">
  <head>
    <title>경상국립대학교 뉴스레터 제280호</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  </head>

  <body>
    <table cellpadding="0" cellspacing="0" width="100%">
      <tr>
        <td align="center">
          <table cellpadding="0" cellspacing="0" border="0" width="770px">
            <tr>
              <td width="770" height="555" style="font-size: 0">
                <img
                  src="main_280_2_01.jpg"
                  alt=""
                  width="770"
                  height="555"
                  usemap="#Map1"
                  border="0"
                />
                <map name="Map1">
                  <area
                    shape="rect"
                    coords="40, 430, 170, 555"
                    href="https://newgh.gnu.ac.kr/main/main.do"
                    target="_blank"
                    alt="경상대학교"
                  />
                  <area
                    shape="rect"
                    coords="187, 430, 310, 555"
                    href="https://newgh.gnu.ac.kr/new/main.do?mi=5419"
                    target="_blank"
                    alt="입학안내"
                  />
                  <area
                    shape="rect"
                    coords="327, 430, 450, 555"
                    href="https://newgh.gnu.ac.kr/fund/main.do"
                    target="_blank"
                    alt="발전기금"
                  />
                  <area
                    shape="rect"
                    coords="467, 430, 592, 555"
                    href="https://newgh.gnu.ac.kr/main/cm/cntnts/cntntsView.do?mi=1065&cntntsId=1185"
                    target="_blank"
                    alt="취업뉴스"
                  />
                  <area
                    shape="rect"
                    coords="607,430,730,555"
                    href="https://newgh.gnu.ac.kr/research/main.do"
                    target="_blank"
                    alt="산학협력바로가기"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="987" style="font-size: 0">
                <img
                  src="main_280_2_02.jpg"
                  alt=""
                  width="770"
                  height="987"
                  usemap="#Map2"
                  border="0"
                  href="http://www.gnu.ac.kr/"
                />
                <map name="Map2">
                  <!--개척광장 1~8번-->
                  <area
                    shape="rect"
                    coords="36,672,255,815"
                    href="https://newsis.com/view/?id=NISX20220207_0001749258&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,825,255,845"
                    href="https://newsis.com/view/?id=NISX20220215_0001760022&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,845,255,865"
                    href="https://newsis.com/view/?id=NISX20220213_0001757009&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,865,255,885"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494124"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,890,255,910"
                    href="http://www.gndomin.com/news/articleView.html?idxno=305626#0BNb"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,910,255,930"
                    href="https://www.nocutnews.co.kr/news/5705382"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,932,255,953"
                    href="https://www.cnbnews.com/news/article.html?no=531971"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,953,255,975"
                    href="https://www.youtube.com/watch?v=1sjGCQ88LoI"
                    target="_blank"
                  />


                  <!--교직원,동문 소식 1~8번-->
                  <area
                    shape="rect"
                    coords="276,672,495,815"
                    href="http://www.idomin.com/news/articleView.html?idxno=786003"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,825,495,845"
                    href="https://www.mk.co.kr/opinion/contributors/view/2022/02/135144/"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,845,495,865"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494049"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,865,495,885"
                    href="https://www.hani.co.kr/arti/opinion/column/1030910.html"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,890,495,910"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493844"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,910,495,930"
                    href="http://www.idomin.com/news/articleView.html?idxno=785232"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,932,495,953"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494011"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,953,495,975"
                    href="https://newsis.com/view/?id=NISX20220217_0001762491&cID=10812&pID=10800"
                    target="_blank"
                  />

                  <!--학술행사 1~8번-->
                  <area
                    shape="rect"
                    coords="516,672,735,815"
                    href="http://www.gndomin.com/news/articleView.html?idxno=306362"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,825,735,845"
                    href="http://www.lecturernews.com/news/articleView.html?idxno=89825"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,845,735,865"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494086"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,865,735,885"
                    href="http://www.kyosu.net/news/articleView.html?idxno=84913"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,890,735,910"
                    href="http://www.lecturernews.com/news/articleView.html?idxno=89772"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,910,735,930"
                    href="http://www.gndomin.com/news/articleView.html?idxno=305697#0BNb"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,932,735,953"
                    href="http://www.veritas-a.com/news/articleView.html?idxno=406152"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,953,735,975"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493945"
                    target="_blank"
                  />

                  <!--핫뉴스 1~3번-->
                  <area
                    shape="rect"
                    coords="35,55,365,300"
                    href="https://newsis.com/view/?id=NISX20220214_0001757319&cID=10812&pID=10800"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,55,740,167"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=493500"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,188,740,301"
                    href="https://www.mk.co.kr/news/it/view/2022/02/114449/"
                    target="_blank"
                  />

                  <!--공지사항 +아이콘-->
                  <area
                    shape="rect"
                    coords="334,357,364,387"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?bbsId=1028&mi=1126"
                    target="_blank"
                  />
                  <!--공지사항 1~5번-->
                  <area
                    shape="rect"
                    coords="25,405,362,440"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2119794"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,440,362,480"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2119384"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,480,362,520"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2122972"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,520,362,560"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?nttSn=2122543&mi=1127"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,560,362,600"
                    href="https://www.gnu.ac.kr/main/na/ntt/selectNttInfo.do?mi=1126&bbsId=1028&nttSn=2122345"
                    target="_blank"
                  />

                  <!--교육정책 +아이콘-->
                  <area
                    shape="rect"
                    coords="720,357,750,387"
                    href="https://newgh.ac.kr/"
                    target="_blank"
                  />
                  <!--교육정책 1~5번-->
                  <area
                    shape="rect"
                    coords="410,405,750,440"
                    href="https://www.donga.com/news/article/all/20220208/111659725/1"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,440,750,480"
                    href="http://www.gnnews.co.kr/news/articleView.html?idxno=494218"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,480,750,520"
                    href="http://www.newsgn.com/321888"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,520,750,560"
                    href="http://www.gndomin.com/news/articleView.html?idxno=306363"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,560,750,600"
                    href="http://www.idomin.com/news/articleView.html?idxno=785086"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="423" style="font-size: 0">
                <img
                  src="main_280_2_03.jpg"
                  alt=""
                  width="770"
                  height="423"
                  usemap="#Map3"
                  border="0"
                />
                <map name="Map3">
                  <area
                    coords="427,320,560,345"
                    href="newsletter@gnu.ac.kr"
                    shape="rect"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="35,26,164,76"
                    href="https://web.facebook.com/pioneeringGNU/"
                    target="_blank"
                    alt="페이스북"
                  />
                  <area
                    shape="rect"
                    coords="186,26,290,76"
                    href="https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?mi=1121&bbsId=1204"
                    target="_blank"
                    alt="웹진"
                  />
                  <area
                    shape="rect"
                    coords="310,26,428,76"
                    href="https://www.youtube.com/channel/UCruDceKvt2W6iZcP04JIZJw"
                    target="_blank"
                    alt="유튜브"
                  />
                  <area
                    shape="rect"
                    coords="445,26,567,76"
                    href="https://blog.naver.com/gnujinju"
                    target="_blank"
                    alt="블로그"
                  />
                  <area
                    shape="rect"
                    coords="585,26,750,76"
                    href="https://www.youtube.com/watch?v=1sjGCQ88LoI"
                    target="_blank"
                    alt="주간 GNU뉴스"
                  />
                  <area
                    coords="604, 320, 736, 345"
                    href="http://www.gnu.ac.kr"
                    shape="rect"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>''')
        file2.close()


# 현재날짜 획득
today_raw = datetime.today().strftime("%Y%m%d")
today_process = today_raw[2:]

# WorkHelper 함수 호출
app = WorkHelper(None)

# GUI 프로그램의 제목과 창 크기 등을 설정
app.title("뉴스레터 근로 도구")
app.geometry("1540x660+200+200")
app.resizable(False, False)

# mainloop 함수를 이용해 GUI 프로그램을 계속 실행
app.mainloop()

    
