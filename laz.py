# -*- coding: utf-8 -*-
# Python 3
# Gausah pake acara Recode Recode segala ya Kontol
import math , requests , os , time , datetime , re , json
from bs4 import BeautifulSoup


W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

##################################################  Banner  ##################################################

def banner():
    print (R+"███████████████████████████████████████████████████████████████"+C+"═╗")
    print ("╚════════════════════════════════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                                             ██"+C+" ║"+W)
    print ("    ██╗      █████╗ ███████╗███╗   ███╗ █████╗ ███╗   ██╗    "+R+"██"+C+" ║"+W)
    print ("    ██║     ██╔══██╗╚══███╔╝████╗ ████║██╔══██╗████╗  ██║    "+R+"██"+C+" ║"+W)
    print ("    ██║     ███████║  ███╔╝ ██╔████╔██║███████║██╔██╗ ██║    "+R+"██"+C+" ║"+W)
    print ("    ██║     ██╔══██║ ███╔╝  ██║╚██╔╝██║██╔══██║██║╚██╗██║    "+R+"██"+C+" ║"+W)
    print ("    ███████╗██║  ██║███████╗██║ ╚═╝ ██║██║  ██║██║ ╚████║    "+R+"██"+C+" ║"+W)
    print ("    ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    "+R+"██"+C+" ║"+R)
    print ("                                                             ██"+C+" ║"+R)
    print ("███████████████████████████████████████████████████████████████"+C+" ║")
    print ("╚═══════════════════════════════════════════════════════════════╝"+W)
    print ("")

def bannerbr():
    os.system('clear')
    print (R+"██████████████████████████████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                                            ██"+C+" ║"+W)
    print ("     ██████╗       ██████╗ ██████╗  █████╗ ██╗███╗   ██╗    "+R+"██"+C+" ║"+W)
    print ("    ██╔═████╗      ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║    "+R+"██"+C+" ║"+W)
    print ("    ██║██╔██║█████╗██████╔╝██████╔╝███████║██║██╔██╗ ██║    "+R+"██"+C+" ║"+W)
    print ("    ████╔╝██║╚════╝██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║    "+R+"██"+C+" ║"+W)
    print ("    ╚██████╔╝      ██████╔╝██║  ██║██║  ██║██║██║ ╚████║    "+R+"██"+C+" ║"+W)
    print ("     ╚═════╝       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    "+R+"██"+C+" ║"+R)
    print ("                                                            ██"+C+" ║"+R)
    print ("██████████████████████████████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════════════════════════════╝"+W)
    print ("")

def bannermath():
    os.system('clear')
    print (R+"██████████████████████████████████████████████"+C+"═╗")
    print ("╚═══════════════════════════════════════════"+R+"██"+C+" ║"+R)
    print ("                                            ██"+C+" ║"+W)
    print ("    ███╗   ███╗ █████╗ ████████╗██╗  ██╗    "+R+"██"+C+" ║"+W)
    print ("    ████╗ ████║██╔══██╗╚══██╔══╝██║  ██║    "+R+"██"+C+" ║"+W)
    print ("    ██╔████╔██║███████║   ██║   ███████║    "+R+"██"+C+" ║"+W)
    print ("    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██║    "+R+"██"+C+" ║"+W)
    print ("    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║    "+R+"██"+C+" ║"+W)
    print ("    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    "+R+"██"+C+" ║"+R)
    print ("                                            ██"+C+" ║"+R)
    print ("██████████████████████████████████████████████"+C+" ║")
    print ("╚══════════════════════════════════════════════╝"+W)
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

def about():
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

##################################################  Banner  ##################################################
##################################################  Proses  ##################################################

