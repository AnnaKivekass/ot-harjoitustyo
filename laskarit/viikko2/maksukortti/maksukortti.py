class Maksukortti:
    def __init__(self, saldo):
        self.saldo = saldo

    def syo_edullisesti(self):
        if self.saldo >= 240:
            self.saldo -= 240

    def syo_maukkaasti(self):
        if self.saldo >= 400:
            self.saldo -= 400

    def lataa_rahaa(self, maara):
        if maara > 0:
            self.saldo += maara
            if self.saldo > 15000:
                self.saldo = 15000

    def ota_rahaa(self, maara):
        if maara <= self.saldo:
            self.saldo -= maara
            return True
        return False

    def saldo_euroina(self):
        return self.saldo / 100

    def __str__(self):
        return f"Kortilla on rahaa {self.saldo / 100:.2f} euroa"
    
