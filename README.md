# rpatest

 1. python3 kurulumu yapılmalı bendeki version 3.6.9

        python3 --version
        
        Python 3.6.9

 2. Pip kurulmalı (ben projeye ekledim, proje dizininde aşağıdaki komut çalıştırabiliriz.)
 		
		python3 get-pip.py

 3. Pip aracılığı ile proje gereksinimleri kurulmalı (pip3 yok derse pip olarak da denenebilir)

	    pip3 install -r requirements.txt

 4. ChromeDriver path'e eklenmeli bunun için;

		pip3 show chromedriver-binary

    komutu çalıştırılınca gelen yerde chrome_driver_binary altındaki chromedriver path de olmalı ( her yerden chromedriver yazıldığında çalışabilmeli)
    
    ### Windows için
    
        Environment System Variables da Path'e bu adres te eklenmeli 
        
            c:\Users\is97459\AppData\Local\Programs\Python\Python36\Lib\site-packages\chromedriver_binary\
            
        bende bu şekilde ekli
        
    ### Ubuntu için 
    
        profile dosyasına eklenebilir (bende ~/.profile dosyası)
        
            PATH="$HOME/.local/lib/python3.6/site-packages/chromedriver_binary:$PATH"
            
        .profile en sonuna bu şekilde ekli. Sonrasında sessionı restart etmek gerekebilir.
        

 5. Uygulama çalıştırma (program dizinindeyken)
    
		python3 web_scrapper.py
    
