import random


oyna = True
senin_parmakların = 10
yuichi_parası = 10000000
senin_paran = 0

while oyna == True:
    seçenekler1 = ["Taş", "Kağıt", "Makas", "Oynamıyorum"]
    aciklama = input("Benim sağ elim sargılı sadece kağıt veya taş yapabilirim.")
    aciklama2 = input("Kaybedersen 5 parmağınıda alırım, kazanırsan 10 milyon yeni sana veririm.")
    senin_seçeneğin = input("Hadi Başlayalım(Taş, Kağıt, Makas, Oynamıyorum veya Devam etmek istiyorum): ")
    yuichi_seçeneği = random.choice(seçenekler1)
  

    if senin_seçeneğin == "Taş":
        yuichi_seçeneği == "Makas"
        print("Yuichi makas yaptı.")
        print("Sonuç: Sen Kazandın.")
        print("Senin parmakların = ",str(senin_parmakların)) 
        yuichi_parası -= 10000000
        senin_paran += 10000000
        oyna = False
        print("Kazadın o yüzden senin paran ",str(senin_paran)," ve benim param ",str(yuichi_parası))

    elif senin_seçeneğin == "Kağıt":
        yuichi_seçeneği == "Makas"
        print("Yuichi makas yaptı.")
        print("Sonuç: Yuichi kazandı.")
        print("Arkadaşlarının önünde küçük düştün ve sakat bir çocuğa en basit oyunda bile kaybettiğin için itibarın bitti.")
        senin_parmakların -= 5
        oyna = False
        print("Kayettin o yüzden 5 parmağını aldım -",str(senin_parmakların) ," ve benim param ", str(yuichi_parası))
                
            
    elif senin_seçeneğin == "Makas":
        yuichi_seçeneği == "Makas"
        print("Yuichi makas yaptı.")
        print("Sonuç: Berabere Kaldınız. Gidebilirsiniz.")
        oyna = False
        print("Berabere kaldık o yüzden senin parmakların",str(senin_parmakların)," ve benim param ",str(yuichi_parası))

    elif senin_seçeneğin == "Oynamıyorum":
        print("Noldu? Korktun mu yoksa??!!")
        oyna = False

    elif senin_seçeneğin != "Taş" or senin_seçeneğin != "Kağıt" or senin_seçeneğin != "Makas" or senin_seçeneğin != "Oynamıyorum":
        print("Düzgünce oyna yoksa diğer 5 parmağınıda iddaaya dahil mi etmek istiyorsun.")
