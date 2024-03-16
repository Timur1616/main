from colorama import init, Fore, Back, Style, deinit, reinit

init(autoreset=True)

print(Fore.RED + 'Fore робить текст кольору якій буде вказаний після крапки Fore.RED')
print(Back.BLUE + 'Back додає фон тексту колір фону можна так само змінити як і в Fore')
print(Style.BRIGHT + Fore.GREEN + 'у атрибуту Style є три стилі "Style.DIM Робить текст тьмянішим", "Style.NORMAL Стандартний", та "Style.BRIGHT Робить колір тексту яскравішим"')

deinit()

print('deinit() Метод, що деініціалізує Colorama та повертає вивід у його стандартний стан. ')

reinit()
print(Fore.YELLOW + 'reinit() Повторно ініціалізує Colorama після її деініціалізації.')
print(Fore.BLUE + 'init() Це метод якій готуєконсоль до використання кольорового тексту та забезпечуючи правильне відображення кольорів')
deinit()
