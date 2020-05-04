# rpatest

 1. python 3 kurulumu yapılmalı bendeki version 3.6.9 (daha yenisi de sorun olmaz)

        python --version
        
        Python 3.6.9

 2. Pip kurulmalı (ben projeye ekledim, proje dizininde aşağıdaki komut çalıştırabiliriz.)
 		
		python get-pip.py

 3. Pip aracılığı ile proje gereksinimleri kurulmalı (chrome driverı vs indirecek)

	    pip install -r requirements.txt

 4. ChromeDriver path'e eklenmeli bunun için;

		pip show chromedriver-binary

    komutu çalıştırılınca gelen yerde chrome_driver_binary altındaki chromedriver path de olmalı ( her yerden chromedriver yazıldığında çalışabilmeli)
    
    ### Windows için
    
        Environment System Variables da Path'e bu adres te eklenmeli 
        
            c:\Users\user\AppData\Local\Programs\Python\Python36\Lib\site-packages\chromedriver_binary\
            
        bende bu şekilde ekli
        
    ### Ubuntu için 
    
        profile dosyasına eklenebilir (bende ~/.profile dosyası)
        
            PATH="$HOME/.local/lib/python3.6/site-packages/chromedriver_binary:$PATH"
            
        .profile en sonuna bu şekilde ekli. Sonrasında sessionı restart etmek gerekebilir.
        

 5. Uygulama çalıştırma (program dizinindeyken)
    
		python web_scrapper.py
    
