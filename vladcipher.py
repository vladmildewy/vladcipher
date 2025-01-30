import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth
import tkinter as tk
from tkinter import messagebox

# Определяем частоты для букв
frequencies = {
    'А': 200, 'Б': 210, 'В': 220, 'Г': 230, 'Д': 240,
    'Е': 250, 'Ё': 260, 'Ж': 270, 'З': 280, 'И': 290,
    'Й': 300, 'К': 310, 'Л': 320, 'М': 330, 'Н': 340,
    'О': 350, 'П': 360, 'Р': 370, 'С': 380, 'Т': 390,
    'У': 400, 'Ф': 410, 'Х': 420, 'Ц': 430, 'Ч': 440,
    'Ш': 450, 'Щ': 460, 'Ъ': 470, 'Ы': 480, 'Ь': 490,
    'Э': 500, 'Ю': 510, 'Я': 520,
    'A': 200, 'B': 210, 'C': 220, 'D': 230, 'E': 240,
    'F': 250, 'G': 260, 'H': 270, 'I': 280, 'J': 290,
    'K': 300, 'L': 310, 'M': 220, 'N': 230, 'O': 240,
    'P': 250, 'Q': 260, 'R': 270, 'S': 280, 'T': 290,
    'U': 300, 'V': 310, 'W': 320, 'X': 330, 'Y': 340,
    'Z': 350
}

# Функция для генерации звука
def generate_sound(letter: str, wave_type='sine'):
    frequency = frequencies.get(letter)
    
    if frequency is None:
        return AudioSegment.silent(duration=0) # Если буква не найдена
    
    duration = 300 # Длительность звука в миллисекундах
    silence_duration = 10 # Длительность тишины после буквы в миллисекундах
    
    if wave_type == 'sine':
        sound = Sine(frequency).to_audio_segment(duration=duration)
    elif wave_type == 'square':
        sound = Square(frequency).to_audio_segment(duration=duration)
    elif wave_type == 'sawtooth':
        sound = Sawtooth(frequency).to_audio_segment(duration=duration)
    
    silence = AudioSegment.silent(duration=silence_duration)
    
    return sound + silence

# Основная функция шифровки
def encode_message(message: str, wave_type='sine'):
    audio = AudioSegment.silent(duration=0) # Начинаем с тишины
    
    for char in message:
        if char == " ":
            audio += AudioSegment.silent(duration=300) # Тишина для пробела
        else:
            audio += generate_sound(char, wave_type)
    
    return audio

# Функция для обработки нажатия кнопки
def on_encode():
    message = entry_message.get()
    wave_type = wave_type_var.get()
    
    if not message:
        messagebox.showwarning("Предупреждение", "Введите сообщение.")
        return

    audio = encode_message(message.upper(), wave_type)
    
    # Сохранение результата в файл
    audio.export("message.wav", format="wav")
    messagebox.showinfo("Успех", "Сообщение закодировано и сохранено в файл message.wav")

# Создание GUI
root = tk.Tk()
root.title("Шифровка сообщений в звук")

# Метка и поле ввода для сообщения
label_message = tk.Label(root, text="Введите сообщение:")
label_message.pack()

entry_message = tk.Entry(root, width=50)
entry_message.pack()

# Выбор типа волны
wave_type_var = tk.StringVar(value='sine')
label_wave_type = tk.Label(root, text="Выберите тип волны:")
label_wave_type.pack()

radio_sine = tk.Radiobutton(root, text="Синусоида", variable=wave_type_var, value='sine')
radio_square = tk.Radiobutton(root, text="Квадрат", variable=wave_type_var, value='square')
radio_sawtooth = tk.Radiobutton(root, text="Пилообразная", variable=wave_type_var, value='sawtooth')

radio_sine.pack()
radio_square.pack()
radio_sawtooth.pack()

# Кнопка для шифровки
button_encode = tk.Button(root, text="Закодировать", command=on_encode)
button_encode.pack()

# Запуск основного цикла приложения
root.mainloop()
