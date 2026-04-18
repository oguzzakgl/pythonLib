import React, { useState } from 'react';
import axios from 'axios';
import { Sparkles, BarChart3, Users, Mail, Settings, Sun, Moon, User, ExternalLink } from 'lucide-react';
import UploadZone from './components/UploadZone';
import CandidateCard from './components/CandidateCard';
import DeepDiveModal from './components/DeepDiveModal';
import ChatBot from './components/ChatBot';

const API_BASE = 'http://localhost:8000';

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState([]);
  const [jobDescription, setJobDescription] = useState('');
  const [filteredCandidates, setFilteredCandidates] = useState(null);
  const [darkMode, setDarkMode] = useState(true);
  const [selectedCandidate, setSelectedCandidate] = useState(null);
  const [progress, setProgress] = useState('');

  // Tema Senkronizasyonu
  React.useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);


  const handleAnalyze = async (jd, files) => {
    setLoading(true);
    setResults([]);
    setProgress('Hazırlanıyor...');
    
    const formData = new FormData();
    formData.append('job_description', jd);
    files.forEach(file => formData.append('files', file));
    formData.append('semantic_weight', 0.7);

    try {
      setJobDescription(jd);
      setFilteredCandidates(null); // Yeni analizde filtreyi sıfırla
      
      setProgress(`${files.length} dosya işleniyor, lütfen bekleyin...`);
      
      const resp = await axios.post(`${API_BASE}/analyze`, formData, {
        timeout: 150000 // 150 saniye (Büyük analizler için pay bırakıyoruz)
      });
      
      setResults(resp.data.results);
      setProgress('Tamamlandı!');
    } catch (err) {
      console.error("ANALYZER ERROR:", err);
      const errorMsg = err.response?.data?.detail || err.message || "Bilinmeyen bir hata oluştu.";
      alert(`Analiz Hatası: ${errorMsg}`);
      setProgress('Hata oluştu.');
    } finally {
      setLoading(false);
      setTimeout(() => setProgress(''), 3000);
    }
  };

  const handleExport = async () => {
    if (results.length === 0) return;
    
    try {
      setProgress('Excel raporu hazırlanıyor...');
      const response = await axios.post(`${API_BASE}/export`, {
        results: results,
        job_description: jobDescription
      }, {
        responseType: 'blob' // Dosya indirmek için blob tipinde yanıt bekliyoruz
      });

      // Dosyayı tarayıcıda indir
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      const filename = `HR_Flow_Analiz_${new Date().toISOString().slice(0,10)}.xlsx`;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      
      setProgress('Rapor indirildi!');
    } catch (err) {
      console.error("EXPORT ERROR:", err);
      alert("Excel oluşturulurken bir hata oluştu.");
    } finally {
      setTimeout(() => setProgress(''), 2000);
    }
  };

  return (
    <div className={`min-h-screen transition-colors duration-500 font-inter relative overflow-x-hidden ${darkMode ? 'dark bg-zinc-950 text-zinc-100' : 'bg-slate-50 text-zinc-900'}`}>
      <div className="premium-bg" />
      
      {/* Navbar */}
      <nav className="sticky top-0 z-50 bg-navy-900 border-b border-white/10 backdrop-blur-xl">
        <div className="container mx-auto px-6 h-20 flex items-center justify-between header-dark-fix">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shadow-lg shadow-navy-950/20 border border-white/20">
              <Sparkles className="text-white" size={20} />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight text-white font-display leading-none">
                HR-FLOW <span className="text-navy-400">AI</span>
              </h1>
              <p className="text-[9px] font-bold text-navy-300 uppercase tracking-[0.2em] mt-1">Smart Recruitment</p>
            </div>
          </div>
          
          <div className="flex items-center gap-8">
            <div className="flex items-center gap-6 text-xs font-bold text-white/90">
              <a href="#stats" className="hover:text-navy-400 transition-colors uppercase tracking-widest">Kontrol Paneli</a>
              <a href="#results" className="hover:text-navy-400 transition-colors uppercase tracking-widest">Analizler</a>
            </div>
            <div className="h-6 w-[1px] bg-white/10 hidden sm:block" />
            <button 
              onClick={() => setDarkMode(!darkMode)}
              className="w-10 h-10 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center hover:bg-white/10 transition-all duration-300"
            >
              {darkMode ? <Sun size={18} className="text-amber-400" /> : <Moon size={18} className="text-white" />}
            </button>
          </div>
        </div>
      </nav>

      <main className="container mx-auto px-6 py-12 relative">
        {/* Hero Section */}
        <div className="text-center mb-20 animate-in fade-in duration-1000">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-navy-500/10 border border-navy-500/20 text-navy-600 dark:text-navy-400 text-[10px] font-black uppercase tracking-[0.2em] mb-8">
            AI-Powered Recruitment
          </div>
          <h2 className="text-5xl md:text-7xl font-black mb-8 tracking-tighter font-display leading-[1.1]">
            Modern İşe Alım <br />
            <span className="hero-highlight">Yapay Zeka</span> ile Başlar
          </h2>
          <p className="max-w-xl mx-auto text-lg mb-12 font-medium leading-relaxed">
            Adaylarınızı bilimsel veriler ve semantik zeka ile analiz edin. <br />
            En doğru kararı, en kısa sürede verin.
          </p>
          
          {loading && (
            <div className="flex flex-col items-center gap-4 bg-white dark:bg-zinc-900/40 backdrop-blur-xl border border-zinc-200 dark:border-white/5 p-8 rounded-[32px] max-w-sm mx-auto shadow-2xl animate-pulse">
              <div className="relative">
                <Sparkles className="text-navy-600 dark:text-navy-400 animate-spin" size={40} />
              </div>
              <div className="text-center">
                <p className="text-sm font-black text-black dark:text-zinc-100 uppercase tracking-widest mb-1">Analiz Başlatıldı</p>
                <p className="text-[10px] text-zinc-500 dark:text-zinc-400 font-bold">Deep learning modelleri optimize ediliyor...</p>
              </div>
            </div>
          )}
        </div>

        {progress && (
          <div className="flex justify-center mb-6 animate-pulse">
            <div className="px-6 py-2 bg-indigo-500/10 border border-indigo-500/20 rounded-full text-indigo-600 dark:text-indigo-400 text-xs font-black uppercase tracking-[0.2em]">
              ⚙️ {progress}
            </div>
          </div>
        )}

        {!loading && <UploadZone onAnalyze={handleAnalyze} loading={loading} />}

        {results && results.length > 0 && (
          <div className="mt-24 space-y-24 animate-in fade-in duration-1000">
            {/* İstatistikler */}
            <div id="stats" className="grid grid-cols-1 md:grid-cols-3 gap-8 scroll-mt-32">
              <div className="glass-morphism p-8 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-white/10 shadow-zinc-200/50 group hover:-translate-y-2 transition-all duration-500">
                <div className="w-12 h-12 rounded-2xl bg-sky-500/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                  <Users className="text-sky-600 dark:text-sky-400" size={24} />
                </div>
                <p className="text-xs font-black text-zinc-500 dark:text-zinc-400 uppercase tracking-widest mb-2">İncelenen Portföy</p>
                <div className="flex items-baseline gap-2">
                  <span className="text-5xl font-black text-zinc-900 dark:text-white font-display leading-none">{results.length}</span>
                  <span className="text-sm font-bold text-zinc-500 dark:text-zinc-500 uppercase">Aday</span>
                </div>
              </div>
              
              <div className="glass-morphism p-8 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-white/10 shadow-zinc-200/50 group hover:-translate-y-2 transition-all duration-500">
                <div className="w-12 h-12 rounded-2xl bg-teal-500/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                  <BarChart3 className="text-teal-600 dark:text-teal-400" size={24} />
                </div>
                <p className="text-xs font-black text-zinc-500 dark:text-zinc-400 uppercase tracking-widest mb-2">Maksimum Uyumluluk</p>
                <div className="flex items-baseline gap-2">
                  <span className="text-5xl font-black text-zinc-900 dark:text-white font-display leading-none">
                    %{results.length > 0 ? Math.round(Math.max(...results.map(r => r.Skor))) : 0}
                  </span>
                  <span className="text-sm font-bold text-zinc-500 dark:text-zinc-500 uppercase">Peak</span>
                </div>
              </div>

              <div className="glass-morphism p-8 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-white/10 shadow-zinc-200/50 group hover:-translate-y-2 transition-all duration-500">
                <div className="w-12 h-12 rounded-2xl bg-amber-500/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                  <Mail className="text-amber-600 dark:text-amber-400" size={24} />
                </div>
                <p className="text-xs font-black text-zinc-500 dark:text-zinc-400 uppercase tracking-widest mb-2">Ortalama Skor</p>
                <div className="flex items-baseline gap-2">
                  <span className="text-5xl font-black text-zinc-900 dark:text-white font-display leading-none">
                    %{results.length > 0 ? Math.round(results.reduce((a, b) => a + b.Skor, 0) / results.length) : 0}
                  </span>
                  <span className="text-sm font-bold text-zinc-500 dark:text-zinc-500 uppercase">Avg</span>
                </div>
              </div>
            </div>

            {/* Aday Listesi */}
            <section id="results" className="scroll-mt-32">
              <div className="flex flex-col md:flex-row items-start md:items-end justify-between gap-6 mb-12 px-2">
                <div>
                  <h3 className="text-4xl font-black text-zinc-900 dark:text-white font-display flex items-center gap-4">
                    <div className="w-2 h-10 bg-navy-600 rounded-full dark:bg-navy-500/80" />
                    En İyi Eşleşmeler
                  </h3>
                  <p className="text-zinc-700 dark:text-zinc-500 mt-2 font-medium">Pozisyon gerekliliklerine en yakın adaylar yukarıdan aşağıya sıralandı.</p>
                </div>
                <div className="flex items-center gap-4">
                  <button 
                    onClick={handleExport}
                    className="flex items-center gap-3 px-6 py-3 rounded-2xl bg-gradient-to-r from-emerald-500/20 to-emerald-600/20 border border-emerald-500/30 text-emerald-400 text-xs font-black uppercase tracking-widest hover:from-emerald-500/30 hover:to-emerald-600/30 transition-all duration-300 group shadow-lg shadow-emerald-500/5"
                  >
                    <BarChart3 size={18} className="group-hover:rotate-12 transition-transform" />
                    Sonuçları İndir (xlsx)
                  </button>
                  <div className="px-6 py-3 rounded-2xl bg-white/5 border border-white/10 text-[10px] font-black text-slate-400 uppercase tracking-[0.2em]">
                    AI-Powered Sorting Active
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 gap-6">
                {results
                  .filter(c => !filteredCandidates || filteredCandidates.includes(c.Aday))
                  .sort((a, b) => b.Skor - a.Skor)
                  .map((cand, idx) => (
                  <CandidateCard 
                    key={idx} 
                    candidate={cand} 
                    rank={idx + 1} 
                    onOpenDetails={(c) => setSelectedCandidate(c)} 
                  />
                ))}
              </div>
            </section>
          </div>
        )}

        {results && results.length > 0 && (
          <ChatBot 
            results={results} 
            jobDescription={jobDescription} 
            onFilter={(list) => setFilteredCandidates(list)} 
          />
        )}

        {selectedCandidate && (
          <DeepDiveModal 
            candidate={selectedCandidate} 
            darkMode={darkMode}
            onClose={() => setSelectedCandidate(null)} 
          />
        )}
      </main>

      <footer className="mt-24 border-t border-zinc-200 dark:border-white/5 py-20 relative">
        <div className="container mx-auto px-6 flex flex-col items-center text-center">
          <div className="w-10 h-10 bg-sky-600/20 rounded-xl flex items-center justify-center mb-6">
            <Sparkles className="text-sky-600 dark:text-sky-400" size={20} />
          </div>
          <p className="text-zinc-900 dark:text-zinc-500 text-sm font-bold uppercase tracking-[0.3em] mb-4">
            HR-FLOW AI <span className="text-navy-600/50">PLATFORM</span>
          </p>
          <p className="text-zinc-700 dark:text-zinc-600 text-xs font-medium max-w-md leading-relaxed">
            Profesyonel işe alım süreçleri için tasarlandı. <br /> 
            &copy; 2026 HR-Flow Intelligence. Tüm Hakları Saklıdır.
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
