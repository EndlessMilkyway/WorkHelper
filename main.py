"""
    GNU Newsletter Work Helper
    
    Use Modules: tkinter, datetime, os, webbrowser
    Version: 0.1
    Email: freekyr7529@gmail.com
    
    Copyright (C) 2022, Yeong Ryeol Kim from Gyeongsang National University
    MIT License
"""

# 필요 모듈 import
import tkinter as tk
import tkinter.font
from datetime import datetime
import webbrowser

# GUI 프로그램 뼈대 및 파일 생성 함수
class WorkHelper(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        
        self.parent = parent
        self.section1()
        self.section2()
        self.section3()
        
        genandsaveButton = tk.Button(self.frame2, text="파일 생성 및 저장", font=("나눔바른고딕", 15), overrelief="groove", command=self.generateFile)
        genandsaveButton.place(x=90, y=870, width=200)
        
        copylightLabel = tk.Label(self, text="Copyright (C) 2022, Yeong Ryeol Kim from Gyeongsang National University", font=("나눔바른고딕", 12) ,fg="black")
        copylightLabel.place(x=370, y=970)
        
    def section1(self):
        self.frame1 = tk.Frame(self, width=400, height=940, relief="ridge", bd=2)
        self.frame1.place(x=20, y=20)
        
        menuLabel = tk.Label(self.frame1, text="1. 상단메뉴", font=("나눔바른고딕", 18) ,fg="black")
        menuLabel.place(x=15, y=15)
        
        self.menuEntry1 = tk.Entry(self.frame1)
        self.menuEntry1.insert(0, "https://newgh.gnu.ac.kr/main/main.do")
        self.menuEntry1.place(x=20, y=50, width=360, height=25)
        
        self.menuEntry2 = tk.Entry(self.frame1)
        self.menuEntry2.insert(0, "https://newgh.gnu.ac.kr/new/main.do?mi=5419")
        self.menuEntry2.place(x=20, y=80, width=360, height=25)
        
        self.menuEntry3 = tk.Entry(self.frame1)
        self.menuEntry3.insert(0, "https://newgh.gnu.ac.kr/fund/main.do")
        self.menuEntry3.place(x=20, y=110, width=360, height=25)
        
        self.menuEntry4 = tk.Entry(self.frame1)
        self.menuEntry4.insert(0, "https://newgh.gnu.ac.kr/main/cm/cntnts/cntntsView.do?mi=1065&cntntsId=1185")
        self.menuEntry4.place(x=20, y=140, width=360, height=25)
        
        self.menuEntry5 = tk.Entry(self.frame1)
        self.menuEntry5.insert(0, "https://newgh.gnu.ac.kr/research/main.do")
        self.menuEntry5.place(x=20, y=170, width=360, height=25)
        
        bottomMenuLabel = tk.Label(self.frame1, text="2. 하단메뉴", font=("나눔바른고딕", 18) ,fg="black")
        bottomMenuLabel.place(x=15, y=205)
        
        self.bottomMenuEntry1 = tk.Entry(self.frame1)
        self.bottomMenuEntry1.insert(0, "https://web.facebook.com/pioneeringGNU/")
        self.bottomMenuEntry1.place(x=20, y=240, width=360, height=25)
        
        self.bottomMenuEntry2 = tk.Entry(self.frame1)
        self.bottomMenuEntry2.insert(0, "https://newgh.gnu.ac.kr/main/na/ntt/selectNttList.do?mi=1121&bbsId=1204")
        self.bottomMenuEntry2.place(x=20, y=270, width=360, height=25)
        
        self.bottomMenuEntry3 = tk.Entry(self.frame1)
        self.bottomMenuEntry3.insert(0, "https://www.youtube.com/channel/UCruDceKvt2W6iZcP04JIZJw")
        self.bottomMenuEntry3.place(x=20, y=300, width=360, height=25)
        
        self.bottomMenuEntry4 = tk.Entry(self.frame1)
        self.bottomMenuEntry4.insert(0, "https://blog.naver.com/gnujinju")
        self.bottomMenuEntry4.place(x=20, y=330, width=360, height=25)
        
        self.bottomMenuEntry5 = tk.Entry(self.frame1)
        self.bottomMenuEntry5.place(x=20, y=360, width=360, height=25)
        
        noticeLabel = tk.Label(self.frame1, text="3. 공지사항", font=("나눔바른고딕", 18) ,fg="black")
        noticeLabel.place(x=15, y=395)
        
        self.noticeEntry1 = tk.Entry(self.frame1)
        self.noticeEntry1.place(x=20, y=430, width=360, height=25)
        
        self.noticeEntry2 = tk.Entry(self.frame1)
        self.noticeEntry2.place(x=20, y=460, width=360, height=25)
        
        self.noticeEntry3 = tk.Entry(self.frame1)
        self.noticeEntry3.place(x=20, y=490, width=360, height=25)
        
        self.noticeEntry4 = tk.Entry(self.frame1)
        self.noticeEntry4.place(x=20, y=520, width=360, height=25)
        
        self.noticeEntry5 = tk.Entry(self.frame1)
        self.noticeEntry5.place(x=20, y=550, width=360, height=25)
        
        edupolicyLabel = tk.Label(self.frame1, text="4. 교육정책", font=("나눔바른고딕", 18) ,fg="black")
        edupolicyLabel.place(x=15, y=585)
        
        self.edupolicyEntry1 = tk.Entry(self.frame1)
        self.edupolicyEntry1.place(x=20, y=620, width=360, height=25)
        
        self.edupolicyEntry2 = tk.Entry(self.frame1)
        self.edupolicyEntry2.place(x=20, y=650, width=360, height=25)
        
        self.edupolicyEntry3 = tk.Entry(self.frame1)
        self.edupolicyEntry3.place(x=20, y=680, width=360, height=25)
        
        self.edupolicyEntry4 = tk.Entry(self.frame1)
        self.edupolicyEntry4.place(x=20, y=710, width=360, height=25)
        
        self.edupolicyEntry5 = tk.Entry(self.frame1)
        self.edupolicyEntry5.place(x=20, y=740, width=360, height=25)
        
        githubFont = tkinter.font.Font(family="나눔바른고딕", size=12, weight="bold")
        
        githubLabel = tk.Label(self.frame1, font=githubFont, text="Github Source Code", fg="blue")
        githubLabel.place(x=20, y=790)
        githubLabel.bind("<Button-1>", lambda e:
            webbrowser.open_new_tab("https://github.com/EndlessMilkyway/WorkHelper"))
        
        emailLabel = tk.Label(self.frame1, font=('나눔바른고딕', 12), text="Email: freekyr7529@gmail.com")
        emailLabel.place(x=20, y=820)
        
        messageLabel = tk.Label(self.frame1, font=('나눔바른고딕', 12), text="유지보수 문의는 이메일로")
        messageLabel.place(x=20, y=850)
        
        message2Label = tk.Label(self.frame1, font=('나눔바른고딕', 12), text="본 프로그램은 1920x1080 해상도에 최적화 되어 있음")
        message2Label.place(x=20, y=880)

    def section2(self):
        self.frame2 = tk.Frame(self, width=400, height=940, relief="ridge", bd=2)
        self.frame2.place(x=440,y=20)
        
        parkLabel = tk.Label(self.frame2, text="5. 개척광장", font=("나눔바른고딕", 18) ,fg="black")
        parkLabel.place(x=15, y=15)
        
        self.parkEntry1 = tk.Entry(self.frame2)
        self.parkEntry1.place(x=20, y=50, width=360, height=25)
        
        self.parkEntry2 = tk.Entry(self.frame2)
        self.parkEntry2.place(x=20, y=80, width=360, height=25)
        
        self.parkEntry3 = tk.Entry(self.frame2)
        self.parkEntry3.place(x=20, y=110, width=360, height=25)
        
        self.parkEntry4 = tk.Entry(self.frame2)
        self.parkEntry4.place(x=20, y=140, width=360, height=25)
        
        self.parkEntry5 = tk.Entry(self.frame2)
        self.parkEntry5.place(x=20, y=170, width=360, height=25)
        
        self.parkEntry6 = tk.Entry(self.frame2)
        self.parkEntry6.place(x=20, y=200, width=360, height=25)
        
        self.parkEntry7 = tk.Entry(self.frame2)
        self.parkEntry7.place(x=20, y=230, width=360, height=25)
        
        self.parkEntry8 = tk.Entry(self.frame2)
        self.parkEntry8.place(x=20, y=260, width=360, height=25)
        
        alumniLabel = tk.Label(self.frame2, text="6. 교직원 동문 소식", font=("나눔바른고딕", 18) ,fg="black")
        alumniLabel.place(x=15, y=295)
        
        self.alumniEntry1 = tk.Entry(self.frame2)
        self.alumniEntry1.place(x=20, y=330, width=360, height=25)
        
        self.alumniEntry2 = tk.Entry(self.frame2)
        self.alumniEntry2.place(x=20, y=360, width=360, height=25)
        
        self.alumniEntry3 = tk.Entry(self.frame2)
        self.alumniEntry3.place(x=20, y=390, width=360, height=25)
        
        self.alumniEntry4 = tk.Entry(self.frame2)
        self.alumniEntry4.place(x=20, y=420, width=360, height=25)
        
        self.alumniEntry5 = tk.Entry(self.frame2)
        self.alumniEntry5.place(x=20, y=450, width=360, height=25)
        
        self.alumniEntry6 = tk.Entry(self.frame2)
        self.alumniEntry6.place(x=20, y=480, width=360, height=25)
        
        self.alumniEntry7 = tk.Entry(self.frame2)
        self.alumniEntry7.place(x=20, y=510, width=360, height=25)
        
        self.alumniEntry8 = tk.Entry(self.frame2)
        self.alumniEntry8.place(x=20, y=540, width=360, height=25)
        
        academiaLabel = tk.Label(self.frame2, text="7. 학술행사", font=("나눔바른고딕", 18) ,fg="black")
        academiaLabel.place(x=15, y=575)
        
        self.academiaEntry1 = tk.Entry(self.frame2)
        self.academiaEntry1.place(x=20, y=610, width=360, height=25)
        
        self.academiaEntry2 = tk.Entry(self.frame2)
        self.academiaEntry2.place(x=20, y=640, width=360, height=25)
        
        self.academiaEntry3 = tk.Entry(self.frame2)
        self.academiaEntry3.place(x=20, y=670, width=360, height=25)
        
        self.academiaEntry4 = tk.Entry(self.frame2)
        self.academiaEntry4.place(x=20, y=700, width=360, height=25)
        
        self.academiaEntry5 = tk.Entry(self.frame2)
        self.academiaEntry5.place(x=20, y=730, width=360, height=25)
        
        self.academiaEntry6 = tk.Entry(self.frame2)
        self.academiaEntry6.place(x=20, y=760, width=360, height=25)
        
        self.academiaEntry7 = tk.Entry(self.frame2)
        self.academiaEntry7.place(x=20, y=790, width=360, height=25)
        
        self.academiaEntry8 = tk.Entry(self.frame2)
        self.academiaEntry8.place(x=20, y=820, width=360, height=25)

    def section3(self):
        self.frame3 = tk.Frame(self, width=400, height=940, relief="ridge", bd=2)
        self.frame3.place(x=860,y=20)
        
        hotnewsLabel = tk.Label(self.frame3, text="8. 핫뉴스", font=("나눔바른고딕", 18) ,fg="black")
        hotnewsLabel.place(x=15, y=15)
        
        self.hotnewsEntry1 = tk.Entry(self.frame3)
        self.hotnewsEntry1.place(x=20, y=50, width=360, height=25)
        
        self.hotnewsEntry2 = tk.Entry(self.frame3)
        self.hotnewsEntry2.place(x=20, y=80, width=360, height=25)
        
        self.hotnewsEntry3 = tk.Entry(self.frame3)
        self.hotnewsEntry3.place(x=20, y=110, width=360, height=25)
        
        numLabel = tk.Label(self.frame3, text="이번 호수", font=("나눔바른고딕", 18) ,fg="black")
        numLabel.place(x=15, y=145)
        
        self.numEntry = tk.Entry(self.frame3)
        self.numEntry.place(x=20, y=180, width=360, height=25)
        
        img = tk.PhotoImage(file='example.png')
        examplePhoto = tk.Label(self.frame3, image=img)
        examplePhoto.place(x=60, y=218)
        examplePhoto.image = img
           
    def generateFile(self):
        file1 = open(file='newsletter_'+ today_process +'_1.html', mode='w', encoding='UTF-8')
        file1.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="ko">
  <head>
    <title>경상국립대학교 뉴스레터 제''' + self.numEntry.get() + '''호</title>
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
                  src="main_''' + self.numEntry.get() + '''_1_01.jpg"
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
                    href="''' + self.menuEntry1.get() + '''"
                    target="_blank"
                    alt="경상대학교"
                  />
                  <area
                    shape="rect"
                    coords="187, 430, 310, 555"
                    href="''' + self.menuEntry2.get() + '''"
                    target="_blank"
                    alt="입학안내"
                  />
                  <area
                    shape="rect"
                    coords="327, 430, 450, 555"
                    href="''' + self.menuEntry3.get() + '''"
                    target="_blank"
                    alt="발전기금"
                  />
                  <area
                    shape="rect"
                    coords="467, 430, 592, 555"
                    href="''' + self.menuEntry4.get() + '''"
                    target="_blank"
                    alt="취업뉴스"
                  />
                  <area
                    shape="rect"
                    coords="607, 430, 730, 555"
                    href="''' + self.menuEntry5.get() + '''"
                    target="_blank"
                    alt="산학협력바로가기"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="987" style="font-size: 0">
                <img
                  src="main_''' + self.numEntry.get() + '''_1_02.jpg"
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
                    href="''' + self.parkEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,825,255,845"
                    href="''' + self.parkEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,845,255,865"
                    href="''' + self.parkEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,865,255,885"
                    href="''' + self.parkEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,890,255,910"
                    href="''' + self.parkEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,910,255,930"
                    href="''' + self.parkEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,932,255,953"
                    href="''' + self.parkEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,953,255,975"
                    href="''' + self.parkEntry8.get() + '''"
                    target="_blank"
                  />


                  <!--교직원,동문 소식 1~8번-->
                  <area
                    shape="rect"
                    coords="276,672,495,815"
                    href="''' + self.alumniEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,825,495,845"
                    href="''' + self.alumniEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,845,495,865"
                    href="''' + self.alumniEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,865,495,885"
                    href="''' + self.alumniEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,890,495,910"
                    href="''' + self.alumniEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,910,495,930"
                    href=''' + self.alumniEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,932,495,953"
                    href="''' + self.alumniEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,953,495,975"
                    href="''' + self.alumniEntry8.get() + '''"
                    target="_blank"
                  />

                  <!--학술행사 1~8번-->
                  <area
                    shape="rect"
                    coords="516,672,735,815"
                    href="''' + self.academiaEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,825,735,845"
                    href="''' + self.academiaEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,845,735,865"
                    href="''' + self.academiaEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,865,735,885"
                    href="''' + self.academiaEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,890,735,910"
                    href="''' + self.academiaEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,910,735,930"
                    href="''' + self.academiaEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,932,735,953"
                    href="''' + self.academiaEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,953,735,975"
                    href="''' + self.academiaEntry8.get() + '''"
                    target="_blank"
                  />

                  <!--핫뉴스 1~3번-->
                  <area
                    shape="rect"
                    coords="35,55,365,300"
                    href="''' + self.hotnewsEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,55,740,167"
                    href="''' + self.hotnewsEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,188,740,301"
                    href="''' + self.hotnewsEntry3.get() + '''"
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
                    href="''' + self.noticeEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,440,362,480"
                    href="''' + self.noticeEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,480,362,520"
                    href="''' + self.noticeEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,520,362,560"
                    href="''' + self.noticeEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,560,362,600"
                    href="''' + self.noticeEntry5.get() + '''"
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
                    href="''' + self.edupolicyEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,440,750,480"
                    href="''' + self.edupolicyEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,480,750,520"
                    href="''' + self.edupolicyEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,520,750,560"
                    href="''' + self.edupolicyEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,560,750,600"
                    href="''' + self.edupolicyEntry5.get() + '''"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="423" style="font-size: 0">
                <img
                  src="main_''' + self.numEntry.get() + '''_1_03.jpg"
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
                    href="''' + self.bottomMenuEntry1.get() + '''"
                    target="_blank"
                    alt="페이스북"
                  />
                  <area
                    shape="rect"
                    coords="186,26,290,76"
                    href="''' + self.bottomMenuEntry2.get() + '''"
                    target="_blank"
                    alt="웹진"
                  />
                  <area
                    shape="rect"
                    coords="310,26,428,76"
                    href="''' + self.bottomMenuEntry3.get() + '''"
                    target="_blank"
                    alt="유튜브"
                  />
                  <area
                    shape="rect"
                    coords="445,26,567,76"
                    href="''' + self.bottomMenuEntry4.get() + '''"
                    target="_blank"
                    alt="블로그"
                  />
                  <area
                    shape="rect"
                    coords="585,26,750,76"
                    href="''' + self.bottomMenuEntry5.get() + '''"
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
    <title>경상국립대학교 뉴스레터 제''' + self.numEntry.get() + '''호</title>
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
                  src="main_''' + self.numEntry.get() + '''_1_01.jpg"
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
                    href="''' + self.menuEntry1.get() + '''"
                    target="_blank"
                    alt="경상대학교"
                  />
                  <area
                    shape="rect"
                    coords="187, 430, 310, 555"
                    href="''' + self.menuEntry2.get() + '''"
                    target="_blank"
                    alt="입학안내"
                  />
                  <area
                    shape="rect"
                    coords="327, 430, 450, 555"
                    href="''' + self.menuEntry3.get() + '''"
                    target="_blank"
                    alt="발전기금"
                  />
                  <area
                    shape="rect"
                    coords="467, 430, 592, 555"
                    href="''' + self.menuEntry4.get() + '''"
                    target="_blank"
                    alt="취업뉴스"
                  />
                  <area
                    shape="rect"
                    coords="607, 430, 730, 555"
                    href="''' + self.menuEntry5.get() + '''"
                    target="_blank"
                    alt="산학협력바로가기"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="987" style="font-size: 0">
                <img
                  src="main_''' + self.numEntry.get() + '''_1_02.jpg"
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
                    href="''' + self.parkEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,825,255,845"
                    href="''' + self.parkEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,845,255,865"
                    href="''' + self.parkEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,865,255,885"
                    href="''' + self.parkEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,890,255,910"
                    href="''' + self.parkEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,910,255,930"
                    href="''' + self.parkEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,932,255,953"
                    href="''' + self.parkEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="36,953,255,975"
                    href="''' + self.parkEntry8.get() + '''"
                    target="_blank"
                  />


                  <!--교직원,동문 소식 1~8번-->
                  <area
                    shape="rect"
                    coords="276,672,495,815"
                    href="''' + self.alumniEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,825,495,845"
                    href="''' + self.alumniEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,845,495,865"
                    href="''' + self.alumniEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,865,495,885"
                    href="''' + self.alumniEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,890,495,910"
                    href="''' + self.alumniEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,910,495,930"
                    href=''' + self.alumniEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,932,495,953"
                    href="''' + self.alumniEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="276,953,495,975"
                    href="''' + self.alumniEntry8.get() + '''"
                    target="_blank"
                  />

                  <!--학술행사 1~8번-->
                  <area
                    shape="rect"
                    coords="516,672,735,815"
                    href="''' + self.academiaEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,825,735,845"
                    href="''' + self.academiaEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,845,735,865"
                    href="''' + self.academiaEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,865,735,885"
                    href="''' + self.academiaEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,890,735,910"
                    href="''' + self.academiaEntry5.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,910,735,930"
                    href="''' + self.academiaEntry6.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,932,735,953"
                    href="''' + self.academiaEntry7.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="516,953,735,975"
                    href="''' + self.academiaEntry8.get() + '''"
                    target="_blank"
                  />

                  <!--핫뉴스 1~3번-->
                  <area
                    shape="rect"
                    coords="35,55,365,300"
                    href="''' + self.hotnewsEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,55,740,167"
                    href="''' + self.hotnewsEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="385,188,740,301"
                    href="''' + self.hotnewsEntry3.get() + '''"
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
                    href="''' + self.noticeEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,440,362,480"
                    href="''' + self.noticeEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,480,362,520"
                    href="''' + self.noticeEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,520,362,560"
                    href="''' + self.noticeEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="25,560,362,600"
                    href="''' + self.noticeEntry5.get() + '''"
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
                    href="''' + self.edupolicyEntry1.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,440,750,480"
                    href="''' + self.edupolicyEntry2.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,480,750,520"
                    href="''' + self.edupolicyEntry3.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,520,750,560"
                    href="''' + self.edupolicyEntry4.get() + '''"
                    target="_blank"
                  />
                  <area
                    shape="rect"
                    coords="410,560,750,600"
                    href="''' + self.edupolicyEntry5.get() + '''"
                    target="_blank"
                  />
                </map>
              </td>
            </tr>

            <tr>
              <td width="770" height="423" style="font-size: 0">
                <img
                  src="main_''' + self.numEntry.get() + '''_2_03.jpg"
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
                    href="''' + self.bottomMenuEntry1.get() + '''"
                    target="_blank"
                    alt="페이스북"
                  />
                  <area
                    shape="rect"
                    coords="186,26,290,76"
                    href="''' + self.bottomMenuEntry2.get() + '''"
                    target="_blank"
                    alt="웹진"
                  />
                  <area
                    shape="rect"
                    coords="310,26,428,76"
                    href="''' + self.bottomMenuEntry3.get() + '''"
                    target="_blank"
                    alt="유튜브"
                  />
                  <area
                    shape="rect"
                    coords="445,26,567,76"
                    href="''' + self.bottomMenuEntry4.get() + '''"
                    target="_blank"
                    alt="블로그"
                  />
                  <area
                    shape="rect"
                    coords="585,26,750,76"
                    href="''' + self.bottomMenuEntry5.get() + '''"
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
app.title("뉴스레터 근로 도구 v0.1")
app.iconbitmap("app.ico")
app.geometry("1280x1000+200+200")
app.resizable(False, False)

# mainloop 함수를 이용해 GUI 프로그램을 계속 실행
app.mainloop()

    
