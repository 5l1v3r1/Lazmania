#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Gausah pake acara Recode Recode segala ya Kontol
import math , requests , os , time , datetime , re , json , string , random , hashlib , sys
from bs4 import BeautifulSoup
from string import *


W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

def banner():
    os.system('clear')
    print (O+"                         _    "+W+"          ________________________")
    print (O+"  ,-.      __,---.__   ,',`\  "+W+"          |                      |")
    print (O+" / `.`. ,-'         `-/ /   ) "+W+"  ________| "+C+"hEllO, L4zy pe0ple!!"+W+" |")
    print (O+"(    `,'             _ \   ;  "+W+" /        |______________________|")
    print (O+" \  _( _           ,'  )/  : "+W+"_/                                 ")
    print (O+"  \ `-( `-.      ,'    /  /                            "+G+" v.5.0  ")
    print (O+"   \   \ __`.___/_,-( /_,' "+R+"_    ____ ___  _  _ ____ _  _ _ ____ ")
    print (O+"    `--'`,\_o,(_)o_,',     "+R+"|    |__|   /  |\/| |__| |\ | | |__| ")
    print (O+"        (    /`-'\    )    "+R+"|___ |  |  /__ |  | |  | | \| | |  | ")
    print (O+"         `--:\,m//`--'                                               ")
    print (O+"             `--'          "+GR+"https://github.com/N1ght420         ")

def bannerbr():
    os.system('clear')
    print (W+"       ,   ,    ")
    print ("      /////|    ")
    print ("     ///// |    ")
    print ("    |~~~|  |    ")
    print ("    |===|  |    "+C+"Brainly Answer Seeker "+O+"v.1.5"+W)
    print ("    |   |  |    "+GR+"https://github.com/N1ght420"+W)
    print ("    |   |  |    ")
    print ("    |   | /     ")
    print ("    |===|/      ")
    print ("    '---'       ")
    print ("")

