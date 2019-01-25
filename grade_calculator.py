scala = 110 / 30

class grade_calculator(object):

    def __init__(self):
        self.cfu_totali = 0
        self.mesi_totali = 0

        #esami
        self.media_esami = 0
        self.cfu_esami = 0

        #tesi
        self.voto_tesi = 0
        self.n_lodi = 0

        self.voto_finale = 0


    def compute_grade(self):
        #voto in 110
        try:
            v_110 = round(((self.media_esami * self.cfu_esami) + (self.voto_tesi * (self.cfu_totali - self.cfu_esami))) / self.cfu_totali * scala)

            delta_1 = 0 if v_110 <= 90 else 4 if v_110 > 106 else (v_110 - 90) / 4 

            delta_2 = 1.5 if self.mesi_totali < 21 else 1

            self.voto_finale = v_110 + delta_1 + delta_2
            if self.n_lodi >= 2 and self.voto_finale >= 110:
                self.voto_finale = '110 e lode'
        except:
            print('Nessun parametro inserito')

    def get_voto_finale(self):
        return self.voto_finale

    def set_cfu_totali(self, cfu_totali):
        self.cfu_totali = cfu_totali

    def set_mesi_totali(self, mesi_totali):
        self.mesi_totali = mesi_totali

    def set_media_esami(self, media_esami):
        self.media_esami = media_esami

    def set_cfu_esami(self, cfu_esami):
        self.cfu_esami = cfu_esami

    def set_voto_tesi(self, voto_tesi):
        self.voto_tesi = voto_tesi

    def set_lodi(self, lodi):
        self.n_lodi = lodi



