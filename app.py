import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Beyza Kurtuluş | Profesyonel Matematik Eğitimi",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- GELİŞMİŞ CSS (2026 Modern Tasarım Trendleri) ---
st.markdown("""
<style>
    /* Google Fonts Entegrasyonu */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Arka Plan */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Kahraman (Hero) Başlıkları */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #1e3a8a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        font-size: 1.15rem;
        color: #475569;
        line-height: 1.8;
        margin-top: 15px;
    }

    /* İstatistik Kartları (Akademik Mavi Tonları) */
    .stat-card {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        padding: 30px 20px;
        border-radius: 24px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.2);
        transition: all 0.4s ease;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .stat-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 30px rgba(37, 99, 235, 0.35);
    }
    .stat-num {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stat-text {
        font-size: 1.1rem;
        font-weight: 400;
        opacity: 0.95;
    }

    /* Yorum Kartları */
    .testimonial-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.04);
        border-left: 5px solid #3b82f6;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .testimonial-card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        transform: scale(1.02);
    }
    .quote {
        font-style: italic;
        color: #334155;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    .author {
        margin-top: 15px;
        font-weight: 700;
        color: #0f172a;
    }
    .rating {
        color: #fbbf24;
        font-size: 1.3rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- KAHRAMAN (HERO) BÖLÜMÜ ---
st.write("<br>", unsafe_allow_html=True)
col1, space, col2 = st.columns([1.1, 0.1, 1.8])

with col1:
    # Lütfen yeni "önlüklü" fotoğrafı beyza_hoca.jpg olarak klasöre kaydedin
    try:
        st.image("beyza_hoca.jpg", use_column_width=True)
    except:
        st.error("Lütfen fotoğrafı 'beyza_hoca.jpg' adıyla kodun olduğu klasöre yükleyin.")

with col2:
    st.markdown('<div class="hero-title">Matematikte Başarının<br>Yeni Formülü</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-subtitle">
    Merhaba, ben <b>Beyza Kurtuluş</b>. Ege Üniversitesi Matematik Öğretmenliği mezunu uzman bir eğitimciyim.<br><br>
    Önlüğümü giyip tahta başına geçtiğimde tek bir amacım var: <b>Öğrencilerime matematiği sevdirmek ve onlara akademik özgüven kazandırmak!</b> 
    1. sınıftan 12. sınıfa kadar her seviyeye uygun, pedagojik temelli ve 2026 güncel müfredatına tam uyumlu ders içerikleriyle başarıyı şansa bırakmıyoruz.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    st.subheader("🌟 Eğitim Anlayışımız")
    st.markdown("""
    - 🎓 **Ege Üniversitesi** Uzmanlığı ve Formasyonu
    - 🏫 Sınıf Disiplini ile Özel Ders Birebirliğinin Mükemmel Uyumu
    - 🧠 Yeni Nesil Soru Çözüm Taktikleri (LGS, TYT, AYT)
    - 📊 Düzenli Veli Bilgilendirmesi ve Analitik Gelişim Takibi
    """)

# --- İSTATİSTİKLER ---
st.write("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">350+</div>
        <div class="stat-text">Memnun & Başarılı Öğrenci</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">1'den 12'ye</div>
        <div class="stat-text">Tüm Sınıf Kademeleri</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-num">%100</div>
        <div class="stat-text">Güven ve Akademik Özveri</div>
    </div>
    """, unsafe_allow_html=True)

# --- ÖĞRENCİ VE VELİ YORUMLARI ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #0f172a;'>Öğrencilerimiz Ne Diyor?</h2><br>", unsafe_allow_html=True)

t1, t2 = st.columns(2)
with t1:
    st.markdown("""
    <div class="testimonial-card">
        <div class="rating">★★★★★</div>
        <div class="quote">"Beyza Hocamın o beyaz önlüğüyle derse gelmesi bile kızıma ne kadar profesyonel ve ciddi bir eğitim aldığını hissettiriyor. LGS'de matematik korkumuzu onun pratik tahta çözümleri sayesinde yendik."</div>
        <div class="author">Sevim A. (8. Sınıf Velisi)</div>
    </div>
    """, unsafe_allow_html=True)
