import React, { useState } from 'react';
import { Upload, FileText, X, AlertCircle } from 'lucide-react';

const UploadZone = ({ onAnalyze, loading }) => {
  const [jd, setJd] = useState('');
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    const selectedFiles = Array.from(e.target.files);
    setFiles(prev => [...prev, ...selectedFiles]);
  };

  const removeFile = (index) => {
    setFiles(files.filter((_, i) => i !== index));
  };

  const handleSubmit = () => {
    if (!jd || jd.length < 10) return alert('Lütfen geçerli bir iş tanımı girin.');
    if (files.length === 0) return alert('Lütfen en az bir CV yükleyin.');
    onAnalyze(jd, files);
  };

  return (
    <div className="flex flex-col lg:flex-row gap-10 mb-16 animate-in fade-in slide-in-from-bottom-5 duration-700 delay-150">
      {/* İş Tanımı Alanı */}
      <div className="flex-[1.2] glass-morphism p-8 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-white/10 shadow-zinc-200/50 group transition-all duration-500 hover:shadow-navy-500/5">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3 text-navy-600 dark:text-navy-400">
            <div className="p-2 bg-navy-500/10 rounded-lg">
              <FileText size={20} />
            </div>
            <h2 className="text-lg font-black uppercase tracking-widest font-display text-zinc-900 dark:text-white">İş Tanımı (JD)</h2>
          </div>
          <div className="text-[10px] font-bold text-zinc-500 dark:text-zinc-400 uppercase tracking-widest">Gerekli Alan</div>
        </div>
        <textarea
          value={jd}
          onChange={(e) => setJd(e.target.value)}
          placeholder="Pozisyon beklentilerini, teknik yetkinlikleri ve sorumlulukları buraya detaylıca yapıştırın..."
          className="w-full h-64 bg-white dark:bg-black/40 border border-zinc-200 dark:border-white/10 rounded-2xl p-6 text-zinc-900 dark:text-zinc-100 placeholder-zinc-400 dark:placeholder-zinc-600 focus:outline-none focus:border-navy-500/40 transition-all duration-300 resize-none text-sm leading-relaxed custom-scrollbar shadow-sm"
        />
        <div className="mt-4 flex items-center gap-2 text-[10px] text-zinc-500 dark:text-zinc-500 font-bold uppercase tracking-widest">
           <AlertCircle size={12} className="text-navy-600/50" />
           Analiz kalitesi için en az 50 karakter girmeniz önerilir.
        </div>
      </div>

      {/* Dosya Yükleme Alanı */}
      <div className="flex-1 glass-morphism p-8 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-white/10 shadow-zinc-200/50">
        <div className="flex items-center gap-3 mb-6 text-navy-600 dark:text-navy-400">
          <div className="p-2 bg-navy-500/10 rounded-lg">
            <Upload size={20} />
          </div>
          <h2 className="text-lg font-black uppercase tracking-widest font-display text-zinc-900 dark:text-white">CV Havuzu</h2>
        </div>
        
        <div className="border-2 border-dashed border-zinc-200 dark:border-zinc-800 rounded-3xl p-10 flex flex-col items-center justify-center bg-zinc-50/50 dark:bg-black/20 hover:bg-white dark:hover:bg-black/40 hover:border-navy-500/30 transition-all duration-500 cursor-pointer relative group shadow-inner">
          <input 
            type="file" 
            multiple 
            accept=".pdf,.docx" 
            onChange={handleFileChange}
            className="absolute inset-0 opacity-0 cursor-pointer z-10"
          />
          <div className="w-16 h-16 bg-white dark:bg-zinc-900 rounded-full flex items-center justify-center mb-4 group-hover:scale-110 group-hover:shadow-lg transition-all duration-500">
            <Upload className="text-zinc-400 dark:text-zinc-500 group-hover:text-navy-600 dark:group-hover:text-navy-400" size={32} />
          </div>
          <p className="text-sm text-zinc-600 dark:text-zinc-300 font-bold mb-1">Dosyaları Sürükleyin</p>
          <p className="text-[10px] text-zinc-400 dark:text-zinc-500 font-bold uppercase tracking-tighter">MAX 10MB | PDF & DOCX</p>
        </div>

        {files.length > 0 && (
          <div className="mt-6 space-y-2 max-h-32 overflow-y-auto pr-2 custom-scrollbar">
            {files.map((file, idx) => (
              <div key={idx} className="flex items-center justify-between py-3 px-4 bg-white dark:bg-black/40 border border-zinc-200 dark:border-white/5 rounded-xl animate-in slide-in-from-left-2 duration-300 shadow-sm">
                <div className="flex items-center gap-3 truncate">
                  <div className="w-2 h-2 rounded-full bg-navy-600 dark:bg-navy-500" />
                  <span className="text-xs text-zinc-700 dark:text-zinc-300 font-medium truncate">{file.name}</span>
                </div>
                <button onClick={() => removeFile(idx)} className="text-zinc-400 hover:text-red-500 hover:bg-red-500/10 p-1.5 rounded-lg transition-all">
                  <X size={14} />
                </button>
              </div>
            ))}
          </div>
        )}

        <button
          onClick={handleSubmit}
          disabled={loading}
          className={`w-full mt-8 py-4 px-6 rounded-2xl font-black uppercase tracking-[0.2em] text-xs transition-all duration-500 flex items-center justify-center gap-3 overflow-hidden relative shadow-2xl ${
            loading 
            ? 'bg-zinc-100 dark:bg-zinc-800 text-zinc-400 dark:text-zinc-500 cursor-not-allowed border border-zinc-200 dark:border-white/5' 
            : 'bg-gradient-to-r from-navy-900 to-navy-700 hover:from-navy-800 hover:to-navy-600 text-white shadow-navy-500/20 hover:-translate-y-1 active:scale-95'
          }`}
        >
          {loading ? (
            <>
              <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
              SİSTEM ÇALIŞIYOR
            </>
          ) : (
            <>
              🚀 ANALİZİ BAŞLAT
            </>
          )}
        </button>
      </div>
    </div>
  );
};

export default UploadZone;
