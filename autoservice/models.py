from django.db import models

# Create your models here.

class Automobilio_modelis(models.Model):
    marke = models.CharField('Marke',max_length=100)
    modelis = models.CharField('Modelis', max_length=100)

    def __str__(self):
         return f'{self.marke} {self.modelis}'

    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilio modeliai'

class Automobilis(models.Model):
    valstybinis_nr = models.CharField('Valstybinis Nr.',max_length=100,unique=True)
    automobilio_modelis = models.ForeignKey(Automobilio_modelis, on_delete=models.CASCADE)
    vin_kodas = models.CharField('VIN kodas', max_length=50)
    klientas = models.CharField('Klientas', max_length=200)
    nuotrauka = models.ImageField('Nuotrauka', upload_to='automobiliai', null=True, blank=True)

    def __str__(self):
         return f'{self.valstybinis_nr}  (VIN {self.vin_kodas})   {self.automobilio_modelis}'

    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'

class Busena(models.Model):
    pavadinimas = models.CharField('Būsena', max_length=100)

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = 'Būsena'
        verbose_name_plural = 'Būsenos'

class Uzsakymas(models.Model):
    data = models.CharField('Data',max_length=100)
    automobilio = models.ForeignKey(Automobilis, on_delete=models.CASCADE)
    status = models.ForeignKey(Busena, on_delete=models.DO_NOTHING, verbose_name='Būsena')

    def __str__(self):
         return f'{self.data} (Automobilio numeris {self.automobilio.valstybinis_nr})'

    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'

class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas',max_length=500)
    kaina = models.IntegerField('Kaina')

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'

class Uzsakymo_eilute(models.Model):
    paslauga = models.ForeignKey(Paslauga, on_delete=models.CASCADE)
    uzsakymas = models.ForeignKey(Uzsakymas, on_delete=models.CASCADE )
    kiekis = models.CharField('Kiekis',max_length=100)

    def __str__(self):
        return f'Uzsakymo id ({self.uzsakymas})'

    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymų eilutės'










