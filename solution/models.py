from django.db import models
import random

# Create your models here.


class GuessNumbers(models.Model):
    name = models.CharField(max_length = 24)

    lottos = models.CharField(max_length = 255, default = '[1,2,3,4,5,6]')

    text = models.CharField(max_length = 255)

    num_lotto = models.IntegerField(default = 5)

    update_date = models.DateTimeField()

    def generate(self):
        self.text = "solution hello"
        self.lottos = ""
        origin = list(range(1,46))
        for _ in ramge(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess)+'\n'
        self.update_date = timezone.now()
        self.save()
