<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hareket Sensörü Uzaktan Kontrol</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        h1, h2 {
            color: #0056b3;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: "Courier New", Courier, monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        .note {
            background: #ffffcc;
            padding: 10px;
            border-left: 6px solid #ffeb3b;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Hareket Sensörü Uzaktan Kontrol</h1>
    <p>Bu proje, bir IP kamera yayını ile hareket algılama sistemini kullanarak bilgisayarınızda uzaktan kontrol işlemlerini simüle eder. Uygulama, belirli bir bölgede hareketi izler ve hareket algılandığında işlemleri tetikler.</p>

    <h2>Özellikler</h2>
    <ul>
        <li>IP kamerasından gerçek zamanlı hareket algılama.</li>
        <li>Trackbar kullanarak ilgi alanını (ROI) yapılandırma.</li>
        <li>Ayarlanabilir hassasiyet ve hareket duraklatma süresi.</li>
        <li>Hareket algılandığında sağ ok tuşuna basmayı simüle eder.</li>
        <li>Çalışma sırasında hareket algılamayı açma/kapama.</li>
    </ul>

    <h2>Bağımlılıklar</h2>
    <p>Aşağıdaki Python kütüphanelerinin yüklü olduğundan emin olun:</p>
    <pre>
        pip install opencv-python numpy pyautogui
    </pre>

    <h2>Kurulum Talimatları</h2>
    <ol>
        <li>Script içindeki <code>stream_url</code> değerini IP kameranızın URL'si ile değiştirin.</li>
        <li>Script'i Python 3 ile çalıştırın:</li>
        <pre>python motion_sensor.py</pre>
        <li>"IP Kamera Yayını" penceresindeki trackbar'ları kullanarak algılama alanını ve hassasiyeti ayarlayın:</li>
        <ul>
            <li><strong>X Merkezi:</strong> Algılama çemberinin merkezinin x koordinatını ayarlayın.</li>
            <li><strong>Y Merkezi:</strong> Algılama çemberinin merkezinin y koordinatını ayarlayın.</li>
            <li><strong>Yarıçap:</strong> Algılama alanının yarıçapını değiştirin.</li>
            <li><strong>Hassasiyet:</strong> Hareket hassasiyetini değiştirin (daha yüksek değerler = daha az hassasiyet).</li>
        </ul>
        <li>Çalışma sırasında <code>d</code> tuşuna basarak hareket algılamayı açıp kapatın.</li>
        <li>Uygulamayı kapatmak için <code>q</code> tuşuna basın.</li>
    </ol>

    <h2>Nasıl Çalışır</h2>
    <ol>
        <li>Uygulama, IP kamerasından video karelerini yakalar.</li>
        <li>Trackbar ayarlarına göre çerçeveye dairesel bir ilgi alanı (ROI) uygulanır.</li>
        <li>Hareket, ROI içindeki ardışık kareler arasındaki piksel farkları karşılaştırılarak algılanır.</li>
        <li>Hareket algılanırsa ve duraklatma süresi geçmişse, simüle edilmiş bir tuş vuruşu tetiklenir.</li>
    </ol>

    <h2>Tuş Konfigürasyonu</h2>
    <p>Uygulama aşağıdaki tuşlarla kontrol edilir:</p>
    <ul>
        <li><strong>d:</strong> Hareket algılamayı aç/kapat.</li>
        <li><strong>q:</strong> Uygulamayı kapat.</li>
    </ul>

    <h2>Notlar</h2>
    <div class="note">
        <strong>Önemli:</strong> IP kamera yayınızın erişilebilir olduğundan emin olun ve <code>stream_url</code> değişkenini doğru URL ile değiştirin.
    </div>

    <h2>Potansiyel İyileştirmeler</h2>
    <ul>
        <li>Daha sofistike algoritmalarla (örneğin, arka plan çıkarma) hareket algılama doğruluğunu artırın.</li>
        <li>Birden fazla ilgi alanı (ROI) desteği ekleyin.</li>
        <li>Daha iyi kontrol ve görselleştirme için bir grafik kullanıcı arayüzü (GUI) uygulayın.</li>
    </ul>

    <h2>Yasal Uyarı</h2>
    <p>Bu script'i sorumlu bir şekilde kullanın ve kamera yayınlarına erişirken gizlilik ve güvenlik kurallarına uyduğunuzdan emin olun.</p>
</body>
</html>
