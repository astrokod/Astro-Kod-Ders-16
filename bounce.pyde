def setup():
    # Setup fonksiyonu
    
    # Global olarak ball adlı değişken oluştur
    global ball
    
    # Pencere boyutunu 500x500 yap
    size(500, 500)
    
    # ball değişkenine Body objesi ata.
    # ball, ekranın yatayda ortasında, diyekde 50 piksel aşağıda ve 20 piksel yarıçapa sahiptir.
    ball = Body(PVector(width/2, 50), 20)
    
def draw():
    # Draw fonksiyonu
    
    # Arka alanı siyah yap
    background(0)
    #Topu göster
    ball.show()
    #Topu hareket ettir
    ball.move()
    

class Body:
    def __init__(self, pos, r):
        """Bu, ivmeli hareket yapabilen bir objedir"""
        
        # Pozisyon bilgisini al
        self.pos = pos
        # Yarıçap bilgisini al
        self.r = r
        # Hız değişkenini sıfır olarak oluştur
        self.vel = PVector(0, 0)
        # İvme değişkenini yatay eksende 0.9807 olarak oluştur
        self.g = PVector(0, 0.9807)
        
    def move(self):
        """Bu metod hareketi sağlar"""
        
        # İvme değerini hız değerine ekle
        self.vel.add(self.g)
        # Hız değerini pozisyon değerine ekle
        self.pos.add(self.vel)
        # Sekmek gerekiyorsa sek.
        self.bounce()
        
    def bounce(self):
        """Sekme metodu"""
        
        # Eğer top ekranın alt tarafından çıkmak üzere ise.
        if self.pos.y >= width - self.r:
            # Hızın yönünü değiştir
            self.vel.y *= -1
            # Pozisyonu ekranın tam altına taşı
            self.pos.y = width - self.r*2
        
    def show(self):
        """Gösterme metodu"""
        
        #self.pos'da self.r*2 çapında bir daire çiz
        circle(self.pos.x, self.pos.y, self.r * 2)