def prima():
    num = int(input(C+' Masukkan Bilangan'+R+' > '+W))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print (C+' Angka'+W, num ,R+' Bukan Bilangan Prima'+W)
                print (C+' Karena '+W, i ,C+' Dikali '+W, num//i ,R+' = '+W, num)
                break
        else:
            print (C+' Angka'+W, num ,C+' Adalah Bilangan Prima'+W)

    else:
        print (C+' Angka'+W, num ,R+' Bukan Bilangan Prima'+W)

def fakt(x):
    print ("")
    print (C+' Faktor Dari'+W+ x +C+' Adalah'+W)
    for i in range(1, x+1):
        if x % i == 0:
            print (" ", i)

def faktor():
    num = int(input(C+' Masukkan Bilangan'+R+' > '+W))
    fakt(num)

def mean():
    data = str(input(C+' Masukkan Data'+R+' > '+W))
    a = str(round(sum(data) / len(data), 2))
    print(C+' Mean'+R+' > '+W+ a)

def median():
    data = str(input(C+' Masukkan Data'+R+' > '+W))
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print(C+' Median'+R+' > '+W, median)

def modus():
    data = str(input(C+' Masukkan Data'+R+' > '+W))
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
    
    print(C+' Modus'+R+' > '+W, modus)

def keliling_persegi () :
    x= float(input(C+' Sisi'+R+' > '+W))
    keliling = 4*x
    print (' ' )
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)
    
def luas_kubik () :
	x=float(input(C+' Sisi'+R+' > '+W))
	luas= 6*x*x
	print (' ' )
	print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
    
def keliling_persegipanjang () :
    x= float(input(C+' Panjang'+R+' > '+W))
    y= float(input(C+' Lebar'+R+' > '+W))
    keliling = 2*(x+y)
    print (' ' )
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)
    
def luas_balok () :
	x= float(input(C+' Panjang'+R+' > '+W))
	y= float(input(C+' Lebar'+R+' > '+W))
	z= float(input(C+' Tinggi'+R+' > '+W))
	luas= 2*((x*y)+(x*z)+(y*z))
	print (' ' )
	print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
    
def volume_limas () :
	x= float(input(C+' Luas Alas'+R+' > '+W))
	y= float(input(C+' Tinggi'+R+' > '+W))
	volume = 1/3*x*y
	print (' ' )
	print (C+' Volume'+R+' > '+W, volume ,C+'cm3'+W)
	
def keliling_segitiga () :
    ab= float(input(C+' Panjang AB'+R+' > '+W))
    bc= float(input(C+' Panjang BC'+R+' > '+W))
    ca= float(input(C+' Panjang CA'+R+' > '+W))
    keliling = ab+bc+ca
    print (' ' )
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)

def luas_bola () :
	x = float(input(C+' Jari Jari'+R+' > '+W))
	luas = 4*22/7*x*x
	print ('')
	print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
              
def keliling_jajargenjang () :
    ab= float(input(C+' Panjang AB'+R+' > '+W))
    bc= float(input(C+' Panjang BC'+R+' > '+W))
    cd= float(input(C+' Panjang CD'+R+' > '+W))
    da= float(input(C+' Panjang DA'+R+' > '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)

def keliling_trapesium () :
    ab= float(input(C+' Panjang AB'+R+' > '+W))
    bc= float(input(C+' Panjang BC'+R+' > '+W))
    cd= float(input(C+' Panjang CD'+R+' > '+W))
    da= float(input(C+' Panjang DA'+R+' > '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)
             
def keliling_ketupat () :
    z= float(input(C+' Sisi'+R+' > '+W))
    keliling = 4*z
    print ('')
    print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)
    
def keliling_layang () :
	ab= float(input(C+' Panjang AB'+R+' > '+W))
	bc= float(input(C+' Panjang BC'+R+' > '+W))
	keliling = 2*(ab+bc)
	print (' ' )
	print (C+' Keliling'+R+' > '+W, keliling ,C+'cm'+W)


def luas_persegi () :
    x= float(input(C+' Sisi'+R+' > '+W))
    luas= x*x
    print (' ' )
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
    
def volume_kubik () :
    x=float(input(C+' Sisi'+R+' > '+W))
    volume= x*x*x
    print (' ' )
    print (C+' Volume'+R+' > '+W, volume ,C+'cm3'+W)
    
def luas_persegipanjang () :
    x= float(input(C+' Panjang'+R+' > '+W))
    y= float(input(C+' Lebar'+R+' > '+W))
    luas= x*y
    print (' ' )
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
    
def volume_balok () :
    x= float(input(C+' Panjang'+R+' > '+W))
    y= float(input(C+' Lebar'+R+' > '+W))
    z= float(input(C+' Tinggi'+R+' > '+W))
    volume= x*y*z
    print (' ' )
    print (C+' Volume'+R+' > '+W, volume ,C+'cm3'+W)
    
def luas_segitiga () :
    x= float(input(C+' Alas'+R+' > '+W))
    y= float(input(C+' Tinggi'+R+' > '+W))
    luas=0.5*x*y
    print (' ' )
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)