def bannerlk():
    os.system('clear')
    print (R+"██████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║"+W)
    print (W+"    ██╗     ██╗  ██╗██████╗  ██╗    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     ██║ ██╔╝╚════██╗███║    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     █████╔╝  █████╔╝╚██║    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     ██╔═██╗ ██╔═══╝  ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ███████╗██║  ██╗███████╗ ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    "+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║"+R)
    print ("██████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════╝")
    print (W+"")

def bannerlk_dl():
    os.system('clear')
    print (R+"██████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                    ██"+C+" ║")
    print (W+"    ██╗     ██╗  ██╗██████╗  ██╗    "+R+"██"+C+" ║  ═════════════════════════════")
    print (W+"    ██║     ██║ ██╔╝╚════██╗███║    "+R+"██"+C+" ║"+W)
    print (W+"    ██║     █████╔╝  █████╔╝╚██║    "+R+"██"+C+" ║"+W+"   ", time.ctime())
    print (W+"    ██║     ██╔═██╗ ██╔═══╝  ██║    "+R+"██"+C+" ║"+W+"    https://layarkaca21.vip")
    print (W+"    ███████╗██║  ██╗███████╗ ██║    "+R+"██"+C+" ║"+W)
    print (W+"    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    "+R+"██"+C+" ║  ═════════════════════════════"+R)
    print ("                                    ██"+C+" ║"+W+"   https://github.com/N1ght420"+R)
    print ("██████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════╝")
    print (W+"")

def readme():
    os.system('clear')
    print ("")
    print (R+"       __   __ ")
    print (R+"      /  \./  \/\_ ")
    print (R+"   __{^\_ _}_   )  }"+G+"/^\  "+O+"  Lazy.Frmwrk "+C+"Project      ")
    print (R+"  /  /\_/^\._}_/  /"+G+"/  / ")
    print (R+" (  (__{(@)}\__}./"+G+"/_/__A____A_____A________A_____A___")
    print (R+"  \__/{/(_)\_}  )\\"+G+"\\ \\\---v-----V-----V-v----Y----v----")
    print (R+"   (   (__)_)_/  )\ "+G+"\> ")
    print (R+"    \__/     \__/\/"+G+"\/  "+W+"          Readme Doc. ")
    print (R+"       \__,--' ")
    print ("")
    print (C+" ════════════════════"+W+" Change logs"+C+" ════════════════════"+W)
    print ("")
    print (O+" ~ Ver.1.0"+W)
    print ("  - First version of this framework, including ")
    print ("    Math Tools, 0-Brain, and LKx21")
    print ("")
    print (O+" ~ Ver.1.5"+W)
    print ("  - Adding Custom Code Generator for extrap")
    print ()
    print (O+" ~ Ver.2.0"+W)
    print ("  - Fixing some bugs and adding Help and About menu")
    print ("")
    print (O+" ~ Ver.2.5"+W)
    print ("  - Interface update and Fixing some bugs on ")
    print ("    Math tools")
    print ("")
    print (O+" ~ Ver.3.0"+W)
    print ("  - This framework now using commands to run ")
    print ("    several tools on it, command that can be used ")
    print ("    included at Help menu")
    print ("")
    print (O+" ~ Ver.4.0"+W)
    print ("  - Fixing a little bug on Custom Code Generator")
    print ("")
    print (O+" ~ Ver.4.5"+W)
    print ("  - Adding Physics tools and Interface update")
    print ("")
    print (O+" ~ Ver.5.beta"+W)
    print ("  - Sorry but Physics tools have many invalid ")
    print ("    operation, now it has been deleted. ")
    print ("    Decrypt tools added")
    print ("")
    print (O+" ~ Ver.5.0"+W)
    print ("  - Adding some Generator, Checker are comingsoon")
    print ("")

def about():
    os.system('clear')
    print ("")
    print (R+"       __   __ ")
    print (R+"      /  \./  \/\_ ")
    print (R+"   __{^\_ _}_   )  }"+G+"/^\  "+O+"  Lazy.Frmwrk "+C+"Project      ")
    print (R+"  /  /\_/^\._}_/  /"+G+"/  / ")
    print (R+" (  (__{(@)}\__}./"+G+"/_/__A____A_____A________A_____A___")
    print (R+"  \__/{/(_)\_}  )\\"+G+"\\ \\\---v-----V-----V-v----Y----v----")
    print (R+"   (   (__)_)_/  )\ "+G+"\> ")
    print (R+"    \__/     \__/\/"+G+"\/  "+W+"    About Me and My Tool")
    print (R+"       \__,--' ")
    print ("")
    print (C+" Name       "+R+":"+W+" Rakka Pratama Putra")
    print (C+" Birth      "+R+":"+W+" 16 August 2003")
    print (C+" Country    "+R+":"+W+" ID")
    print (C+" Fav. Color "+R+":"+W+" White")
    print ("")
    print (C+" ═══════════════════════"+W+" About"+C+" ═══════════════════════"+W)
    print ("")
    print (" I made this framework initially just for fun")
    print (" but finally I developed this framework by adding")
    print (" some tools for lazy society out there.")
    print (" Maybe now I can only add a few tools in this framework,")
    print (" and I will continue to update them")
    print ("")

def help():
    os.system('clear')
    print ("")
    print (R+"       __   __ ")
    print (R+"      /  \./  \/\_ ")
    print (R+"   __{^\_ _}_   )  }"+G+"/^\  "+O+"  Lazy.Frmwrk "+C+"Project      ")
    print (R+"  /  /\_/^\._}_/  /"+G+"/  / ")
    print (R+" (  (__{(@)}\__}./"+G+"/_/__A____A_____A________A_____A___")
    print (R+"  \__/{/(_)\_}  )\\"+G+"\\ \\\---v-----V-----V-v----Y----v----")
    print (R+"   (   (__)_)_/  )\ "+G+"\> ")
    print (R+"    \__/     \__/\/"+G+"\/  "+W+"          How To Use")
    print (R+"       \__,--' ")
    print ("")
    print (W+" This framework uses the command to run several tools in it")
    print ("")
    print (W+" Commands that can be used, including :")
    menu()
    mathtool()
    pilbangundatar()
    pilbangunruang()
    phytool()
    crypto()
    glurus()
    glurusbc()
    glurusbl()
    medus()
    persegi()
    persegipanjang()
    layang()
    ketupat()
    trapesium()
    jajargenjang()
    segitiga()
    lingkaran()
    bola()
    balok()
    kubik()
    limas()
    main()

def glurus():
    print ('')
    print (C+' ljrr'+R+'      :'+W+' Laju Rata Rata')
    print (C+' kcrr'+R+'      :'+W+' Kecepatan Rata Rata')
    print (C+' kcs'+R+'       :'+W+' Kecepatan Sesaat')
    print (C+' plj'+R+'       :'+W+' Perlajuan')
    print (C+' pcrr'+R+'      :'+W+' Percepatan Rata Rata')
    print (C+' pcs'+R+'       :'+W+' Percepatan Sesaat')
    print (C+' glb'+R+'       :'+W+' Gerak Lurus Beraturan')
    print (C+' glbb'+R+'      :'+W+' Gerak Lurus Berubah Beraturan')
    print (C+' glbc'+R+'      :'+W+' Gerak Lurus Berubah Dipercepat')
    print (C+' glbl'+R+'      :'+W+' Gerak Lurus Berubah Diperlambat')
    print (C+' gvb'+R+'       :'+W+' Gerak Vertikal Ke Bawah')
    print (C+' gva'+R+'       :'+W+' Gerak Vertikal Ke Atas')
    print ('')

def lajurata():
    s = float(input(C+' Jarak '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    v = s/t
    print ('')
    print (C+' Laju Rata Rata '+R+'>'+W, v ,C+'m/s'+W)

def kcepatrata():
    x = float(input(C+' Perpindahan '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    v = x/t
    print ('')
    print (C+' Kecepatan Rata Rata '+R+'>'+W, v ,W)

def kcepats():
    x = float(input(C+' Perpindahan '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    v = x/t
    print ('')
    print (C+' Laju Rata Rata '+R+'>'+W, v ,W)

def plajuan():
    v = float(input(C+' Kecepatan '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = v/t
    print ('')
    print (C+' Perlajuan '+R+'>'+W, a ,C+'m/s2'+W)

def pcepatrata():
    v = float(input(C+' Kecepatan '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = v/t
    print ('')
    print (C+' Percepatan Rata Rata '+R+'>'+W, a ,W)

def pcepats():
    v = float(input(C+' Kecepatan '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = v/t
    print ('')
    print (C+' Laju Rata Rata '+R+'>'+W, a ,C+'m/s'+W)

def glurusb():
    s = float(input(C+' Jarak '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    v = s/t
    print ('')
    print (C+' Gerak Lurus Beraturan '+R+'>'+W, v ,W)

def glurusbb():
    v = float(input(C+' Jarak '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = v/t
    print ('')
    print (C+' Gerak Lurus Berubah Beraturan '+R+'>'+W, v ,W)

def glurusbcvt():
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = float(input(C+' Percepatan '+R+'> '+W))
    vt = v0+a*t
    s = v0*t+(a*t)*(a*t)*1/2
    print ('')
    print (C+' Kecepatan Akhir '+R+'>'+W, vt ,C+'m/s'+W)
    print (C+' Jarak Yang Ditempuh '+R+'>'+W, s ,C+'m'+W)

def glurusbca():
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    vt = float(input(C+' Kecepatan Akhir '+R+'> '+W))
    a = (vt-v0)/t
    s = v0*t+(a*t)*(a*t)*1/2
    print ('')
    print (C+' Percepatan '+R+'>'+W, a ,C+'m/s2'+W)
    print (C+' Jarak Yang Ditempuh '+R+'>'+W, s ,C+'m'+W)

def gverta():
    g = 10
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    tm = float(input(C+' Waktu Di Titik Tertinggi '+R+'> '+W))
    h = v0**2/(2*g)
    t = 2*tm
    vt = v0-g*t
    vt2 = v0**2-2*g*h
    print (C+' Tinggi Maksimum '+R+'>'+W, h ,C+'m/s'+W)
    print (C+' Waktu Ketika Benda Di Tanah '+R+'>'+W, t ,C+'m/s'+W)
    print (C+' Kecepatan '+R+'>'+W, vt ,C+'m/s'+W)
    print (C+' Kecepatan (vt2) '+R+'>'+W, vt2 ,C+'m/s2'+W)

def gvertb():
    g = 10
    h = float(input(C+' Ketinggian '+R+'> '+W))
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    vt = v0+g*t
    vt2 = v0**2+2*g*h
    print (C+' Kecepatan '+R+'>'+W, vt ,C+'m/s'+W)
    print (C+' Kecepatan (vt2) '+R+'>'+W, vt2 ,C+'m/s2'+W)

def glurusbc():
    print ('')
    print (C+' glbcka'+R+'    :'+W+' Kecepatan Akhir')
    print (C+' glbcpc'+R+'    :'+W+' Percepatan')
    print ('')

def glurusbl():
    print ('')
    print (C+' glblka'+R+'    :'+W+' Kecepatan Akhir')
    print (C+' glblpc'+R+'    :'+W+' Percepatan')
    print ('')

def glurusblvt():
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    a = float(input(C+' Percepatan '+R+'> '+W))
    vt = v0-a*t
    s = v0*t-1/2*(a*t)**2
    print ('')
    print (C+' Kecepatan Akhir '+R+'>'+W, vt ,C+'m/s'+W)
    print (C+' Jarak Yang Ditempuh '+R+'>'+W, s ,C+'m'+W)

def glurusbla():
    v0 = float(input(C+' Kecepatan Awal '+R+'> '+W))
    t = float(input(C+' Waktu '+R+'> '+W))
    vt = float(input(C+' Kecepatan Akhir '+R+'> '+W))
    a = (vt-v0)/t
    s = v0*t-1/2*(a*t)**2
    print ('')
    print (C+' Percepatan '+R+'>'+W, a ,C+'m/s2'+W)
    print (C+' Jarak Yang Ditempuh '+R+'>'+W, s ,C+'m'+W)

def prima():
    num = int(input(C+' Masukkan Bilangan '+R+'> '+W))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print (C+' Angka'+W, num ,R+'Bukan Bilangan Prima'+W)
                print (C+' Karena'+W, i ,C+'Dikali'+W, num//i ,R+'='+W, num)
                break
        else:
            print (C+' Angka'+W, num ,C+'Adalah Bilangan Prima'+W)

    else:
        print (C+' Angka'+W, num ,R+'Bukan Bilangan Prima'+W)

def fakt(x):
    print ("")
    print (C+' Faktor Dari'+W, x ,C+'Adalah'+W)
    for i in range(1, x+1):
        if x % i == 0:
            print (" ", i)

def faktor():
    num = int(input(C+' Masukkan Bilangan '+R+'> '+W))
    fakt(num)

def mean():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    a = str(round(sum(data) / len(data), 2))
    print(C+' Mean '+R+'>'+W, a)

def median():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print(C+' Median '+R+'>'+W, median)

def modus():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    modus = max(set(data), key=data.count)
    a = data.count(modus)
    b = []
    for i in data:
        if a - 1 < data.count(i):
            b.append(i)
    c = b[::a]
    modus1 = 'Modus data adalah '
    modus2 = []
    if len(c) == 1:
        modus1 += str(c[0])
    else:
        for i in c:
            modus2.append(str(i))
        modus1 += ' & '.join(modus2)
    
    print(C+' Modus '+R+'>'+W, modus)

def keliling_persegi () :
    x= float(input(C+' Sisi '+R+'> '+W))
    keliling = 4*x
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def luas_kubik () :
	x=float(input(C+' Sisi'+R+'> '+W))
	luas= 6*x*x
	print (' ' )
	print (C+' Luas'+R+'>'+W, luas ,C+'cm2'+W)
    
def keliling_persegipanjang () :
    x= float(input(C+' Panjang '+R+'> '+W))
    y= float(input(C+' Lebar '+R+'> '+W))
    keliling = 2*(x+y)
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def luas_balok () :
	x= float(input(C+' Panjang '+R+'> '+W))
	y= float(input(C+' Lebar '+R+'> '+W))
	z= float(input(C+' Tinggi '+R+'> '+W))
	luas= 2*((x*y)+(x*z)+(y*z))
	print (' ' )
	print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_limas () :
	x= float(input(C+' Luas Alas '+R+'> '+W))
	y= float(input(C+' Tinggi '+R+'> '+W))
	volume = 1/3*x*y
	print (' ' )
	print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
	
def keliling_segitiga () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    ca= float(input(C+' Panjang CA '+R+'> '+W))
    keliling = ab+bc+ca
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)

def luas_bola () :
	x = float(input(C+' Jari Jari '+R+'> '+W))
	luas = 4*22/7*x*x
	print ('')
	print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
              
def keliling_jajargenjang () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    cd= float(input(C+' Panjang CD '+R+'> '+W))
    da= float(input(C+' Panjang DA '+R+'> '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)

def keliling_trapesium () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    cd= float(input(C+' Panjang CD '+R+'> '+W))
    da= float(input(C+' Panjang DA '+R+'> '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
             
def keliling_ketupat () :
    z= float(input(C+' Sisi '+R+'> '+W))
    keliling = 4*z
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def keliling_layang () :
	ab= float(input(C+' Panjang AB '+R+'> '+W))
	bc= float(input(C+' Panjang BC '+R+'> '+W))
	keliling = 2*(ab+bc)
	print (' ' )
	print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)


def luas_persegi () :
    x= float(input(C+' Sisi '+R+'> '+W))
    luas= x*x
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_kubik () :
    x=float(input(C+' Sisi '+R+'> '+W))
    volume= x*x*x
    print (' ' )
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
    
def luas_persegipanjang () :
    x= float(input(C+' Panjang'+R+'> '+W))
    y= float(input(C+' Lebar'+R+'> '+W))
    luas= x*y
    print (' ' )
    print (C+' Luas'+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_balok () :
    x= float(input(C+' Panjang '+R+'> '+W))
    y= float(input(C+' Lebar '+R+'> '+W))
    z= float(input(C+' Tinggi '+R+'> '+W))
    volume= x*y*z
    print (' ' )
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
    
def luas_segitiga () :
    x= float(input(C+' Alas '+R+'> '+W))
    y= float(input(C+' Tinggi '+R+'> '+W))
    luas=0.5*x*y
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def luas_lingkaran () :
    x = float(input(C+' Jari Jari '+R+'> '+W))
    luas = 22/7*x*x
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def volume_bola () :
    x = float(input(C+' Jari Jari '+R+'> '+W))
    volume = 4/3*22/7*x*x*x
    print ('')
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
              
def luas_jajargenjang () :
    x= float(input(C+' Tinggi '+R+'> '+W))
    y= float(input(C+' Alas '+R+'> '+W))
    luas = x*y
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def luas_trapesium () :
    x= float(input(C+' Sisi Atas '+R+'> '+W))
    y= float(input(C+' Sisi Bawah '+R+'> '+W))
    z= float(input(C+' Tinggi '+R+'> '+W))
    luas = (x+y)*z/2
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
             
def luas_ketupat () :
    x= float(input(C+' Diagonal 1 '+R+'> '+W))
    y= float(input(C+' Diagonal 2 '+R+'> '+W))
    luas = 0.5*x*y
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def luas_layang () :
    x= float(input(C+' Diagonal 1 '+R+'> '+W))
    y= float(input(C+' Diagonal 2 '+R+'> '+W))
    luas = 0.5*x*y
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
	
def medus() :      
    print ('')
    print (C+' mean'+R+'      :'+W+' Mean')
    print (C+' med'+R+'       :'+W+' Median')
    print (C+' mod'+R+'       :'+W+' Modus')
    print ('')

def persegi():
    print ('')
    print (C+' kp'+R+'        :'+W+' Keliling Persegi')
    print (C+' lp'+R+'        :'+W+' Luas Persegi')
    print ('')

def persegipanjang():
    print ('')
    print (C+' kpp'+R+'       :'+W+' Keliling Persegi Panjang')
    print (C+' lpp'+R+'       :'+W+' Luas Persegi Panjang')
    print ('')

def layang():
    print ('')
    print (C+' kll'+R+'       :'+W+' Keliling Layang Layang')
    print (C+' lll'+R+'       :'+W+' Luas Layang Layang')
    print ('')

def ketupat():
    print ('')
    print (C+' kbk'+R+'       :'+W+' Keliling Belah Ketupat')
    print (C+' lbk'+R+'       :'+W+' Luas Belah Ketupat')
    print ('')

def trapesium():
    print ('')
    print (C+' kt'+R+'        :'+W+' Keliling Trapesium')
    print (C+' lt'+R+'        :'+W+' Luas Trapesium')
    print ('')

def jajargenjang():
    print ('')
    print (C+' kjg'+R+'       :'+W+' Keliling Jajar Genjang')
    print (C+' ljg'+R+'       :'+W+' Luas Jajar Genjang')
    print ('')

def segitiga():
    print ('')
    print (C+' kst'+R+'       :'+W+' Keliling Segitiga')
    print (C+' lst'+R+'       :'+W+' Luas Segitiga')
    print ('')

def lingkaran():
    print ('')
    print (C+' klk'+R+'       :'+W+' Keliling Lingkaran')
    print (C+' llk'+R+'       :'+W+' Luas Lingkaran')
    print ('')

def bola():
    print ('')
    print (C+' kbl'+R+'       :'+W+' Keliling Bola')
    print (C+' vbl'+R+'       :'+W+' Volume Bola')
    print ('')

def balok():
    print ('')
    print (C+' kb'+R+'        :'+W+' Keliling Balok')
    print (C+' vb'+R+'        :'+W+' Volume Balok')
    print ('')

def kubik():
    print ('')
    print (C+' kk'+R+'        :'+W+' Keliling Kubik')
    print (C+' vk'+R+'        :'+W+' Volume Kubik')
    print ('')

def limas():
    print ('')
    print (C+' kl'+R+'        :'+W+' Keliling Limas')
    print (C+' vl'+R+'        :'+W+' Volume Limas')
    print ('')

def pilbangundatar() :		
    print ('')
    print (C+' bdp'+R+'       :'+W+' Persegi')
    print (C+' bdpp'+R+'      :'+W+' Persegi Panjang')
    print (C+' bdst'+R+'      :'+W+' Segitiga')
    print (C+' bdlk'+R+'      :'+W+' Lingkaran')
    print (C+' bdjg'+R+'      :'+W+' Jajar Genjang')
    print (C+' bdt'+R+'       :'+W+' Trapesium')
    print (C+' bdbk'+R+'      :'+W+' Belah Ketupat')
    print (C+' bdll'+R+'      :'+W+' Layang Layang')
    print ('')

def pilbangunruang() :      
    print ('')
    print (C+' brk'+R+'       :'+W+' Kubik')
    print (C+' brb'+R+'       :'+W+' Balok')
    print (C+' brl'+R+'       :'+W+' Limas')
    print (C+' brbl'+R+'      :'+W+' Bola')
    print ('')

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

string_list = ascii_letters

def generateHashFromString(hashMethod, cleartextString):
    if hashMethod == "md5":
        return hashlib.md5(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha1":
        return hashlib.sha1(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha224":
        return hashlib.sha224(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha256":
        return hashlib.sha256(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha384":
        return hashlib.sha384(cleartextString.encode()).hexdigest()
    
    elif hashMethod == "sha512":
        return hashlib.sha512(cleartextString.encode()).hexdigest()
    else:
        pass

def reverseString(string):
    return string[::-1]

def IndexErrorCheck(index_input):
    if len(string_list) <= index_input:
        pass
    else:
        return string_list[index_input]

def StringGenerator(string):
    if len(string) <= 0:
        string.append(string_list[0])
    else:
        # error checking needs to be done, otherwise a ValueError will raise
        string[0] = IndexErrorCheck((string_list.index(string[0]) + 1) % len(string_list))
        if string_list.index(string[0]) == 0:
            return [string[0]] + StringGenerator(string[1:])
    return string

def demd5():
    hashMethod = "md5"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def desha1():
    hashMethod = "sha1"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def desha224():
    hashMethod = "sha224"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def desha256():
    hashMethod = "sha256"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def desha384():
    hashMethod = "sha384"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def desha512():
    hashMethod = "sha512"
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString("".join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+" String "+R+">"+W+" {}".format(formatted_string))
            main()

def brainly():
    bannerbr()
    a = input(C+" Pertanyaan "+R+"> "+W)
    payload = {"query":a}
    url = "https://brainly.co.id/api/28/api_tasks/suggester"
    scrap = json.loads(requests.get(url, params=payload).text)
    try:
       os.system('clear')
       qtion = scrap['data']['tasks']['items'][0]['task']['content']
       qtion = qtion.replace("<br />","\n").replace("<span>","").replace("</span>","")
       bannerbr()
       print (C+" ["+W+" PERTANYAAN "+C+"]\n\n"+W+" ",qtion)
    except:
        bannerbr()
        print (C+" ["+W+" 404 "+C+"]"+R+" >"+W+" Soal tidak dapat ditemukan")
        print ("")
        exit()
    try:
        for x in range(100):
            ans = scrap['data']['tasks']['items'][0]['responses'][x]['content']
            ans = ans.replace("<br />","\n").replace("<span>","").replace("</span>","")
            print ("")
            print (C+" [ "+W+"Jawaban " + str(x+1) + C+" ]\n\n"+W + ans)
    except:
        print ("")
        print (C+" [ "+W+"Hanya dapat mengambil"+C+" ]"+R+" > "+W+ str(x) +" Jawaban")
        print ("")

def lk21():
    bannerlk()
    a = input(C+" Judul "+R+"> "+W)
    payload = {"s":a}
    req = requests.get("https://dunia21.net/", params=payload).text
    soup = BeautifulSoup(req, "html.parser")
    linknya = soup.find_all('h2')
    link = linknya[2]
    judul = re.search(r'<a href="https://dunia21.net/(.*)/" rel="bookmark"', str(link)).group(1)
    try:
        bannerlk_dl()
        print (C+" ["+W+" JUDUL "+C+"]"+R+" >"+W+" ",str(judul))
        print ("")
        dload = "https://dl.layarkaca21.vip/get/" + judul
        bpass = "https://dl.layarkaca21.vip/verifying.php"
        data = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Accept":"*/*",
                "X-Requested-With":"XMLHttpRequest"}
        payload2 = {"slug":judul}
        req2 = requests.post(bpass, headers=data, params=payload2).text
        soup2 = BeautifulSoup(req2, "html.parser")
        linkdownload = soup2.find_all('a')
        p360 = re.findall(r'btn-360" href="(.*)" rel=', str(linkdownload))
        if len(p360) > 0:
            for laz1 in p360:
                print(C+" ["+W+" 360 P "+C+"]"+R+" >"+W+" ",laz1)
        p480 = re.findall(r'btn-480" href="(.*)" rel=', str(linkdownload))
        if len(p480) > 0:
            for laz2 in p480:
                print(C+" ["+W+" 480 P "+C+"]"+R+" >"+W+" ",laz2)
        p720 = re.findall(r'btn-720" href="(.*)" rel=', str(linkdownload))
        if len(p720) > 0:
            for laz3 in p720:
                print(C+" ["+W+" 720 P "+C+"]"+R+" >"+W+" ",laz3)
        p1080 = re.findall(r'btn-1080" href="(.*)" rel=', str(linkdownload))
        if len(p1080) > 0:
            for laz4 in p1080:
                print(C+" ["+W+" 1080P "+C+"]"+R+" >"+W+" ",laz4)
    except:
        print (C+" ["+W+" 404 "+C+"]"+R+" >"+W+" Film tidak ditemukan")
    print ("")

def hma() :
    total = int(input(C+" Total "+R+"> "+W))
    def rand(chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(6))
    for i in range(total):
        asd = rand()
        print (' '+asd+'-'+asd+'-'+asd)


def generate() :
    pil = str(input(C+" Input Base (y/n) ? "+R+"> "+W))
    if pil == 'n' or pil == 'N' :
        size = int(input(C+" Jumlah digit kode "+R+"> "+W))
        case = str(input(C+" UPPER/lower (U/l) ? "+R+"> "+W))
        total = int(input(C+" Total kode "+R+"> "+W))
        if case == 'u' or case == 'U' :
            def rand(chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            for i in range(total):
                print (' '+rand())
        elif case == 'l' or case == 'L' :
            def rand(chars=string.ascii_lowercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            for i in range(total):
                print (' '+rand())
    elif pil == 'y' or pil == 'Y' :
        base = str(input(C+' Base '+R+'> '+W))
        size = int(input(C+" Jumlah digit kode "+R+"> "+W))
        case = str(input(C+" UPPER/lower (U/l) ? "+R+"> "+W))
        total = int(input(C+" Total kode "+R+"> "+W))
        if case == 'u' or case == 'U' :
            def rand(chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size-len(base)))
            for i in range(total):
                print (' '+base+rand())
        elif case == 'l' or case == 'L' :
            def rand(chars=string.ascii_lowercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size-len(base)))
            for i in range(total):
                print (' '+base+rand())

def betaprogram():
    print ('')
    print (O+' COMINGSOON !!'+W)
    print ('')

def gen():
    print ('')
    print (C+' hma'+R+'       :'+W+' HMA License key Generator')
    print (C+' custgen'+R+'   :'+W+' Custom Code Generator')

def crypto():
    print ('')
    print (C+' demd5'+R+'     :'+W+' Decode MD5')
    print (C+' desha1'+R+'    :'+W+' Decode SHA1')
    print (C+' desha224'+R+'  :'+W+' Decode SHA224')
    print (C+' desha256'+R+'  :'+W+' Decode SHA256')
    print (C+' desha384'+R+'  :'+W+' Decode SHA384')
    print (C+' desha512'+R+'  :'+W+' Decode SHA512')
    print ('')

def mathtool():
    print ('')
    print (C+' bd'+R+'        :'+W+' Bangun Datar')
    print (C+' br'+R+'        :'+W+' Bangun Ruang')
    print (C+' bp'+R+'        :'+W+' Bilangan Prima')
    print (C+' fb'+R+'        :'+W+' Faktor Bilangan')
    print (C+' mm'+R+'        :'+W+' Mean / Median / Modus')
    print ('')

def phytool():
    print ('')
    print (C+' gl'+R+'        :'+W+' Gerak Lurus')
    print ('')

def menu():
    print ('')
    print (C+' math'+R+'      :'+W+' Math Tool')
    print (C+' phy'+R+'       :'+W+' Physics Tool')
    print (C+' crypt'+R+'     :'+W+' Crypto Tool')
    print (C+' 0brain'+R+'    :'+W+' Brainly Seeker')
    print (C+' lkx21'+R+'     :'+W+' LK21 Bypass Shortlink')
    print (C+' gen'+R+'       :'+W+' Generator')
    print ('')
    print (C+' help'+R+'      :'+W+' Help')
    print (C+' about'+R+'     :'+W+' About')
    print (C+' readme'+R+'    :'+W+' Readme')
    print (C+' exit'+R+'      :'+W+' Exit')
    print ('')

def main():
    print ('')
    cmd = str(input(R+' > '+W))
    if cmd == 'menu' or cmd == '-m' :
        menu()
        main()
    elif cmd == 'about' or cmd == '-a' :
        about()
        main()
    elif cmd == 'help' or cmd == '-h' :
        help()
        main()
    elif cmd == 'readme' or cmd == '-r' :
        readme()
        main()
    elif cmd == 'clear' or cmd == '-c' :
        banner()
        main()
    elif cmd == 'exit' or cmd == '-e' :
        print (R+' Exitting Now'+W)
        exit()
    elif cmd == 'quit' or cmd == '-q' :
        print ('')
        print (O+" Command "+cmd+" Not Found")
        print (W+" Type ( "+C+"exit"+W+" ) to Exit Program")
        main()
    elif cmd == 'math' :
        mathtool()
        main()
    elif cmd == 'phy' :
        betaprogram()
        main()
    elif cmd == 'crypt' :
        crypto()
        main()
    elif cmd == 'gen' :
        gen()
        main()
    elif cmd == '0brain' :
        brainly()
        main()
    elif cmd == 'lkx21' :
        lk21()
        main()
    elif cmd == 'custgen' :
        generate()
        main()
    elif cmd == 'hma' :
        hma()
        main()
    elif cmd == 'bd' :
        pilbangundatar()
        main()
    elif cmd == 'br' :
        pilbangunruang()
        main()
    elif cmd == 'gl' :
        glurus()
        main()
    elif cmd == 'gml' :
        glingkar()
        main()
    elif cmd == 'bp' :
        prima()
        main()
    elif cmd == 'fb' :
        faktor()
        main()
    elif cmd == 'mm' :
        betaprogram()
        main()
    elif cmd == 'bdp' :
        persegi()
        main()
    elif cmd == 'bdpp' :
        persegipanjang()
        main()
    elif cmd == 'bdst' :
        segitiga()
        main()
    elif cmd == 'bdlk' :
        lingkaran()
        main()
    elif cmd == 'bdjg' :
        jajargenjang()
        main()
    elif cmd == 'bdt' :
        trapesium()
        main()
    elif cmd == 'bdbk' :
        ketupat()
        main()
    elif cmd == 'bdll' :
        layang()
        main()
    elif cmd == 'brk' :
        kubik()
        main()
    elif cmd == 'brb' :
        balok()
        main()
    elif cmd == 'brl' :
        limas()
        main()
    elif cmd == 'brbl' :
        bola()
        main()
    elif cmd == 'mean' :
        mean()
        main()
    elif cmd == 'med' :
        median()
        main()
    elif cmd == 'mod' :
        modus()
        main()
    elif cmd == 'kp' :
        keliling_persegi()
        main()
    elif cmd == 'lp' :
        luas_persegi()
        main()
    elif cmd == 'kpp' :
        keliling_persegipanjang()
        main()
    elif cmd == 'lpp' :
        luas_persegipanjang()
        main()
    elif cmd == 'kll' :
        keliling_layang()
        main()
    elif cmd == 'lll' :
        luas_layang()
        main()
    elif cmd == 'kbk' :
        keliling_ketupat()
        main()
    elif cmd == 'lbk' :
        luas_ketupat()
        main()
    elif cmd == 'kt' :
        keliling_trapesium()
        main()
    elif cmd == 'lt' :
        luas_trapesium()
        main()
    elif cmd == 'kjg' :
        keliling_jajargenjang()
        main()
    elif cmd == 'ljg' :
        luas_jajargenjang()
        main()
    elif cmd == 'kst' :
        keliling_segitiga()
        main()
    elif cmd == 'lst' :
        luas_segitiga()
        main()
    elif cmd == 'llk' :
        luas_lingkaran()
        main()
    elif cmd == 'kbl' :
        luas_bola()
        main()
    elif cmd == 'vbl' :
        volume_bola()
        main()
    elif cmd == 'lb' :
        luas_balok()
        main()
    elif cmd == 'vb' :
        volume_balok()
        main()
    elif cmd == 'kk' :
        luas_kubik()
        main()
    elif cmd == 'vk' :
        volume_kubik()
        main()
    elif cmd == 'vl' :
        volume_limas()
        main()
    elif cmd == 'glblka' :
        glurusblvt()
        main()
    elif cmd == 'glblpc' :
        glurusbla()
        main()
    elif cmd == 'glbl' :
        glurusbl()
        main()
    elif cmd == 'ljrr' :
        lajurata()
        main()
    elif cmd == 'kcrr' :
        kcepatrata()
        main()
    elif cmd == 'kcs' :
        kcepats()
        main()
    elif cmd == 'plj' :
        plajuan()
        main()
    elif cmd == 'pcrr' :
        pcepatrata()
        main()
    elif cmd == 'pcs' :
        pcepats()
        main()
    elif cmd == 'glb' :
        glurusb()
        main()
    elif cmd == 'glbb' :
        glurusbb()
        main()
    elif cmd == 'glbc' :
        glurusbc()
        main()
    elif cmd == 'glbl' :
        glurusbl()
        main()
    elif cmd == 'glbcka' :
        glurusbcvt()
        main()
    elif cmd == 'glbcpc' :
        glurusbca()
        main()
    elif cmd == 'gvb' :
        gvertb()
        main()
    elif cmd == 'gva' :
        gverta()
        main()
    elif cmd == 'demd5' :
        demd5()
    elif cmd == 'desha1' :
        desha1()
    elif cmd == 'desha224' :
        desha224()
    elif cmd == 'desha256' :
        desha256()
    elif cmd == 'desha384' :
        desha384()
    elif cmd == 'desha512' :
        desha512()
    else :
        print ('')
        print (O+" Command "+cmd+" Not Found")
        print (W+" Type ( "+C+"help"+W+" ) to Show Help")
        main()
banner()
main()
