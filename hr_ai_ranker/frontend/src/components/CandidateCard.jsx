import React from 'react';
import { Github, Linkedin, Mail, Phone, ExternalLink, Award } from 'lucide-react';

const CandidateCard = ({ candidate, rank, onOpenDetails }) => {
  const { Aday, Skor, Etiket, Iletisim, ["Eşleşen_Yetkinlikler"]: eslesenYetkinlikler, ["Ozet"]: ozet } = candidate;
  const name = Aday.replace('.pdf', '').replace('.docx', '').replace('_', ' ').replace('-', ' ');

  const scoreColor = Skor >= 70 ? 'text-emerald-400' : Skor >= 40 ? 'text-amber-400' : 'text-red-400';
  const scoreBg = Skor >= 70 ? 'bg-emerald-500/10 border-emerald-500/20' : Skor >= 40 ? 'bg-amber-500/10 border-amber-500/20' : 'bg-red-500/10 border-red-500/20';

  return (
    <div className="glass-morphism p-6 mb-4 group transition-all duration-300 relative overflow-hidden dark:bg-zinc-950/40 border border-zinc-200 dark:border-white/5 hover:border-navy-500/30 dark:hover:border-indigo-500/30">
      
      <div className="flex flex-col lg:flex-row justify-between items-start gap-8">
        
        {/* Sol Taraf: İsim ve Bilgiler */}
        <div className="flex-1 space-y-6">
          <div className="flex flex-wrap items-center gap-4">
            <div className="w-12 h-12 rounded-xl bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-white/10 flex items-center justify-center text-xl font-bold text-zinc-400 dark:text-zinc-500 group-hover:text-navy-600 dark:group-hover:text-indigo-400 group-hover:border-navy-500/30 transition-all duration-300 font-display shadow-sm">
              {rank < 10 ? `0${rank}` : rank}
            </div>
            <div>
              <h3 className="text-2xl font-bold text-zinc-900 dark:text-zinc-100 group-hover:text-navy-600 dark:group-hover:text-indigo-400 transition-colors duration-300 font-display uppercase tracking-tight">
                {name}
              </h3>
              <div className="flex items-center gap-2 mt-1">
                <span className={`px-3 py-0.5 rounded-full text-[9px] font-bold uppercase tracking-[0.1em] border ${scoreBg} ${scoreColor}`}>
                  {Etiket}
                </span>
                <div className="h-1 w-1 rounded-full bg-zinc-400" />
                <span className="text-[9px] font-bold text-navy-600 dark:text-indigo-500/80 uppercase tracking-widest leading-none">Aday Analizi</span>
              </div>
            </div>
          </div>

          <div className="flex flex-wrap gap-6 text-xs font-bold text-zinc-500 dark:text-zinc-400">
            {Iletisim.emails?.[0] && (
              <a href={`mailto:${Iletisim.emails[0]}`} className="flex items-center gap-2 hover:text-navy-600 dark:hover:text-white transition-colors group/link">
                <div className="p-1.5 bg-zinc-100 dark:bg-white/5 rounded-lg group-hover/link:bg-navy-500/10 dark:group-hover/link:bg-indigo-500/10 transition-colors"><Mail size={14} /></div> {Iletisim.emails[0]}
              </a>
            )}
            {Iletisim.linkedin?.[0] && (
              <a href={Iletisim.linkedin[0]} target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 hover:text-navy-600 dark:hover:text-white transition-colors group/link">
                <div className="p-1.5 bg-zinc-100 dark:bg-white/5 rounded-lg group-hover/link:bg-navy-500/10 dark:group-hover/link:bg-indigo-500/10 transition-colors"><Linkedin size={14} /></div> LinkedIn
              </a>
            )}
            {Iletisim.github?.[0] && (
              <a href={Iletisim.github[0]} target="_blank" rel="noopener noreferrer" className="flex items-center gap-2 hover:text-navy-600 dark:hover:text-white transition-colors group/link">
                <div className="p-1.5 bg-zinc-100 dark:bg-white/5 rounded-lg group-hover/link:bg-navy-500/10 dark:group-hover/link:bg-indigo-500/10 transition-colors"><Github size={14} /></div> Github
              </a>
            )}
          </div>

          {/* Yetkinlikler */}
          <div>
            <div className="flex flex-wrap gap-1.5">
              {eslesenYetkinlikler && eslesenYetkinlikler.length > 0 ? (
                eslesenYetkinlikler.slice(0, 8).map((skill, idx) => (
                  <span key={idx} className="px-3 py-1 bg-zinc-100 dark:bg-white/5 text-zinc-800 dark:text-zinc-300 text-[9px] font-bold rounded-lg border border-zinc-200 dark:border-white/5 transition-all lowercase">
                    {skill}
                  </span>
                ))
              ) : (
                <span className="text-[10px] text-zinc-500 italic">Genel Yetkinlikler</span>
              )}
              {eslesenYetkinlikler && eslesenYetkinlikler.length > 8 && (
                <span className="px-3 py-1 bg-navy-500/10 dark:bg-indigo-500/10 text-navy-600 dark:text-indigo-400 text-[10px] font-black rounded-lg border border-navy-500/20 dark:border-indigo-500/20">
                  +{eslesenYetkinlikler.length - 8}
                </span>
              )}
            </div>
          </div>

          {/* Neden Bu Aday? */}
          <div className="p-5 bg-navy-500/5 dark:bg-indigo-500/[0.03] border border-navy-500/10 dark:border-indigo-500/10 rounded-xl group-hover:bg-navy-500/10 dark:group-hover:bg-indigo-500/[0.06] transition-all">
            <div className="flex items-center gap-2 mb-2">
              <Award className="text-amber-500/80" size={14} />
              <p className="text-[9px] font-bold text-zinc-500 dark:text-zinc-400 uppercase tracking-widest">AI Özet Raporu</p>
            </div>
            <p className="text-zinc-700 dark:text-zinc-300 text-sm leading-relaxed font-medium">
              "{ozet || "Adayın teknik yetkinlikleri ve projeleri iş tanımıyla uyumluluk göstermektedir."}"
            </p>
          </div>
        </div>

        {/* Sağ Taraf: Skor ve Buton */}
        <div className="flex lg:flex-col items-center lg:items-end justify-between lg:justify-start gap-8 min-w-[160px] w-full lg:w-auto pt-6 lg:pt-0 border-t lg:border-t-0 border-zinc-200 dark:border-white/5">
          <div className="relative group/score">
            <div className={`w-24 h-24 rounded-2xl flex flex-col items-center justify-center border shadow-xl transition-all duration-500 ${scoreBg} ${scoreColor} border-zinc-200 dark:border-white/10 bg-zinc-50 dark:bg-zinc-900/60`}>
              <span className="text-3xl font-black font-display tracking-tighter text-zinc-900 dark:text-zinc-100">%{Math.round(Skor)}</span>
              <span className="text-[9px] uppercase font-black tracking-widest opacity-70">Uyum</span>
            </div>
            {/* Pulsing ring for high scores */}
            {Skor >= 80 && (
              <div className="absolute inset-0 rounded-2xl border-2 border-emerald-500/20 animate-ping -z-10" />
            )}
          </div>
          
          <button 
            onClick={() => candidate && onOpenDetails(candidate)}
            className="flex-1 lg:flex-none w-full flex items-center justify-center gap-2 px-5 py-3 bg-zinc-50 dark:bg-zinc-950 hover:bg-zinc-100 dark:hover:bg-zinc-900 border border-zinc-200 dark:border-white/10 hover:border-navy-500/40 dark:hover:border-indigo-500/40 text-[10px] font-black rounded-xl transition-all duration-300 uppercase tracking-widest group/btn relative overflow-hidden active:scale-95 text-zinc-800 dark:text-zinc-100"
          >
            <span className="relative z-10 group-hover:text-navy-600 dark:group-hover:text-indigo-400 transition-colors">Analiz Raporu</span>
            <ExternalLink size={12} className="relative z-10 text-zinc-500 dark:text-zinc-500 group-hover:text-navy-600 dark:group-hover:text-indigo-400 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-all" />
          </button>
        </div>
      </div>
    </div>
  );
};

export default CandidateCard;
