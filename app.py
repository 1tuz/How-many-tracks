from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
from decimal import Decimal, ROUND_HALF_UP


# Глобальные настройки
Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
Window.title = "How many tracks?"


class MyApp(App):

    # Создание всех виджетов (объектов)
    def __init__(self):
        super().__init__()
        self.label = Label(text='Сколько треков?')
        self.kilometres = Label(text='Для прохождения пути Вам необходимо прослушать ')
        self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
        self.input_data.bind(text=self.on_text)  # Добавляем обработчик события

    # Получаем данные и производим их конвертацию
    def on_text(self, *args):
        data = self.input_data.text
        number_of_tracks = (int(data) / 4) / 3.5 * 60
        result = Decimal(str(number_of_tracks)).quantize(Decimal("1.0"), ROUND_HALF_UP)
        if data.isnumeric():
            self.kilometres.text = 'Для прохождения пути Вам необходимо прослушать ' + str(result) + ' трека(ов)'

        else:
            self.input_data.text = ''

    # Основной метод для построения программы
    def build(self):
        # Все объекты будем помещать в один общий слой
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.kilometres)

        return box


# Запуск проекта
if __name__ == "__main__":
    MyApp().run()
