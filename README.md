# Сортировка спектр _ Компьютерная графика

## Формулировка задания
Дан датасет, состоящий из различных картинок. Картинки отличаются по цветам, при этом в каждой картинке обязательно преобладает какой-либо один цвет. Необходимо рассортировать изображения по цветам спектра, начиная с красного, заканчивая фиолетовым. Для удобства проверки переименуйте изображения в название цвета (red, orange, yellow, green, cyan, blue и тд)

Входные данные: папка с набором файлов .jpg

Выходные данные: папка с набором файлов .jpg

## Руководство пользователя

#### При запуске с .exe файла:
Для запуска необходимо иметь OS Windows;

#### При запуске с .py файла:
Для запуска необходимо иметь OS Windows, 
Python 3.10+,
установленные библиотеки: NumPy, Pillow, os, Tkinter.

#### Работа с приложением:
Доступно два поля для ввода: Input directory и Output directory, в которые нужно вписывать соответственно путь до папки с изображениями и путь до папки, куда нужно загрузить отсортированные изображения.
При нажатии на кнопку Sort отсортированные изображения загружаются в папку, на которую указал пользователь в Output directory.

## Как это работает?
На вход программа принимает директорию до папки с изображениями, которые нужно отсортировать по спектру. Изображения сжимаются внутри программы до 1 пикселя, значения RGB этого пикселя будут указывать на среднее значения цвета по всей картинки. Далее происходит перевод из RGB в другую цветовую модель — HSL. Значения Saturation(насыщенности) и Lightness(яркости) нас не интересуют, а по цветности Hue уже будет происходить сортировка.
