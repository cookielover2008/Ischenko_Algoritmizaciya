import tkinter as tk

def check_odd():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
    except ValueError:
        result_label.config(text="Ошибка: Пожалуйста, введите целые числа.")
        return

    odd_num = (a % 2 != 0) + (b % 2 != 0)

    if odd_num == 1:
        result_label.config(text="Ровно одно из чисел нечетное.\nВысказывание истинно.")
    else:
        result_label.config(text="Оба числа либо четны, либо нечетны.\nВысказывание ложно.")

# Настройка главного окна
root = tk.Tk()
root.title("Проверка четности чисел")
root.geometry("300x200")  # Установка размера окна

# Создание полей ввода и кнопки
label_a = tk.Label(root, text="Введите первое число (A):")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Введите второе число (B):")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

check_button = tk.Button(root, text="Проверить", command=check_odd)
check_button.pack()

result_label = tk.Label(root, text="", wraplength=250)  # Метка для отображения результата
result_label.pack(pady=10)

# Запуск приложения
root.mainloop()