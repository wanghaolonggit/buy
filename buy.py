# -*- coding: utf-8 -*-
import requests
import threading

url = 'https://www.giftu.top/Qt/PigF/BuyPig?OID=181fa58a796b4284bcd42bd163c76c38'
headers = {
        "connection":"keep-alive",
        "content-type":"text/html",
        "X-Requested-With": "XMLHttpRequest",
        "pragma": "no-cache",
        "referer": "https://www.giftu.top/PluginView/Qt/phone/1/index.html",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"
    }
data = {'OID': '181fa58a796b4284bcd42bd163c76c38'}
numList = [
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=FCB5F0E0AC9AFC07; 6279D8D3C2C2B32346CF69B6581FBBB8=67B0A6284E3EA6AF8CEE96F4E538390BD4EA1522E1BC8CBBA1D1B91560C49574ED4FF59AEBE04341506DF4719F83261184B648702658FA42; 3C936632BE4E76B9DD1E483C2EB2D500=450BE998566DD5EEF0C897E1175068245DFFBECC1F9B37C34CC910591623F1ECE0E50C921D2DBC52; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B4747596363019A23261CA1',
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=8AC3CA16F81353E3; 6279D8D3C2C2B32346CF69B6581FBBB8=67B0A6284E3EA6AFDBD50CF19D0EBC4FB38B01AB5B74AC5105A6458B660E2EFEE3B0D7EDD6A712B8E35580F8189F3B742C76D7B3FF7A5462; 3C936632BE4E76B9DD1E483C2EB2D500=C900434D5769A41B2F1A596B9DAE124884CF63E6EC28569BBFEBBF84F206E58121742C2A5DFFE2B8; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B474759B3CF0DB01572CD31'
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=CD29C53961E92FDB; 6279D8D3C2C2B32346CF69B6581FBBB8=C78E9103787433AE1889584340DA93E792CE2A0B64D40EC69EC192EA2DE0A558CCCFE78868086E79C094F7D69EFE0A078AAF00DAF391AF80; 3C936632BE4E76B9DD1E483C2EB2D500=00465980B581DB1EAE8C5BCCB5518520B97F3F2128E1EAFC20AADD6C2AA8C26518FC186784ED4606; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B474759422A509732D1ED9A',
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=E93E247D9D590E44; 6279D8D3C2C2B32346CF69B6581FBBB8=4701F6CF2707A0F58E71CEA9FA4C46584EF3A1A76A3AAD3C5F197EC3E44C74733B6343E156B1FE21E93C8310FAB68962E86485F61D268723; 3C936632BE4E76B9DD1E483C2EB2D500=C7202151106B3B3F4248741A5914551D680BC6A06F627226C1FB99B8F465EAAD319DDF191B740ECB; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B474759F8516BC866FF99AD',
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=0191C375E700533F; 6279D8D3C2C2B32346CF69B6581FBBB8=653F369D28C8D796EF0DE035FF47218B5B1D4B8FFE684A72C5769A9E0118CC11F30826298ACF9082964C342C0DC5EF00678C2CCDAE0F0BDD; 3C936632BE4E76B9DD1E483C2EB2D500=2F4D9E9DA9DBA34CFDFCE4A769EBEE3E3F0E89060D28758A41D2BB64D4232C365702E1ACE1D95E67; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B47475905AC833C8F007522',
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=133649EEE0FC7BA9; 6279D8D3C2C2B32346CF69B6581FBBB8=084083B126605FE0B3855D734DBBF33007FC99C768FBA057B7E37FA846D7A640AB85B72B6038752F85D52B850D9B72147CB6994B240A7B7E; 3C936632BE4E76B9DD1E483C2EB2D500=39F44A130463130C0EB864EEBC6AB6E9D25BC94A70A0FE88EECEA82116D19BE021D3ED3236C68E7F; 0BFE2B2D28B84A9623459C0A45F9C06A=31E6BC170B4747597336CAB96DD8409D',
    '__jsluid=7c3fcec438e425586fccec0c0302c0b0; __jsl_clearance=1556447888.233|0|TayiW4y84nOXIj5JQTok4vg46uY%3D; 8AC3302B4D959C2160994B0E4F1D9412=54FEF289239D9507; 6279D8D3C2C2B32346CF69B6581FBBB8=653F369D28C8D796D59778AE5392F02DD88E67783E09F2EAE4FFC052C4D9BCAD964135FE61CDD31DDD9E235B8F6DDDC425CC4789B376CBC3; 3C936632BE4E76B9DD1E483C2EB2D500=367CC6D3A682757C9E6EC58A87F040BEC7352CE6AD105EE15FA6B74E35BFED21C867D4D6DE6C2B48; 0BFE2B2D28B84A9623459C0A45F9C06A=47791ADBDDE1C6963E151F6095BD9B99',
];

def test(i):
    jar = requests.cookies.RequestsCookieJar()
    oneList = numList[i].split("; ")
    for v in oneList:
        twoList = v.split("=")
        jar.set(twoList[0], twoList[1], domain='giftu.top', path='/')
    r = requests.post(url, headers=headers, data=data, cookies=jar)
    print(r.text)



i = 0
print('启动')
# 开启线程数目
tasks_number = len(numList)
print tasks_number
while i < tasks_number:
    t = threading.Thread(target=test(i))
    t.start()
    t.start()
    t.start()
    t.start()
    i +=1
    i +=1
    i +=1
    i +=1
    i +=1
    44444444444444666


print(1111)
print(1111)
print(1111)
print(1111)
    777777
    8888888
    100000
    9999999



print(2222)
print(1111)
print(1111)
print(1111)
print(1111)
print(33333)