def luas_lingkaran () :
    x = float(input(C+' Jari Jari'+R+' > '+W))
    luas = 22/7*x*x
    print ('')
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)

def volume_bola () :
    x = float(input(C+' Jari Jari'+R+' > '+W))
    volume = 4/3*22/7*x*x*x
    print ('')
    print (C+' Volume'+R+' > '+W, volume ,C+'cm3'+W)
              
def luas_jajargenjang () :
    x= float(input(C+' Tinggi'+R+' > '+W))
    y= float(input(C+' Alas'+R+' > '+W))
    luas = x*y
    print ('')
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)

def luas_trapesium () :
    x= float(input(C+' Sisi Atas'+R+' > '+W))
    y= float(input(C+' Sisi Bawah'+R+' > '+W))
    z= float(input(C+' Tinggi'+R+' > '+W))
    luas = (x+y)*z/2
    print ('')
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
             
def luas_ketupat () :
    x= float(input(C+' Diagonal 1'+R+' > '+W))
    y= float(input(C+' Diagonal 2'+R+' > '+W))
    luas = 0.5*x*y
    print ('')
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
    
def luas_layang () :
    x= float(input(C+' Diagonal 1'+R+' > '+W))
    y= float(input(C+' Diagonal 2'+R+' > '+W))
    luas = 0.5*x*y
    print (' ' )
    print (C+' Luas'+R+' > '+W, luas ,C+'cm2'+W)
	
def tanya_3M() :      
    print ('')
    print (C+' 01'+R+' :'+W+' Mean')
    print (C+' 02'+R+' :'+W+' Median')
    print (C+' 03'+R+' :'+W+' Modus')
    print ('')
    pilmenu = int(input(C+' Menu '+R+'> '+W))

    if pilmenu == 1 :
        mean()
    elif pilmenu == 2 :
        median()
    elif pilmenu == 3 :
        modus()
    else :
        tanya_3M()
