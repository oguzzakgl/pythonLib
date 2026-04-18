import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from utils.reader import extract_text_from_pdf, extract_text_auto
from utils.processor import clean_data
from utils.analyzer import perform_analysis

# ═══════════════════════════════════════════════════════════════
# SAYFA YAPILANDIRMASI
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="HireSync AI — Akıllı İK Analiz Platformu",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════
# PREMIUM CSS TASARIM SİSTEMİ
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Genel Temizlik */
    * { font-family: 'Inter', sans-serif; }
    
    .main { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); }
    
    /* Streamlit varsayılan header'ı gizle */
    header[data-testid="stHeader"] { background: transparent; }
    
    /* Glass Kart Stili */
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 16px;
        padding: 20px;
    }
    
    /* İstatistik Kartı */
    .stat-card {
        background: rgba(30, 41, 59, 0.8);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(148, 163, 184, 0.08);
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .stat-card:hover {
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.15);
    }
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 16px 16px 0 0;
    }
    .stat-card.blue::before { background: linear-gradient(90deg, #3b82f6, #6366f1); }
    .stat-card.green::before { background: linear-gradient(90deg, #10b981, #34d399); }
    .stat-card.amber::before { background: linear-gradient(90deg, #f59e0b, #fbbf24); }
    
    .stat-label { color: #94a3b8; font-size: 0.8em; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
    .stat-value { font-size: 2.2em; font-weight: 800; line-height: 1; }
    .stat-value.blue { color: #60a5fa; }
    .stat-value.green { color: #34d399; }
    .stat-value.amber { color: #fbbf24; }
    
    /* Aday Satır Kartı */
    .candidate-row {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(148, 163, 184, 0.06);
        border-radius: 12px;
        padding: 12px 16px;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 12px;
        transition: all 0.2s ease;
    }
    .candidate-row:hover {
        background: rgba(51, 65, 85, 0.6);
        border-color: rgba(99, 102, 241, 0.2);
    }
    
    /* Etiket Badge */
    .tag-badge {
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.7em;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
    }
    
    /* Progress Bar */
    .progress-track {
        background: rgba(55, 65, 81, 0.8);
        border-radius: 10px;
        height: 10px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.6s ease;
    }
    
    /* Bölüm Başlıkları */
    .section-title {
        font-size: 1.3em;
        font-weight: 700;
        color: #f1f5f9;
        padding-bottom: 8px;
        margin-bottom: 16px;
        border-bottom: 2px solid rgba(99, 102, 241, 0.3);
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(16, 185, 129, 0.1) 100%);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 20px;
        padding: 32px;
        text-align: center;
        margin-bottom: 24px;
    }
    .hero-title {
        font-size: 2.4em;
        font-weight: 800;
        background: linear-gradient(135deg, #818cf8, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 4px;
    }
    .hero-subtitle {
        color: #94a3b8;
        font-size: 1em;
        font-weight: 400;
    }
    .hero-version {
        display: inline-block;
        background: rgba(99, 102, 241, 0.2);
        color: #818cf8;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 600;
        margin-top: 8px;
    }
    
    /* Footer */
    .pro-footer {
        text-align: center;
        color: #475569;
        font-size: 0.8em;
        padding: 24px 0 8px 0;
        border-top: 1px solid rgba(148, 163, 184, 0.08);
        margin-top: 40px;
    }
    .pro-footer a { color: #6366f1; text-decoration: none; }
    
    /* Sidebar Premium */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    }
    [data-testid="stSidebar"] .stMarkdown h2 { color: #f1f5f9 !important; }
    
    /* E-posta Kutusu */
    .email-preview {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(148, 163, 184, 0.1);
        border-radius: 12px;
        padding: 20px;
        font-family: 'Inter', sans-serif;
        color: #cbd5e1;
        line-height: 1.7;
    }
    
    /* Chip'ler */
    .skill-chip-match {
        display: inline-block;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(52, 211, 153, 0.1));
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78em;
        font-weight: 500;
        margin: 2px;
    }
    .skill-chip-miss {
        display: inline-block;
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(248, 113, 113, 0.08));
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.15);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78em;
        font-weight: 500;
        margin: 2px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #1e293b; }
    ::-webkit-scrollbar-thumb { background: #475569; border-radius: 3px; }
    
    /* Plotly chart arka planını şeffaf yap */
    .js-plotly-plot .plotly .main-svg { background: transparent !important; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# HERO BANNER (Marka Alanı)
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">🧠 HireSync AI</div>
    <div class="hero-subtitle">Yapay Zeka Destekli Aday Analiz ve Değerlendirme Platformu</div>
    <div class="hero-version">v2.0 PRO</div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SIDEBAR — PROFESYONEL
# ═══════════════════════════════════════════════════════════════
st.sidebar.markdown("""
<div style="text-align:center; padding:12px 0 8px;">
    <span style="font-size:2em;">🧠</span>
    <div style="font-size:1.1em; font-weight:700; color:#f1f5f9; margin-top:4px;">HireSync AI</div>
    <div style="font-size:0.75em; color:#64748b;">Akıllı İK Çözümleri</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("**📐 Skorlama Ağırlıkları**")
semantic_weight = st.sidebar.slider("Semantik Anlam Ağırlığı (%)", 10, 90, 70, 5, key="sem_w")
keyword_weight = 100 - semantic_weight
st.sidebar.caption(f"Anahtar Kelime Ağırlığı: %{keyword_weight}")

st.sidebar.markdown("---")
st.sidebar.markdown("**📄 Desteklenen Formatlar**")
st.sidebar.caption("✅ PDF  ✅ DOCX  ✅ Görsel PDF (OCR)")

st.sidebar.markdown("---")
st.sidebar.markdown("**💡 Nasıl Kullanılır?**")
st.sidebar.caption("1. İş tanımını girin\n2. CV dosyalarını yükleyin\n3. 'Analizi Başlat' butonuna tıklayın\n4. AI sonuçlarını inceleyin")

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 HireSync AI | Tüm hakları saklıdır.")

# ═══════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════
if 'df' not in st.session_state:
    st.session_state['df'] = None
if 'resumes_processed' not in st.session_state:
    st.session_state['resumes_processed'] = []

# ═══════════════════════════════════════════════════════════════
# GİRİŞ ALANLARI
# ═══════════════════════════════════════════════════════════════
input_col1, input_col2 = st.columns([1.2, 1])

with input_col1:
    st.markdown('<div class="section-title">📝 İş Tanımı</div>', unsafe_allow_html=True)
    job_desc_input = st.text_area(
        "Aranan nitelikleri ve iş tanımını detaylıca yazın:",
        "Python, Machine Learning, Scikit-learn, veri analizi ve raporlama konusunda tecrübeli adaylar.",
        height=160,
        label_visibility="collapsed"
    )

with input_col2:
    st.markdown('<div class="section-title">📂 CV Yükleme</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "PDF veya DOCX formatında CV yükleyin:",
        type=["pdf", "docx"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    if uploaded_files:
        st.caption(f"✅ {len(uploaded_files)} dosya yüklendi")
    else:
        st.caption("📎 Henüz dosya seçilmedi")

st.markdown("")
analyze_btn = st.button("🚀 Analizi Başlat", use_container_width=True, type="primary")

# ═══════════════════════════════════════════════════════════════
# ANALİZ MOTORU
# ═══════════════════════════════════════════════════════════════
if analyze_btn:
    if not job_desc_input or len(job_desc_input.strip()) < 10:
        st.error("⚠️ Lütfen en az 10 karakter uzunluğunda bir iş tanımı girin!")
    elif not uploaded_files:
        st.warning("📂 Henüz herhangi bir dosya yüklenmedi.")
    else:
        try:
            with st.status("🧠 AI Modeli Hazırlanıyor...", expanded=True) as status:
                st.write("⏳ Semantik analiz motoru yükleniyor...")
                
                job_desc_clean = clean_data(job_desc_input)
                resumes_for_analysis = []
                skipped_files = []
                
                for uploaded_file in uploaded_files:
                    try:
                        temp_path = os.path.join("data", "resumes", uploaded_file.name)
                        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
                        
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        
                        raw_text = extract_text_auto(temp_path)
                        
                        if not raw_text or len(raw_text.strip()) < 20:
                            skipped_files.append(uploaded_file.name)
                            continue
                        
                        clean_text = clean_data(raw_text)
                        
                        resumes_for_analysis.append({
                            'filename': uploaded_file.name,
                            'clean_text': clean_text,
                            'raw_text': raw_text
                        })
                    except Exception as e:
                        skipped_files.append(uploaded_file.name)
                        st.write(f"⚠️ {uploaded_file.name} atlandı: {e}")
                
                if not resumes_for_analysis:
                    st.error("❌ Hiçbir CV'den metin çıkarılamadı. Lütfen dosyalarınızı kontrol edin.")
                else:
                    st.write(f"📄 {len(resumes_for_analysis)} CV işleniyor...")
                    if skipped_files:
                        st.write(f"⚠️ Atlanan dosyalar: {', '.join(skipped_files)}")
                    
                    results = perform_analysis(job_desc_input, resumes_for_analysis, semantic_weight=semantic_weight/100, keyword_weight=keyword_weight/100)
                    
                    if results:
                        st.session_state['df'] = pd.DataFrame(results).sort_values(by="Skor", ascending=False)
                        st.session_state['resumes_processed'] = resumes_for_analysis
                    else:
                        st.error("❌ Analiz sonucu üretilemedi.")
                
            status.update(label="✅ Analiz Tamamlandı!", state="complete", expanded=False)
        except Exception as e:
            st.error(f"❌ Beklenmeyen hata: {e}")

# ═══════════════════════════════════════════════════════════════
# SONUÇLAR
# ═══════════════════════════════════════════════════════════════
if st.session_state['df'] is not None:
    df = st.session_state['df']
    resumes_processed = st.session_state['resumes_processed']
    
    if not df.empty:
        # ── İSTATİSTİK KARTLARI ──
        st.markdown("")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="stat-card blue">
                <div class="stat-label">👥 Toplam Aday</div>
                <div class="stat-value blue">{len(df)}</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="stat-card green">
                <div class="stat-label">🏆 En Yüksek Skor</div>
                <div class="stat-value green">%{round(df['Skor'].max(), 1)}</div>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="stat-card amber">
                <div class="stat-label">📊 Ortalama Skor</div>
                <div class="stat-value amber">%{round(df['Skor'].mean(), 1)}</div>
            </div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ── TOP 10 ADAY PANELİ ──
        st.markdown('<div class="section-title">🏅 En Uyumlu 10 Aday</div>', unsafe_allow_html=True)
        top10 = df.head(10)
        
        tag_colors = {
            'AI/ML': '#8b5cf6', 'Frontend': '#3b82f6', 'Backend': '#10b981',
            'Full-Stack': '#f59e0b', 'Mobil': '#ec4899', 'DevOps': '#6366f1',
            'Veri Mühendisi': '#14b8a6', 'Siber Güvenlik': '#ef4444',
            'Oyun Geliştirici': '#f97316', 'Genel': '#64748b'
        }
        
        for idx, row in enumerate(top10.itertuples(), 1):
            medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(idx, f"<span style='color:#64748b;font-weight:600;'>{idx}.</span>")
            tag = getattr(row, 'Etiket', 'Genel')
            tag_color = tag_colors.get(tag, '#64748b')
            score_color = "#34d399" if row.Skor >= 70 else "#fbbf24" if row.Skor >= 40 else "#f87171"
            
            c1, c2, c3 = st.columns([4, 1, 1])
            c1.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:6px 0;">
                <span style="font-size:1.3em;min-width:28px;">{medal}</span>
                <span style="font-weight:600;color:#f1f5f9;">{row.Aday.replace('.pdf','').replace('.docx','')}</span>
                <span class="tag-badge" style="background:{tag_color};">{tag}</span>
            </div>
            """, unsafe_allow_html=True)
            c2.markdown(f"<div style='padding-top:8px;color:{score_color};font-weight:700;font-size:1.1em;'>%{round(row.Skor, 1)}</div>", unsafe_allow_html=True)
            
            cv_path = os.path.join("data", "resumes", row.Aday)
            if os.path.exists(cv_path):
                with open(cv_path, "rb") as cv_file:
                    c3.download_button("📥 CV", cv_file.read(), row.Aday, "application/pdf", key=f"dl_{idx}_{row.Aday}")
            else:
                c3.write("")
        
        st.markdown("---")
        
        # ── TOP 5 KARŞILAŞTIRMA ──
        st.markdown('<div class="section-title">🆚 En İyi 5 Aday Karşılaştırması</div>', unsafe_allow_html=True)
        top5 = df.head(5)
        
        if len(top5) >= 2:
            categories = ['Genel Uyum', 'Semantik Anlam', 'Anahtar Kelime']
            colors = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6']
            
            fig_compare = go.Figure()
            for idx, row in enumerate(top5.itertuples()):
                name_short = row.Aday.replace('.pdf', '').replace('.docx', '').replace('_', ' ')[:20]
                fig_compare.add_trace(go.Scatterpolar(
                    r=[row.Skor, row.Semantik_Skor, row.Anahtar_Kelime_Skor],
                    theta=categories, fill='toself', name=name_short,
                    line_color=colors[idx % len(colors)], opacity=0.7
                ))
            
            fig_compare.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100], gridcolor='rgba(148,163,184,0.1)'),
                    angularaxis=dict(gridcolor='rgba(148,163,184,0.1)')
                ),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.3, font=dict(color='#94a3b8')),
                margin=dict(l=60, r=60, t=30, b=80),
                height=420,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94a3b8')
            )
            st.plotly_chart(fig_compare, use_container_width=True)
            
            compare_data = []
            for row in top5.itertuples():
                name_short = row.Aday.replace('.pdf', '').replace('.docx', '').replace('_', ' ')
                matched = row.Eşleşen_Yetkinlikler if isinstance(row.Eşleşen_Yetkinlikler, list) else []
                missing = row.Eksik_Yetkinlikler if isinstance(row.Eksik_Yetkinlikler, list) else []
                compare_data.append({
                    'Aday': name_short,
                    'Genel %': round(row.Skor, 1),
                    'Semantik %': round(row.Semantik_Skor, 1),
                    'Kelime %': round(row.Anahtar_Kelime_Skor, 1),
                    'Eşleşen': ', '.join(matched[:5]),
                    'Eksik': ', '.join(missing[:3])
                })
            
            st.dataframe(pd.DataFrame(compare_data), use_container_width=True, hide_index=True)
        else:
            st.info("Karşılaştırma için en az 2 aday gerekli.")
        
        st.markdown("---")
        
        # ── GENEL SIRALAMA ──
        st.markdown('<div class="section-title">📊 Genel Sıralama</div>', unsafe_allow_html=True)
        display_cols = ['Aday', 'Skor', 'Semantik_Skor', 'Anahtar_Kelime_Skor']
        if 'Etiket' in df.columns:
            display_cols.insert(1, 'Etiket')
        st.dataframe(df[display_cols], use_container_width=True, hide_index=True)
        
        # ── EXCEL EXPORT ──
        st.markdown('<div class="section-title">📥 Rapor İndir</div>', unsafe_allow_html=True)
        if not df.empty:
            export_df = df.copy()
            
            def flatten_contact(row):
                c = row.get('Iletisim', {}) if isinstance(row.get('Iletisim'), dict) else {}
                return pd.Series({
                    'E-posta': ", ".join(c.get('emails', [])),
                    'Telefon': ", ".join(c.get('phones', [])),
                    'LinkedIn': ", ".join(c.get('linkedin', [])),
                    'GitHub': ", ".join(c.get('github', []))
                })
            
            contact_info = export_df.apply(flatten_contact, axis=1)
            export_df = pd.concat([export_df, contact_info], axis=1)
            
            cols_to_keep = ['Aday', 'Skor', 'Semantik_Skor', 'Anahtar_Kelime_Skor', 'Etiket', 'E-posta', 'Telefon', 'LinkedIn', 'GitHub', 'Ozet']
            cols_to_keep = [c for c in cols_to_keep if c in export_df.columns]
            export_df = export_df[cols_to_keep]
            
            export_df = export_df.rename(columns={
                'Aday': 'Aday Adı',
                'Skor': 'Genel Uyumluluk (%)',
                'Semantik_Skor': 'Anlam Benzerliği (%)',
                'Anahtar_Kelime_Skor': 'Anahtar Kelime Eşleşmesi (%)',
                'Etiket': 'Uzmanlık Alanı',
                'Ozet': 'AI Değerlendirmesi'
            })
            
            from io import BytesIO
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                export_df.to_excel(writer, index=False, sheet_name='Aday_Analizi')
            
            st.download_button(
                label="📊 Tüm Sonuçları Excel Olarak İndir",
                data=output.getvalue(),
                file_name="HireSync_AI_Rapor.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        
        st.markdown("---")
        
        # ── E-POSTA ŞABLONU ──
        # ── TOPLU MÜLAKAT DAVETİ (OUTLOOK/GMAIL ENTEGRASYONU) ──
        st.markdown('<div class="section-title">✉️ Toplu Mülakat Daveti (v2.0 PRO)</div>', unsafe_allow_html=True)
        
        email_col1, email_col2 = st.columns(2)
        with email_col1:
            selected_emails = st.multiselect(
                "Mülakata Çağrılacak Adayları Seçin:", 
                df['Aday'].unique().tolist(), 
                default=df['Aday'].unique().tolist()[:1] if len(df) > 0 else None,
                key="bulk_email_candidates"
            )
            company_name = st.text_input("Şirket Adı:", "ABC Teknoloji", key="company_name")
        with email_col2:
            position_name = st.text_input("Pozisyon:", "Yazılım Mühendisi", key="position_name")
            interview_date = st.text_input("Mülakat Tarihi:", "20 Mart 2026, Saat 14:00", key="interview_date")
        
        if selected_emails:
            import urllib.parse
            st.markdown(f"**Seçilen Aday Sayısı:** `{len(selected_emails)}`")
            
            for candidate in selected_emails:
                try:
                    cand_row = df[df['Aday'] == candidate].iloc[0]
                    cand_name = candidate.replace('.pdf', '').replace('.docx', '').replace('_', ' ').title()
                    matched = cand_row.get('Eşleşen_Yetkinlikler', [])
                    contact = cand_row.get('Iletisim', {})
                    cand_email = contact.get('emails', [''])[0] if isinstance(contact, dict) and contact.get('emails') else ''
                    
                    skills_text = ', '.join(matched[:3]) if matched else 'teknik yetkinlikleriniz'
                    
                    subject = f"{company_name} - {position_name} Pozisyonu Mülakat Daveti"
                    body = f"""Sayın {cand_name},

{company_name} bünyesinde açık olan {position_name} pozisyonu için özgeçmişinizi inceledik. Özellikle {skills_text} alanlarındaki deneyiminiz dikkatimizi çekmiştir.

Sizi daha yakından tanımak ve pozisyon hakkında detaylı bilgi paylaşmak adına, {interview_date} tarihinde bir mülakat gerçekleştirmek istiyoruz.

Müsaitlik durumunuzu bizimle paylaşmanızı rica ederiz.

Saygılarımızla,
İnsan Kaynakları Departmanı
{company_name}"""
                    
                    # Mailto bağlantısı oluştur (Outlook/Gmail uyumlu)
                    mailto_link = f"mailto:{cand_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                    
                    with st.expander(f"📝 {cand_name} (Sıradaki: {cand_email if cand_email else 'E-posta Bulunamadı'})"):
                        st.text_area(f"Mesaj Önizleme ({cand_name}):", body, height=200, key=f"body_{candidate}")
                        
                        if cand_email:
                            st.markdown(f"""
                                <a href="{mailto_link}" target="_blank" style="text-decoration: none;">
                                    <div style="background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); 
                                                color: white; padding: 10px 20px; border-radius: 8px; 
                                                text-align: center; font-weight: 600; cursor: pointer; 
                                                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);">
                                        ✉️ Outlook / Gmail ile Hemen Gönder
                                    </div>
                                </a>
                                """, unsafe_allow_html=True)
                        else:
                            st.warning("⚠️ Bu adayın CV'sinde e-posta adresi bulunamadı. Lütfen manuel ekleyin.")
                            manual_email = st.text_input(f"E-posta Adresi Girin ({cand_name}):", key=f"manual_email_{candidate}")
                            if manual_email:
                                updated_mailto = f"mailto:{manual_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
                                st.markdown(f'<a href="{updated_mailto}" target="_blank" style="text-decoration: none;"><div style="background: #6366f1; color: white; padding: 10px; border-radius: 8px; text-align: center;">✉️ Gönder</div></a>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"{candidate} için e-posta hazırlanamadı: {e}")
        else:
            st.info("💡 Yukarıdan mülakata çağırmak istediğiniz adayları seçtiğinizde, her biri için otomatik davet butonları burada görünecektir.")
        
        st.markdown("---")
        
        # ── DETEKTİF RAPOR ──
        st.markdown('<div class="section-title">🔍 Profesyonel Aday Analiz Raporu</div>', unsafe_allow_html=True)
        
        selected_candidate = st.selectbox("Raporunu görüntülemek istediğiniz adayı seçin:", df['Aday'].unique().tolist())
        
        if selected_candidate:
            cand_data = df[df['Aday'] == selected_candidate].iloc[0]
            
            # AI Özet
            st.info(f"💡 **AI Değerlendirmesi:** {cand_data['Ozet']}")
            
            rep_col1, rep_col2 = st.columns([1, 1.2])
            
            with rep_col1:
                st.markdown("#### 🎯 Yetkinlik Dağılımı")
                categories = ['Genel', 'Semantik', 'Anahtar Kelime']
                cand_scores = [cand_data['Skor'], cand_data['Semantik_Skor'], cand_data['Anahtar_Kelime_Skor']]
                
                fig_radar = go.Figure()
                fig_radar.add_trace(go.Scatterpolar(
                    r=cand_scores, theta=categories, fill='toself',
                    name=selected_candidate, line_color='#6366f1',
                    fillcolor='rgba(99, 102, 241, 0.2)'
                ))
                fig_radar.update_layout(
                    polar=dict(
                        radialaxis=dict(visible=True, range=[0, 100], gridcolor='rgba(148,163,184,0.1)'),
                        angularaxis=dict(gridcolor='rgba(148,163,184,0.1)')
                    ),
                    showlegend=False,
                    margin=dict(l=40, r=40, t=20, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='#94a3b8')
                )
                st.plotly_chart(fig_radar, use_container_width=True)
                
                # İletişim
                st.markdown("#### 📫 İletişim Bilgileri")
                contact = cand_data.get('Iletisim', {'emails': [], 'phones': [], 'linkedin': [], 'github': []})
                if not isinstance(contact, dict):
                    contact = {'emails': [], 'phones': [], 'linkedin': [], 'github': []}
                
                if contact.get('emails') or contact.get('phones') or contact.get('linkedin') or contact.get('github'):
                    contact_text = ""
                    if contact.get('emails'):
                        contact_text += f"📧 **E-posta:** {', '.join(contact['emails'])}\n\n"
                    if contact.get('phones'):
                        contact_text += f"📞 **Telefon:** {', '.join(contact['phones'])}\n\n"
                    if contact.get('linkedin'):
                        links = [f"[{l}]({l if l.startswith('http') else 'https://'+l})" for l in contact['linkedin']]
                        contact_text += f"🔗 **LinkedIn:** {', '.join(links)}\n\n"
                    if contact.get('github'):
                        links = [f"[{l}]({l if l.startswith('http') else 'https://'+l})" for l in contact['github']]
                        contact_text += f"💻 **GitHub:** {', '.join(links)}"
                    st.info(contact_text)
                else:
                    st.warning("İletişim bilgisi saptanamadı.")
                
                # Bölüm Skorları
                st.markdown("**📂 Bölüm Bazlı Uyumluluk:**")
                for sec, score in cand_data['Bolum_Skorlari'].items():
                    if score > 0 and sec != 'Diğer':
                        display_score = min(round(float(score), 1), 100)
                        bar_color = "#34d399" if display_score >= 70 else "#fbbf24" if display_score >= 40 else "#f87171"
                        st.markdown(f"""
                        <div style="display:flex; align-items:center; gap:10px; margin-bottom:6px;">
                            <span style="min-width:110px; font-weight:600; color:#e2e8f0; font-size:0.9em;">{sec}</span>
                            <span style="min-width:50px; font-size:0.85em; color:#94a3b8;">%{display_score}</span>
                            <div class="progress-track" style="flex:1;">
                                <div class="progress-fill" style="background:{bar_color}; width:{display_score}%;"></div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        detail = cand_data['Bolum_Detaylari'].get(sec, "")
                        if detail:
                            st.caption(f"↳ {detail}")
            
            with rep_col2:
                st.markdown("#### 💎 Öne Çıkan Kanıtlar")
                if cand_data['Kanitlar']:
                    for kanit in cand_data['Kanitlar']:
                        st.success(f"📌 {kanit}")
                else:
                    st.warning("Belirgin kanıt bulunamadı, ancak genel uyum puanı hesaplandı.")
                
                st.markdown("---")
                st.markdown("#### 🛠️ Teknik Yetkinlik Detayı")
                
                st.write("**✅ Eşleşen Yetkinlikler:**")
                matched_html = " ".join([f'<span class="skill-chip-match">{kw}</span>' for kw in cand_data['Eşleşen_Yetkinlikler']])
                st.markdown(matched_html, unsafe_allow_html=True)
                
                st.markdown("")
                st.write("**❌ Eksik / Geliştirilmeli:**")
                missing_html = " ".join([f'<span class="skill-chip-miss">{kw}</span>' for kw in cand_data['Eksik_Yetkinlikler']])
                st.markdown(missing_html, unsafe_allow_html=True)
            
            with st.expander("📝 Kaynak Metin ve Ham Veri"):
                for res in resumes_processed:
                    if res['filename'] == selected_candidate:
                        st.text_area("İşlenen Ham Metin", res['raw_text'][:2000] + "...", height=200)
        
        # ── FOOTER ──
        st.markdown("""
        <div class="pro-footer">
            <strong>HireSync AI</strong> v2.0 PRO — Yapay Zeka Destekli İnsan Kaynakları Analiz Platformu<br>
            © 2026 Tüm hakları saklıdır. | <a href="#">Gizlilik Sözleşmesi</a> · <a href="#">Kullanım Koşulları</a>
        </div>
        """, unsafe_allow_html=True)

else:
    # ── BOŞ DURUM (İlk Açılış) ──
    st.markdown("""
    <div style="text-align:center; padding:60px 0;">
        <div style="font-size:4em; margin-bottom:16px;">📋</div>
        <div style="color:#94a3b8; font-size:1.2em; font-weight:500;">Henüz bir analiz yapılmadı</div>
        <div style="color:#64748b; font-size:0.9em; margin-top:8px;">
            İş tanımını girin, CV dosyalarını yükleyin ve<br>
            <strong style="color:#818cf8;">"Analizi Başlat"</strong> butonuna tıklayın.
        </div>
    </div>
    """, unsafe_allow_html=True)
