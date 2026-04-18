// HireSync AI - Frontend İşleyişi

document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('cv-upload');
    const analyzeBtn = document.getElementById('analyze-btn');
    const loader = document.getElementById('loader');

    // Chart.js Yapılandırması
    const ctx = document.getElementById('scoreChart').getContext('2d');
    let scoreChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [0, 100],
                backgroundColor: ['#dc2626', 'rgba(255, 255, 255, 0.05)'],
                borderWidth: 0,
                circumference: 180,
                rotation: -90, // Üst yarım ay formunu sağlar
            }]
        },
        options: {
            cutout: '80%',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } }
        }
    });

    // Dosya Yükleme Etkileşimi
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.style.borderColor = '#6366f1';
        dropZone.style.background = 'rgba(99, 102, 241, 0.1)';
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.style.borderColor = 'rgba(255, 255, 255, 0.1)';
        dropZone.style.background = 'transparent';
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        const files = e.dataTransfer.files;
        if (files.length) handleFileSelect(files[0]);
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) handleFileSelect(e.target.files[0]);
    });

    function handleFileSelect(file) {
        dropZone.querySelector('p').innerHTML = `Seçilen dosya: <span>${file.name}</span>`;
        dropZone.style.borderColor = '#10b981';
    }

    // Analiz Butonu Simülasyonu (Backend henüz hazır değil)
    analyzeBtn.addEventListener('click', async () => {
        const jd = document.getElementById('job-description').value;
        if (!jd) {
            alert('Lütfen önce iş ilanı detaylarını girin.');
            return;
        }

        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = 'Analiz ediliyor...';

        // Simülasyon: Sahte bir analiz süreci
        setTimeout(() => {
            updateResults(85); // Örnek skor
            analyzeBtn.disabled = false;
            analyzeBtn.innerHTML = 'Analizi Tekrarla';
        }, 2000);
    });

    function updateResults(score) {
        // Grafiği güncelle
        scoreChart.data.datasets[0].data = [score, 100 - score];
        scoreChart.update();

        // Skor metnini güncelle
        const scoreVal = document.getElementById('score-value');
        let current = 0;
        const interval = setInterval(() => {
            if (current >= score) clearInterval(interval);
            scoreVal.innerText = current;
            current++;
        }, 20);

        // Status badge güncelle
        const badge = document.getElementById('match-status');
        badge.innerText = 'Yüksek Uyumluluk';
        badge.style.background = 'rgba(16, 185, 129, 0.2)';
        badge.style.color = '#10b981';
    }
});