with t2:
    st.markdown("""
    <div class="testimonial-card">
        <div class="rating">★★★★★</div>
        <div class="quote">"TYT/AYT kampında netlerimi bu kadar hızlı artırabileceğimi düşünmüyordum. Ege Üniversitesi mezunu olmasının farkını, formülleri ezberletmek yerine mantığını öğretmesinde çok net görüyorsunuz."</div>
        <div class="author">Caner T. (12. Sınıf Öğrencisi)</div>
    </div>
    """, unsafe_allow_html=True)

# --- İLETİŞİM VE DETAYLI KAYIT FORMU ---
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #0f172a;'>📋 Profesyonel Özel Ders Talep Formu</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; font-size: 1.1rem;'>2026 Eğitim-Öğretim yılı planlaması ve ücretsiz ön görüşme için aşağıdaki formu doldurun.</p><br>", unsafe_allow_html=True)

with st.container():
    with st.form("kayit_formu", clear_on_submit=False):
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            ad_soyad = st.text_input("👤 Öğrenci Adı Soyadı *", placeholder="Örn: Ali Yılmaz")
            sinif = st.selectbox("📚 Sınıf Seviyesi *", [
                "Sınıf Seçin...", "1. Sınıf", "2. Sınıf", "3. Sınıf", "4. Sınıf", 
                "5. Sınıf", "6. Sınıf", "7. Sınıf", "8. Sınıf (LGS)", 
                "9. Sınıf", "10. Sınıf", "11. Sınıf", "12. Sınıf (YKS)", "Mezun (YKS)"
            ])
            telefon = st.text_input("📱 İletişim Numarası *", placeholder="05XX XXX XX XX")
            
        with col_f2:
            veli_ad = st.text_input("👥 Veli Adı Soyadı", placeholder="Örn: Ayşe Yılmaz")
            hedef = st.selectbox("🎯 Temel Hedef", [
                "Hedef Seçin...",
                "Okul Derslerine Takviye ve Not Yükseltme", 
                "LGS'ye Hazırlık", 
                "YKS (TYT/AYT) Hazırlık",
                "Temel Matematik Becerilerini Geliştirme",
                "Sınav Kaygısı ve Zaman Yönetimi"
            ])
            email = st.text_input("📧 E-Posta Adresi", placeholder="ornek@email.com")

        mesaj = st.text_area("📝 Eklemek İstedikleriniz (Öğrencinin mevcut matematik temeli, netleri, özel talepleriniz vb.)")
        
        st.markdown("<small style='color: #94a3b8;'>* İşaretli alanların doldurulması zorunludur. Bilgileriniz KVKK kapsamında gizli tutulmaktadır.</small>", unsafe_allow_html=True)
        
        # Gönder Butonu
        submit = st.form_submit_button("🚀 Talebi Gönder ve Planlamaya Başla", use_container_width=True)
        
        if submit:
            if ad_soyad and sinif != "Sınıf Seçin..." and telefon:
                st.success(f"Tebrikler! Talebiniz başarıyla alındı. Beyza Öğretmen en kısa sürede {telefon} numarası üzerinden sizinle iletişime geçecektir.")
                st.balloons()
            else:
                st.error("⚠️ Lütfen Öğrenci Adı, Sınıf Seviyesi ve Telefon Numarası alanlarını eksiksiz doldurduğunuzdan emin olun.")

# --- ALT BİLGİ (FOOTER) ---
st.write("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; border-top: 1px solid #e2e8f0; padding-top: 25px; color: #94a3b8;'>
    <p style='font-weight: 600; color: #475569;'>© 2026 Beyza Kurtuluş | Yeni Nesil Matematik Eğitimi</p>
    <p style='font-size: 0.85rem;'>📍 Eğitimlerimiz hem yüz yüze (lokasyon bazlı) hem de yüksek kaliteli online platformlarda verilmektedir.</p>
</div>
""", unsafe_allow_html=True)
