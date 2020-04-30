# rpatest

1.python3 kurulumu yapılmalı bendeki version 3.6.9
        python3 --version
        Python 3.6.9
        
2.Pip kurulmalı (ben projeye ekledim, proje dizininde aşağıdaki komut çalıştılabilir.)
    python3 get-pip.py
    
3.Pip aracılığı ile proje gereksinimleri kurulmalı (pip3 yok derse pip olarak da denenebilir)
    pip3 install -r requirements.txt
    
4.pip3 show chromedriver-binary
    komutu çalıştırılınca gelen yerde chrome_driver_binary altındaki chromedriver path de olmalı
    .windows için
        Environment System Variables da Path'e bu adres te eklenmeli 
        bende 
            c:\Users\is97459\AppData\Local\Programs\Python\Python36\Lib\site-packages\chromedriver_binary\
        bu ekli
    .ubuntu için 
        profile dosyasına eklenebilir (~/.profile dosyası)
            PATH="$HOME/.local/lib/python3.6/site-packages/chromedriver_binary:$PATH"
        satırını ekledim. daha sonra sessionı kapatıp açmak gerekebilir.
        
5.Uygulama çalıştırma
    bu klasördeyken
    python3 web_scrapper.py
