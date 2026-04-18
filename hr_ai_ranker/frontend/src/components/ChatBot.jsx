import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Bot, User, Filter, RotateCcw } from 'lucide-react';

const ChatBot = ({ results, jobDescription, onFilter }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { role: 'bot', content: 'Merhaba! Ben HR-Flow Akıllı Asistanı. Adaylar hakkında size nasıl yardımcı olabilirim? Örneğin: "Deneyimi olanları listele" diyebilirsiniz.' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.set_attribute?.({ behavior: "smooth" }); // Legacy fix
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage,
          results: results,
          job_description: jobDescription
        })
      });

      const data = await response.json();
      
      setMessages(prev => [...prev, { role: 'bot', content: data.reply }]);

      if (data.filtered_candidates) {
        onFilter(data.filtered_candidates);
      }
    } catch (error) {
      setMessages(prev => [...prev, { role: 'bot', content: 'Üzgünüm, bir bağlantı hatası oluştu.' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed bottom-8 right-8 z-[200] font-sans">
      {/* Chat Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={`w-16 h-16 rounded-full flex items-center justify-center shadow-2xl transition-all duration-500 scale-hover ${isOpen ? 'bg-rose-500 rotate-90' : 'bg-navy-600 dark:bg-navy-500 hover:scale-110 shadow-navy-500/20'}`}
      >
        {isOpen ? <X className="text-white" size={28} /> : <MessageSquare className="text-white" size={28} />}
      </button>

      {/* Chat Window */}
      {isOpen && (
        <div className="absolute bottom-20 right-0 w-[400px] h-[600px] bg-slate-50 dark:bg-zinc-950 backdrop-blur-2xl border border-zinc-200 dark:border-white/10 rounded-[32px] shadow-2xl flex flex-col overflow-hidden animate-in slide-in-from-bottom-10 duration-500">
          
          {/* Header */}
          <div className="p-6 bg-gradient-to-r from-navy-700 to-navy-600 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-white/20 flex items-center justify-center">
                <Bot className="text-white" size={24} />
              </div>
              <div>
                <h4 className="text-white font-black text-sm uppercase tracking-widest leading-none mb-1">HR-Flow AI</h4>
                <div className="flex items-center gap-1.5">
                  <div className="w-1.5 h-1.5 rounded-full bg-teal-300 animate-pulse" />
                  <span className="text-[10px] text-white/70 font-bold uppercase tracking-tighter">Sistem Aktif</span>
                </div>
              </div>
            </div>
            <button 
              onClick={() => onFilter(null)}
              className="p-2 bg-white/10 hover:bg-white/20 rounded-lg text-white/70 transition-all"
              title="Filtreleri Sıfırla"
            >
              <RotateCcw size={16} />
            </button>
          </div>

          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-6 space-y-6 custom-scrollbar">
            {messages.map((msg, idx) => (
              <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`flex gap-3 max-w-[85%] ${msg.role === 'user' ? 'flex-row-reverse' : ''}`}>
                  <div className={`w-8 h-8 rounded-lg flex-shrink-0 flex items-center justify-center ${msg.role === 'user' ? 'bg-zinc-200 dark:bg-zinc-800' : 'bg-navy-600 dark:bg-navy-500'}`}>
                    {msg.role === 'user' ? <User size={16} className="text-zinc-600 dark:text-zinc-400" /> : <Bot size={16} className="text-white" />}
                  </div>
                  <div className={`p-4 rounded-2xl text-[11px] font-medium leading-relaxed ${msg.role === 'user' ? 'bg-navy-600 text-zinc-50 rounded-tr-none' : 'bg-zinc-100/50 dark:bg-white/[0.03] text-zinc-900 dark:text-zinc-200 rounded-tl-none border border-zinc-200 dark:border-white/5'}`}>
                    {msg.content}
                  </div>
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="flex justify-start">
                <div className="flex gap-3 items-center bg-zinc-50 dark:bg-zinc-900/40 p-4 rounded-2xl rounded-tl-none border border-zinc-200 dark:border-white/5">
                  <div className="flex gap-1">
                    <div className="w-1.5 h-1.5 bg-navy-500 rounded-full animate-bounce" />
                    <div className="w-1.5 h-1.5 bg-navy-500 rounded-full animate-bounce [animation-delay:0.2s]" />
                    <div className="w-1.5 h-1.5 bg-navy-500 rounded-full animate-bounce [animation-delay:0.4s]" />
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-6 bg-zinc-50 dark:bg-zinc-900/40 border-t border-zinc-200 dark:border-white/5">
            <div className="flex gap-2 relative">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                placeholder="Mesajınızı yazın..."
                className="w-full bg-slate-50 dark:bg-zinc-950/50 border border-zinc-200 dark:border-white/10 rounded-2xl py-4 pl-6 pr-14 text-xs font-medium text-zinc-900 dark:text-zinc-100 placeholder:text-zinc-400 dark:placeholder:text-zinc-600 focus:outline-none focus:border-navy-500/50 transition-all"
              />
              <button
                onClick={handleSend}
                disabled={isLoading}
                className="absolute right-2 top-2 w-10 h-10 bg-navy-600 hover:bg-navy-500 text-white rounded-xl flex items-center justify-center transition-all disabled:opacity-50"
              >
                <Send size={18} />
              </button>
            </div>
            <p className="text-center text-[8px] text-slate-500 font-bold uppercase tracking-[0.2em] mt-4">AI can make mistakes. Please verify important info.</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatBot;
