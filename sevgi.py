import streamlit as st
from datetime import datetime
import time
import random
import pandas as pd

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Bizim Hikayemiz ❤️", page_icon="🌹", layout="wide")

# 🌙 ÖZEL TASARIM (DARK MODE & MODERN BUTONLAR)
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    h1, h2, h3 { color: #FF4B4B !important; }
    .st-expander { background-color: #262730; border: 1px solid #444; border-radius: 10px; margin-bottom: 10px; }
    .mesaj-kutusu { background-color: #1A1C24; padding: 20px; border-left: 5px solid #FF4B4B; border-radius: 5px; margin: 10px 0px; }
    .stButton>button { width: 100%; border-radius: 20px; border: 1px solid #FF4B4B; background-color: transparent; color: white; transition: 0.3s; font-weight: bold; height: 50px; }
    .stButton>button:hover { background-color: #FF4B4B; color: white; border: 1px solid #FF4B4B; }
    </style>
    """, unsafe_allow_html=True)

# 2. KENAR ÇUBUĞU (ANA MÜZİK)
with st.sidebar:
    st.title("🎵 Bizim Şarkımız")
    try:
        audio_file = open('sarki.mp3', 'rb')
        st.audio(audio_file.read(), format='audio/mp3')
    except:
        st.error("sarki.mp3 bulunamadı!")

# 3. ANA BAŞLIK
st.title("İyi ki Varsın Sevgilim... ✨")
st.write("---")

# 4. CANLI SAYAÇ ALANI
st.subheader("🗓️ Beraber Geçen Zamanımız")
sayac_alani = st.empty() 

# 5. DİJİTAL FOTOĞRAF ALBÜMÜ (28 Fotoğraf)
st.divider()
st.subheader("📸 Anılarımız (28 Özel Kare)")
cols = st.columns(3)
for i in range(1, 29): 
    try:
        with cols[(i-1) % 3]:
            st.image(f"{i}.jpg", use_container_width=True, caption=f"Anı #{i}")
    except: pass

# 6. TAKVİM (ÖZEL TARİHLER)
st.divider()
st.subheader("📅 Bizim Takvimimiz")
t_col1, t_col2, t_col3 = st.columns(3)
with t_col1: st.date_input("❤️ Yıl Dönümümüz", datetime(2025, 3, 12), disabled=True)
with t_col2: st.date_input("🎂 Benim Doğum Günüm", datetime(2026, 5, 2), disabled=True)
with t_col3: st.date_input("🥳 Senin Doğum Günün", datetime(2026, 6, 30), disabled=True)

# 7. GÜNÜN GÖREVLERİ & PUAN TABLOSU
st.divider()
col_g1, col_g2 = st.columns(2)
with col_g1:
    st.subheader("🎯 Günün Küçük Görevi")
    gorevler = [
        "Bana en sevdiğin fotoğrafımızı at! 📸", "Günün ilk kahvesini içerken beni düşün. ☕", 
        "Akşam için yemek seç! 🍲", "Bana bir sesli not at! 🎙️", "Mardin hayali kur! 🏰",
        "En sevdiğin ortak şarkımızı aç ve sonuna kadar dinle! 🎧"
    ]
    st.info(random.choice(gorevler))
with col_g2:
    st.subheader("🏆 Puan Tablosu")
    st.metric(label="👩 Senin Puanın", value="100", delta="Her Zaman Lider ❤️")

# 8. ANI HARİTAMIZ
st.divider()
st.subheader("📍 Anı ve Hayal Haritamız")
# Mardin, Burhaniye ve İzmir civarı koordinatlar
df_map = pd.DataFrame({'lat': [37.3129, 39.5052, 38.4192], 'lon': [40.7350, 26.9702, 27.1287]})
st.map(df_map)

# 9. KARAR ÇARKIMIZ
st.divider()
st.subheader("🎡 Karar Çarkımız")
if st.button("Karar Veremedik mi? Tıkla! 🎲"):
    secim = random.choice(['Film İzleyelim 🎬', 'Uzun Bir Yürüyüş 🚶‍♂️', 'Mardin Usulü Yemek 🍲', 'Yeni Bir Oyun 🎮', 'Sadece Sarılalım 🤗'])
    st.balloons()
    st.success(f"Kaderin seçimi: **{secim}**")

# 10. SENİ NEDEN SEVİYORUM (10 MADDE)
st.divider()
st.subheader("❤️ Seni Neden Çok Seviyorum?")
maddeler = {
    "✨ Küçük Detaylar": "Benim unuttuğum şeyleri bile hatırlaman beni her gün yeniden aşık ediyor.",
    "🌟 Kendim Olabilmek": "Yanında hiçbir maskeye ihtiyacım yok. En doğal halimi kabul ediyorsun.",
    "🕊️ Verdiğin Huzur": "Sesini duyduğum an tüm stresim uçup gidiyor, senin yanın benim güvenli limanım.",
    "🎞️ Doğallığın": "Analog bir makinenin vizöründen bakar gibi, beni tüm kusurlarımla sevdiğin için...",
    "🌈 Dünyamı Renklendirmen": "Sıradan bir günü tek bir mesajınla dünyanın en özel günü yapabiliyorsun.",
    "🧭 Yol Arkadaşlığın": "Hayat yolunda rotayı seninle çizmek ve elini tutarak yürümek bana güven veriyor.",
    "🎧 Ortak Sessizliğimiz": "Konuşmadan bile yan yana durarak dünyanın en anlamlı sohbetini edebildiğimiz için.",
    "🌙 Aydınlığın": "Ne zaman umudumu kaybetsem, beni o karanlıktan çekip çıkaran enerjin için...",
    "🧩 Tamamlanmak": "Ben söylemeden ne hissettiğimi bakışlarımdan anlaman seni vazgeçilmez kılıyor.",
    "🔮 Hayallerimiz": "Kurduğumuz her hayalin sonunda seninle yaşlanmak ve yeni yerler keşfetmek olduğu için."
}
for baslik, icerik in maddeler.items():
    with st.expander(baslik): st.write(icerik)

# 11. MÜZİK ALBÜMÜ (8 ŞARKI)
st.divider()
st.subheader("💿 Bizim Müzik Albümümüz")
m_cols = st.columns(2)
album_isimleri = ["Gülüşün ✨", "İlk Anımız 🎧", "Yolculuğumuz 🚗", "Seni Anlatan ❤️", "Dansımız 💃", "Eğlencemiz 🎤", "Huzurumuz 🌊", "Sonsuzluğumuz ♾️"]
for i in range(1, 9):
    with m_cols[(i-1)%2]:
        try: 
            st.markdown(f"**{album_isimleri[i-1]}**")
            st.audio(open(f"sarki{i}.mp3", 'rb').read(), format='audio/mp3')
        except: pass

# 12. ŞANS KURABİYESİ (30+ NOT)
st.divider()
st.subheader("🥠 Şans Kurabiyesi")
kurabiye_notlari = [
    "Bugün dünyanın en şanslı insanısın çünkü çok seviliyorsun! ❤️",
    "Gülüşün güneş gibi, etrafındaki her şeyi aydınlatıyor. ✨",
    "Seninle yaşlanmak, hayal edebileceğim en güzel macera. ♾️",
    "Mardin sokaklarında el ele yürüyeceğimiz günler yaklaşıyor... 🏰",
    "Analog bir makine gibi her anımızı ölümsüzleştirmek istiyorum. 📸",
    "Senin enerjin en karanlık günlerimi bile aydınlatıyor. ☀️",
    "İyi ki varsın, iyi ki benimlesin! ❤️"
]
if st.button("Bir Kurabiye Kır! 🥠"):
    st.balloons()
    st.warning(f"### Kurabiyen Diyor Ki:\n{random.choice(kurabiye_notlari)}")

# 13. ÖZEL MEKTUP (SENİN YAZDIĞIN)
st.divider()
st.subheader("💌 Kalbimden Sana")
if st.button('Özel Notumu Aç 🔓'):
    st.snow()
    st.success("""
    ### AŞKIMMM BENİMM ❤️
    
    Seninle ilk konuştuğumdan beri hep içimde bir his vardı anlamadığım ama şimdi anlıyorum o hissin ne olduğunu; o his sana duyduğum sevgi ve aşkmış. 
    
    Bana bu hisleri yaşattığın için çok teşekkür ederim aşkım, seni çok seviyorum, iyi ki varsın.
    
    Aşkım seninle yıllarımı değil ömrümü harcamak istiyorum; seninle yemeyi, seninle eğlenmeyi, seninle üzülmeyi, seninle gülmeyi, seninle ağlamayı istiyorum. İnanıyorum ki bunların hepsini ömrümüzün sonuna kadar birlikte yapacağız.
    
    Konu sen olunca benim için dünya duruyor. İstersem iki elim kanda olsun yine senin yanında olacağım. Ne yapmak istersen yapacağız, ne yaparsan yap ben arkanda değil yanında olacağım aşkım.
    
    Bazen seni kırabiliyorum ama inan kötü niyetimden değil; senin üzülmeni, senin hasta olmanı istemiyorum. Bazen bunları sana yansıtırken seni kırıyorum ama dediğim gibi, seni her şeyden çok sevdiğim için başına bir şey gelsin istemiyorum. Seni kırdığım her şey için özür dilerim güzelim.
    
    Senin her şeyini seviyorum; gözlerini, kalbini, utanmanı, unutmanı... Her şeyinle seni seviyorum aşkım benim.
    
    Sensiz geçen tek bir anım olsun istemiyorum. Hayal olsun gerçek olsun ne yaparsam yapayım seni yanımda istiyorum. Seninle dünyayı ve Mardin'i gezmek istiyorum, seninle yeni tatlar keşfetmek istiyorum. Seninle üzülmek, seninle ağlamak, seninle gülmek, seninle eğlenmek... Kısacası seni istiyorum, sen yanımda olduğun sürece her şeyi istiyorum. En önemlisi seninle bir aile olmak istiyorum, bunu her şeyden çok istiyorum.
    
    Senin bu dünyadaki hiçbir şeyden zarar görmeni istemiyorum, o yüzden çok nasihat verip belki bazen canını sıkacak duruma getiriyor olabilirim. Ama güzelim inan zarar görünce sen, benim canımdan can gidiyor. O yüzden bu nasihatlerim inşallah seni sıkmıyordur.
    
    Hayat paylaşmaya değer aşkım, o yüzden bu hayatı seninle paylaşmak istiyorum ve bu isteğimden ölüm dışında hiçbir şey vazgeçtiremez.
    
    Seni çok seviyorum ve her zaman da seveceğim aşkım benim. ❤️
    """)

# 14. SAYAÇ GÜNCELLEME
st.divider()
baslangic = datetime(2025, 3, 12, 0, 0, 0)
fark = datetime.now() - baslangic
sayac_alani.success(f"### {fark.days} Gün, {fark.seconds//3600} Saat, {(fark.seconds//60)%60} Dakika ❤️")
if st.button("🕒 Zamanı Senkronize Et (Sayacı Güncelle)"):
    st.rerun()