def tanya_persegi():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_persegi()
    
    elif ans=='02'or ans=='2':
        luas_persegi()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_persegipanjang():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_persegipanjang()
    
    elif ans=='02'or ans=='2':
        luas_persegipanjang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_layang():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_layang()
    
    elif ans=='02'or ans=='2':
        luas_layang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_ketupat():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_ketupat()
    
    elif ans=='02'or ans=='2':
        luas_ketupat()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_trapesium():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_trapesium()
    
    elif ans=='02'or ans=='2':
        luas_trapesium()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_jajargenjang():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_jajargenjang()
    
    elif ans=='02'or ans=='2':
        luas_jajargenjang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_segitiga():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_segitiga()
    
    elif ans=='02'or ans=='2':
        luas_segitiga()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_lingkaran():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangundatar()
    
    elif ans=='02'or ans=='2':
        luas_lingkaran()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_bola():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_bola()

    elif ans=='03'or ans=='3':
        volume_bola()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_balok():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_balok()

    elif ans=='03'or ans=='3':
        volume_balok()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_kubik():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_kubik()

    elif ans=='03'or ans=='3':
        volume_kubik()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_limas():
    print ('')
    print (C+' 01'+R+' :'+W+' Keliling')
    print (C+' 02'+R+' :'+W+' Luas')
    print (C+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(C+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        pilbangunruang()

    elif ans=='03'or ans=='3':
        volume_limas()      
    else:
        print ('[!]==// Abort')
        exit()

def pilbangundatar() :		
    print ('')
    print (C+' 01'+R+' :'+W+' Persegi')
    print (C+' 02'+R+' :'+W+' Persegi Panjang')
    print (C+' 03'+R+' :'+W+' Segitiga')
    print (C+' 04'+R+' :'+W+' Lingkaran')
    print (C+' 05'+R+' :'+W+' Jajar Cenjang')
    print (C+' 06'+R+' :'+W+' Trapesium')
    print (C+' 07'+R+' :'+W+' Belah Ketupat')
    print (C+' 08'+R+' :'+W+' Layang Layang')
    print ('')
    pilmenu = int(input(C+' Menu '+R+'> '+W))

    if pilmenu == 1 :
        tanya_persegi()
    elif pilmenu == 2 :
        tanya_persegipanjang()
    elif pilmenu == 3 :
        tanya_segitiga()
    elif pilmenu == 4 :
        tanya_lingkaran()
    elif pilmenu == 5 :
        tanya_jajargenjang()
    elif pilmenu == 6 :
        tanya_trapesium()
    elif pilmenu == 7 :
        tanya_ketupat()
    elif pilmenu == 8 :
        tanya_layang()
    else :
        pilbangundatar()
def pilbangunruang() :      
    print ('')
    print (C+' 01'+R+' :'+W+' Kubik')
    print (C+' 02'+R+' :'+W+' Balok')
    print (C+' 03'+R+' :'+W+' Limas')
    print (C+' 04'+R+' :'+W+' Bola')
    print ('')
    pilmenu = int(input(C+' Menu '+R+'> '+W))

    if pilmenu == 1 :
        tanya_kubik()
    elif pilmenu == 2 :
        tanya_balok()
    elif pilmenu == 3 :
        tanya_limas()
    elif pilmenu == 4 :
        tanya_bola()
    else :
        pilbangunruang()

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

##################################################  Proses  ##################################################
##################################################   Menu   ##################################################

def mathtool() :
    bannermath()
    print (C+' 01'+R+' :'+W+' Bangun Datar')
    print (C+' 02'+R+' :'+W+' Bangun Ruang')
    print (C+' 03'+R+' :'+W+' Bilangan Prima')
    print (C+' 04'+R+' :'+W+' Faktor Bilangan')
    print (C+' 05'+R+' :'+W+' Mean / Median / Modus')
    print (C+' 00'+R+' :'+W+' Exit')
    print ('')
    pilmenu = int(input(C+' Menu '+R+'> '+W))

    if pilmenu == 1 :
        pilbangundatar()
    elif pilmenu == 2 :
        pilbangunruang()
    elif pilmenu == 3 :
        prima()
    elif pilmenu == 4 :
        faktor()
    elif pilmenu == 5 :
        tanya_3M()
    elif pilmenu == 0 :
        exit()
    else :
        bannermath()
        mathtool()

def menu():
    print (C+' 01'+R+' :'+W+' Math Tool')
    print (C+' 02'+R+' :'+W+' Brainly Seeker')
    print (C+' 03'+R+' :'+W+' LK21 Bypass Shortlink')
    print (C+' 04'+R+' :'+W+' About')
    print (C+' 00'+R+' :'+W+' Exit')
    print ('')
    pilmenu = int(input(C+' Menu '+R+'> '+W))

    if pilmenu == 1 :
        mathtool()
    elif pilmenu == 2 :
        brainly()
    elif pilmenu == 3 :
        lk21()
    elif pilmenu == 4 :
        about()
    elif pilmenu == 0 :
        exit()
    else :
        banner()
        menu()

##################################################   Menu   ##################################################

banner()
menu()
