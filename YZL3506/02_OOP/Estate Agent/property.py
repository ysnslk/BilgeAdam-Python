from utilities import get_valid_input


class Property:
    def __init__(self, square_feet='', bedrooms='', bathrooms='', *args, **kwargs):
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.square_feet = square_feet

    def display(self):
        print(f'General Information\n'
              f'===================='
              f'Square Feet: {self.square_feet}\n'
              f'Bedrooms: {self.bedrooms}\n'
              f'Bathrooms: {self}\n')

    def promp_init():
        return dict(
            square=input('Square Feet: '),
            bedrooms=input('Bedrooms: '),
            bathrooms=input('Bathrooms: ')
        )

    promp_init = staticmethod(promp_init)


class Apartment(Property):
    def __init__(self, balcony='', laundry='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.laundry = laundry
        self.balcony = balcony

    def display(self):
        super().display()
        print(f'Balcony: {self.balcony}\n'
              f'Laundry: {self.laundry}\n')

    def prompt_init():
        parent_init = Property.promp_init()

        balcony = get_valid_input(
            'Does apartment have a balcony',
            ('yes', 'no')
        )

        laundry = get_valid_input(
            'What laundry type do you prefer?',
            ('yes', 'no')
        )

        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    def __init__(self, number_stories='', garage='', fenced='', pool='', *args, **kwargs):
        super().display()
        print(f'Number of stories: {self.number_stories}\n'
              f'Fenced: {self.fenced}\n'
              f'Garage: {self.garage}\n'
              f'Pool: {self.pool}\n')

    def prompt_init():
        parent_init = Property.promp_init()

        number_stories = input('How many stories do you want?')

        garage = get_valid_input(
            input_question='Do you want garage?',
            valid_options=('yes', 'no')
        )

        pool = get_valid_input(
            input_question='Do you prefer to pool your house',
            valid_options=('yes', 'no')
        )

        fenced = get_valid_input(
            input_question='Do you prefer to fenced in your house?',
            valid_options=('yes', 'no')
        )

        parent_init.update({
            'number_stories': number_stories,
            'garage': garage,
            'fenced': fenced,
            'pool': pool
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)
