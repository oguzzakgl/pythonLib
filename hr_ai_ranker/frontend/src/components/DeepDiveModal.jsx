import React from 'react';
import { X, CheckCircle2, AlertTriangle, MessageSquare, Target, User, Mail, Phone, ExternalLink, Linkedin, Github, Sparkles } from 'lucide-react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer } from 'recharts';

const DeepDiveModal = ({ candidate, onClose, darkMode }) => {
  React.useEffect(() => {
    document.body.style.overflow = 'hidden';
    return () => {
      document.body.style.overflow = 'unset';
    };
  }, []);

  if (!candidate) return null;

  const { 
    Aday, Skor, Semantik_Skor, Anahtar_Kelime_Skor, 
    ["Eşleşen_Yetkinlikler"]: eslesenYetkinlikler, 
    Bolum_Skorlari, Kanitlar, ["Ozet"]: ozet, Iletisim,
    ["Mülakat_Soruları"]: mulakatSorulari 
  } = candidate;

  const radarData = [
    { subject: 'Genel', A: Skor || 0, fullMark: 100 },
    { subject: 'Semantik', A: Semantik_Skor || 0, fullMark: 100 },
    { subject: 'Teknik', A: Anahtar_Kelime_Skor || 0, fullMark: 100 },
    { subject: 'Egitim', A: (Bolum_Skorlari && Bolum_Skorlari['Eğitim']) || 0, fullMark: 100 },
    { subject: 'Deneyim', A: (Bolum_Skorlari && Bolum_Skorlari['Deneyim']) || 0, fullMark: 100 },
  ];

  const name = Aday.replace(/\.[^/.]+$/, "").replace(/_/g, ' ').replace(/-/g, ' ');

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 md:p-8 bg-white/95 dark:bg-zinc-950/95 backdrop-blur-md animate-in fade-in duration-300 selection:bg-navy-500/30">
      {/* Reduced background glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-navy-500/5 blur-[120px] -z-10" />
      
      <div className="glass-morphism w-full max-w-6xl max-h-full overflow-y-auto custom-scrollbar relative">
        
        {/* Header - Ultra Modern */}
        <div className="sticky top-0 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-3xl z-10 p-8 border-b border-zinc-200 dark:border-white/5 flex items-center justify-between">
          <div className="flex items-center gap-5">
            <div className="relative group">
              <div className={`w-14 h-14 rounded-xl flex flex-col items-center justify-center border shadow-xl transition-all duration-300 ${Skor >= 70 ? 'bg-emerald-500/10 border-emerald-500/20 text-emerald-400' : 'bg-navy-500/10 border-navy-500/20 text-navy-600 dark:text-navy-400'}`}>
                <span className="text-xl font-bold font-display leading-none">%{Math.round(Skor)}</span>
              </div>
            </div>
            <div>
              <h2 className="text-2xl font-bold dark:text-zinc-100 font-display uppercase tracking-tight leading-none mb-1.5">{name}</h2>
              <div className="flex items-center gap-3">
                <span className="text-[9px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-[0.2em]">Detailed Analysis Report</span>
                <div className="h-2 w-[1px] bg-zinc-200 dark:bg-white/10" />
                <span className="text-[9px] font-bold text-navy-600 dark:text-navy-500 uppercase tracking-widest">HR-Flow Verified</span>
              </div>
            </div>
          </div>
          <button 
            onClick={onClose} 
            className="w-12 h-12 flex items-center justify-center bg-white/5 hover:bg-red-500/10 border border-white/10 hover:border-red-500/30 rounded-2xl text-slate-400 hover:text-red-400 transition-all active:scale-90"
          >
            <X size={24} />
          </button>
        </div>

        <div className="p-8 md:p-12">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-16">
            
            {/* Sol Sütun: Görselleştirme ve Özet */}
            <div className="space-y-10">
              <section className="animate-in slide-in-from-left-10 duration-700">
                <div className="flex items-center justify-between mb-8">
                  <h3 className="text-lg font-bold dark:text-zinc-100 font-display flex items-center gap-3">
                    <div className="p-2 bg-navy-500/10 rounded-lg text-navy-600 dark:text-navy-400/80">
                      <Target size={20} />
                    </div>
                    Yetkinlik Matrisi
                  </h3>
                  <div className="text-[9px] font-bold text-zinc-400 dark:text-zinc-500 uppercase tracking-widest">Polar Mapping</div>
                </div>
                <div className="h-[380px] w-full bg-slate-50/50 dark:bg-zinc-900/40 backdrop-blur-md rounded-[32px] border border-zinc-200 dark:border-white/5 p-8 relative group hover:border-navy-500/30 transition-all duration-700">
                  <ResponsiveContainer width="100%" height="100%">
                    <RadarChart cx="50%" cy="50%" outerRadius="80%" data={radarData}>
                      <PolarGrid stroke={darkMode ? "rgba(255,255,255,0.05)" : "rgba(0,0,0,0.1)"} />
                      <PolarAngleAxis dataKey="subject" tick={{ fill: darkMode ? '#71717a' : '#1e3a8a', fontSize: 10, fontWeight: 700, letterSpacing: '0.1em' }} />
                      <PolarRadiusAxis angle={30} domain={[0, 100]} tick={false} axisLine={false} />
                      <Radar
                        name="Aday"
                        dataKey="A"
                        stroke="#1e3a8a"
                        strokeWidth={2}
                        fill="url(#radarGradient)"
                        fillOpacity={0.6}
                      />
                      <defs>
                        <linearGradient id="radarGradient" x1="0" y1="0" x2="1" y2="1">
                          <stop offset="0%" stopColor="#1e40af" stopOpacity="0.8" />
                          <stop offset="100%" stopColor="#1e3a8a" stopOpacity="0.2" />
                        </linearGradient>
                      </defs>
                    </RadarChart>
                  </ResponsiveContainer>
                </div>
              </section>

              <section className="animate-in slide-in-from-left-10 duration-700 delay-200">
                <div className="p-8 bg-navy-500/5 border border-navy-500/10 rounded-2xl relative overflow-hidden group">
                  <h3 className="text-lg font-bold dark:text-white font-display mb-4 flex items-center gap-3">
                    <MessageSquare className="text-navy-600 dark:text-navy-400" size={18} /> Karar Özeti
                  </h3>
                  <p className="text-zinc-800 dark:text-zinc-300 text-base leading-relaxed font-medium relative z-10">
                    "{ozet}"
                  </p>
                </div>
              </section>
            </div>

            {/* Sağ Sütun: Detaylar */}
            <div className="space-y-12 animate-in slide-in-from-right-10 duration-700">
              {/* Kanıtlar */}
              <section>
                <h3 className="text-lg font-bold text-zinc-900 dark:text-zinc-100 font-display mb-6 flex items-center gap-3">
                  <div className="p-2 bg-teal-500/10 rounded-lg text-teal-600 dark:text-teal-400/80">
                    <CheckCircle2 size={18} />
                  </div>
                  Tespit Edilen Kanıtlar
                </h3>
                <div className="space-y-4">
                  {Kanitlar.length > 0 ? Kanitlar.map((kanit, idx) => (
                    <div key={idx} className="p-4 bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200 dark:border-white/5 rounded-xl text-zinc-700 dark:text-zinc-300 text-sm font-medium flex gap-4 hover:bg-zinc-100 dark:hover:bg-zinc-800 transition-all duration-300">
                      <div className="w-6 h-6 rounded-full bg-teal-500/10 flex items-center justify-center flex-shrink-0">
                        <CheckCircle2 className="text-teal-600 dark:text-teal-500" size={12} />
                      </div>
                      <span className="leading-relaxed">{kanit}</span>
                    </div>
                  )) : (
                    <div className="p-8 text-center bg-white/[0.02] border border-dashed border-white/5 rounded-2xl">
                       <p className="text-slate-600 font-bold uppercase tracking-widest text-[10px]">Veri işlenemedi</p>
                    </div>
                  )}
                </div>
              </section>

              {/* Beceriler Paneli */}
              <section>
                <div className="p-8 bg-emerald-500/5 border border-emerald-500/10 rounded-[32px] group hover:bg-emerald-500/10 transition-all duration-500">
                  <h4 className="text-[10px] font-black text-emerald-400 mb-6 uppercase tracking-[0.2em] flex items-center gap-2">
                    <div className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                    Eşleşen Teknik Yetkinlikler
                  </h4>
                  <div className="flex flex-wrap gap-2">
                    {Array.isArray(eslesenYetkinlikler) && eslesenYetkinlikler.map((s, idx) => (
                      <span key={idx} className="px-4 py-2 bg-navy-500/10 dark:bg-slate-950/60 text-navy-700 dark:text-emerald-300 text-[10px] font-bold rounded-xl border border-navy-500/20 dark:border-emerald-500/10 lowercase">
                        {s}
                      </span>
                    ))}
                  </div>
                </div>
              </section>

              {/* AI Mülakat Soruları - Yeni Bölüm */}
              <section className="animate-in slide-in-from-right-10 duration-700 delay-300">
                <h3 className="text-xl font-black text-zinc-900 dark:text-zinc-100 font-display mb-6 flex items-center gap-3">
                  <div className="p-2 bg-amber-500/10 rounded-lg text-amber-600 dark:text-amber-400/80">
                    <Sparkles size={20} />
                  </div>
                  Önerilen Mülakat Soruları
                </h3>
                <div className="space-y-4">
                  {Array.isArray(mulakatSorulari) && mulakatSorulari.length > 0 ? mulakatSorulari.map((soru, idx) => (
                    <div key={idx} className="p-6 bg-amber-500/5 border border-amber-500/10 rounded-2xl group hover:border-amber-500/30 transition-all duration-300">
                      <div className="flex gap-4">
                        <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-amber-500/10 flex items-center justify-center text-amber-600 dark:text-amber-400/80 font-black text-xs">
                          {idx + 1}
                        </div>
                        <p className="text-zinc-700 dark:text-zinc-300 text-sm font-medium leading-relaxed">
                          {soru}
                        </p>
                      </div>
                    </div>
                  )) : (
                    <div className="p-8 text-center bg-white/[0.02] border border-dashed border-white/5 rounded-2xl">
                       <p className="text-slate-600 font-bold uppercase tracking-widest text-[10px]">Soru üretilemedi</p>
                    </div>
                  )}
                </div>
              </section>

              {/* İletişim Paketi - Glass Card Style */}
              <section className="pt-10 border-t border-zinc-200 dark:border-white/5">
                <div className="flex items-center justify-between mb-8">
                   <h3 className="text-xl font-black text-black dark:text-zinc-100 font-display flex items-center gap-3">
                      <div className="p-2 bg-zinc-500/10 rounded-lg text-zinc-600 dark:text-zinc-400/80">
                        <User size={20} />
                      </div>
                      İletişim Portalı
                   </h3>
                   <div className="px-3 py-1 rounded-full bg-navy-500/10 border border-navy-500/20 text-navy-600 dark:text-navy-400/80 text-[8px] font-black uppercase tracking-widest">
                     Ready to Contact
                   </div>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {/* Email */}
                  <div className="p-5 bg-navy-500/5 rounded-2xl border border-navy-500/10 hover:border-navy-500/30 transition-all group/item">
                    <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-3">Resmi E-Posta</p>
                    <div className="flex items-center justify-between gap-4">
                      <p className="text-xs text-black dark:text-white font-bold truncate">{Iletisim.emails[0] || 'Bulunamadı'}</p>
                      {Iletisim.emails[0] && (
                        <div className="flex items-center gap-3">
                          <button 
                            onClick={() => {
                              navigator.clipboard.writeText(Iletisim.emails[0]);
                              alert('Email kopyalandı!');
                            }}
                            className="p-2 bg-navy-500/10 rounded-xl hover:bg-navy-500/20 hover:text-navy-600 dark:hover:text-navy-400 transition-all"
                            title="Kopyala"
                          >
                            <Target size={14} />
                          </button>
                          <a href={`mailto:${Iletisim.emails[0]}`} className="p-2 bg-navy-500/20 rounded-xl text-navy-600 dark:text-navy-400 hover:scale-110 transition-transform"><ExternalLink size={14} /></a>
                        </div>
                      )}
                    </div>
                  </div>
                  
                  {/* Telefon */}
                  <div className="p-5 bg-emerald-500/5 rounded-2xl border border-emerald-500/10 group/item hover:border-emerald-500/30 transition-all">
                    <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest mb-3 flex items-center gap-1">Mobil Hat</p>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-black dark:text-white font-bold">{Iletisim.phones[0] || 'Bulunamadı'}</p>
                      {Iletisim.phones[0] && (
                        <button 
                          onClick={() => {
                            navigator.clipboard.writeText(Iletisim.phones[0]);
                            alert('Telefon kopyalandı!');
                          }}
                          className="p-2 bg-emerald-500/10 rounded-xl hover:bg-emerald-500/20 hover:text-emerald-600 dark:hover:text-emerald-400 transition-all"
                          title="Kopyala"
                        >
                          <Target size={14} />
                        </button>
                      )}
                    </div>
                  </div>

                  {/* LinkedIn */}
                  <div className="p-5 bg-navy-500/5 rounded-2xl border border-navy-500/10 hover:border-navy-500/30 transition-all group/item">
                    <div className="flex items-center justify-between mb-3">
                      <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Profesyonel Ağ</p>
                      <Linkedin size={14} className="text-navy-500/50" />
                    </div>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-black dark:text-white font-bold truncate">{Iletisim.linkedin[0] ? 'LinkedIn Profili' : 'Bulunamadı'}</p>
                      {Iletisim.linkedin[0] && (
                        <a href={Iletisim.linkedin[0].startsWith('http') ? Iletisim.linkedin[0] : `https://${Iletisim.linkedin[0]}`} target="_blank" rel="noreferrer" className="p-2 bg-navy-500/20 rounded-xl text-navy-600 dark:text-navy-400 hover:scale-110 transition-transform">
                          <ExternalLink size={14} />
                        </a>
                      )}
                    </div>
                  </div>

                  {/* GitHub / Website */}
                  <div className="p-5 bg-emerald-500/5 rounded-2xl border border-emerald-500/10 hover:border-emerald-500/30 transition-all group/item">
                    <div className="flex items-center justify-between mb-3">
                      <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest">Üretim & Portfolyo</p>
                      <Github size={14} className="text-emerald-500/50" />
                    </div>
                    <div className="flex items-center justify-between">
                      <p className="text-xs text-black dark:text-white font-bold truncate">
                        {Iletisim.github[0] ? 'GitHub Profili' : (Iletisim.websites?.[0] || 'Bulunamadı')}
                      </p>
                      {(Iletisim.github[0] || Iletisim.websites?.[0]) && (
                        <a 
                          href={(Iletisim.github[0] || Iletisim.websites[0]).startsWith('http') ? (Iletisim.github[0] || Iletisim.websites[0]) : `https://${Iletisim.github[0] || Iletisim.websites[0]}`} 
                          target="_blank" rel="noreferrer" 
                          className="p-2 bg-emerald-500/20 rounded-xl text-emerald-600 dark:text-emerald-400 hover:scale-110 transition-transform"
                        >
                          <ExternalLink size={14} />
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              </section>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
};

export default DeepDiveModal;
