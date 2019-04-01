import random


class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.orginal_value * 1.25
        else:
            self.value = self.orgonal_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print('Coin spent!')

    def flip(self):
        head_options = [True, False]
        choice = random.choice(head_options)
        self.heads = choice


class Pound(Coin):
    def __init__(self):
        data = {
            'original_value': 1.00,
            'clean_colour': 'gold',
            'rusty_colours': 'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5
        }
        super().__init__(**data)

,
coin1 = Pound()
print(coin1.rare)
print(coin1.value)
coin2 = Pound(rare=True)
print(coin2.rare)
print(coin2.value)
coin1.rust()
print(coin1.colour)
coin1.clean()
print(coin1.colour)
print(coin1.heads)
coin1.flip()
print(coin1.heads)
del coin1
