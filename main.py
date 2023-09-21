from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
import numpy as np

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Ajoutez un fond orange à l'écran
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Couleur blanche (RGBA)
            self.rect = Rectangle(size=(800, 600), pos=(0, 0))  # Taille de l'écran
        

        

        label_with_background = Label(
            text="HParking",
            size_hint=(None, None),
            size=(800, 50),
            pos=(0, 550),
            font_size=30,
        )
        # Ajoutez un rectangle orange en arrière-plan du label
        with label_with_background.canvas.before:
            Color(1, 0.5, 0, 1)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=label_with_background.size, pos=label_with_background.pos)
        
        self.add_widget(label_with_background)
        
        # Ajoutez une image
        image = Image(source='tps.png', size_hint=(None, None), size=(600, 500), pos=(100, 75))
        # Remplacez 'votre_image.png' par le chemin de votre propre image
        self.add_widget(image)
        

        
        # Ajoutez un bouton

        
        
        button = Button(text="My actual location", font_size = (40), size_hint=(None, None), size=(500, 70), pos=(150,25) ,
            background_normal='button.png', background_down='button1.png')
       
        button.bind(on_press=self.go_to_second_screen)
        self.add_widget(button)

        # button1 = Button(text="Position 2", font_size = (30), size_hint=(None, None), size=(200, 70), pos=(300, 25) ,
        #     background_normal='button.png', background_down='button1.png')
       
        # button1.bind(on_press=self.go_to_second_screen)
        # self.add_widget(button1)

        # button2 = Button(text="Position 3", font_size = (30), size_hint=(None, None), size=(200, 70), pos=(550, 25) ,
        #     background_normal='button.png', background_down='button1.png')
       
        # button2.bind(on_press=self.go_to_second_screen)
        # self.add_widget(button2)

    def go_to_second_screen(self, instance):
        app = App.get_running_app()
        app.root.current = 'second_screen'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Couleur blanche (RGBA)
            self.rect = Rectangle(size=(800, 600), pos=(0, 0))  # Taille de l'écran

        label_with_background = Label(
            text="HParking",
            size_hint=(None, None),
            size=(800, 50),
            pos=(0, 550),
            font_size=30,
        )
        # Ajoutez un rectangle orange en arrière-plan du label
        with label_with_background.canvas.before:
            Color(1, 0.5, 0, 1)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=label_with_background.size, pos=label_with_background.pos)
        
        self.add_widget(label_with_background)

        # Ajoutez une image
        image = Image(source='map.png', size_hint=(None, None), size=(600, 500), pos=(100, 75))
        # Remplacez 'votre_image.png' par le chemin de votre propre image
        self.add_widget(image)

        label = Label(text="Please choose your destination.",size_hint=(None, None),
            size=(500, 50),
            pos=(150, 150),
            font_size=30,
            )
        with label.canvas.before:
            Color(0.5, 0.5, 0.5, 1.0)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=label.size, pos=label.pos)
        self.add_widget(label)
        button = Button(text="My residence",font_size = (30), size_hint=(None, None), size=(200, 70), pos=(50, 25) ,
            background_normal='button.png', background_down='button1.png')
       
        button.bind(on_press=self.go_to_third_screen)
        self.add_widget(button)

        button1 = Button(text="The office",font_size = (30), size_hint=(None, None), size=(200, 70), pos=(300, 25) ,
            background_normal='button.png', background_down='button1.png')
       
        button1.bind(on_press=self.go_to_third_screen)
        self.add_widget(button1)

        button2 = Button(text="School",font_size = (30), size_hint=(None, None), size=(200, 70), pos=(550, 25) ,
            background_normal='button.png', background_down='button1.png')
       
        button2.bind(on_press=self.go_to_third_screen)
        self.add_widget(button2)

    def on_enter(self):
            # Appeler la fonction pour calculer WASPAS lorsque la première page est affichée
        results = WASPAS()
            
            # Accéder à la deuxième page et afficher les résultats
        third_screen = self.manager.get_screen('third_screen')
        third_screen.show_results(results)
        

    def go_to_third_screen(self, instance):
        app = App.get_running_app()
        app.root.current = 'third_screen'

class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Couleur blanche (RGBA)
            self.rect = Rectangle(size=(800, 600), pos=(0, 0))  # Taille de l'écran

        label_with_background = Label(
            text="HParking",
            size_hint=(None, None),
            size=(800, 50),
            pos=(0, 550),
            font_size=30,
        )
        # Ajoutez un rectangle orange en arrière-plan du label
        with label_with_background.canvas.before:
            Color(1, 0.5, 0, 1)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=label_with_background.size, pos=label_with_background.pos)
        
        self.add_widget(label_with_background)

        

        label = Label(text="Veuillez choisir votre destination .",font_size = (50), size_hint=(None, None),
            size=(500, 50),
            pos=(150, 150))
        with label.canvas.before:
            Color(0.5, 0.5, 0.5, 1.0)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=label.size, pos=label.pos)

        

        self.results_label = Label(font_size=30, size_hint=(None, None), size=(400, 300), pos=(200, 150), text="")

        self.add_widget(self.results_label)

        with self.results_label .canvas.before:
            Color(1, 0.5, 0, 1)  # Couleur orange plus lumineuse (RGBA)
            self.rect = Rectangle(size=self.results_label .size, pos=self.results_label .pos)

    
        
        button2 = Button(text="Back",font_size = (30), size_hint=(None, None), size=(200, 70), pos=(300, 25) ,
            background_normal='button.png', background_down='button1.png')
       
        button2.bind(on_press=self.go_to_first_screen)
        self.add_widget(button2)
    def show_results(self, results):
        # Afficher les résultats dans le label
        self.results_label.text = results

    
        

    def go_to_first_screen(self, instance):
        app = App.get_running_app()
        app.root.current = 'first_screen'

def WASPAS():
        # Définir les parkings et les critères
        parkings = ['parking 1', 'parking 2', 'parking 3']
        criteria = ['Criterion 1', 'Criterion 2', 'Criterion 3', 'Criterion 4', 'Criterion 5']

        # Définir les données de performance pour chaque parking et chaque critère
        performance_data = np.array([
            [0.8, 0.7, 0.6, 0.75, 0.85],
            [0.6, 0.9, 0.7, 0.8, 0.7],
            [0.7, 0.8, 0.9, 0.7, 0.6]
        ])

        # Définir les poids des critères (plus grand = plus important)
        weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

        # Calculer le score WASPAS pour chaque parking
        scores = np.dot(performance_data, weights)

        # Trier les parkings en fonction des scores WASPAS
        ranked_parkings = [x for _, x in sorted(zip(scores, parkings), reverse=True)]

        # Afficher les résultats
        results = "WASPAS results: \n"
        for i, parking in enumerate(ranked_parkings):
            results +=f"{i + 1}. {parking}\n"

        return results

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        
        first_screen = FirstScreen(name='first_screen')
        second_screen = SecondScreen(name='second_screen')
        third_screen = ThirdScreen(name='third_screen')
        sm.add_widget(first_screen)
        sm.add_widget(second_screen)
        sm.add_widget(third_screen)

        sm.current = 'first_screen'

        return sm

if __name__ == '__main__':
    MyApp().run()