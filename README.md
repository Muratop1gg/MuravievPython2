# Репозиторий для 2 модуля `ЦК2024`

## Сейчас загружены:
- [Лабораторная работа 1](https://github.com/Muratop1gg/MuravievPython2/blob/main/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%201/lab.py)
- [Лабораторная работа 2](https://github.com/Muratop1gg/MuravievPython2/blob/main/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%202/lab.py)
- [Лабораторная работа 3](https://github.com/Muratop1gg/MuravievPython2/blob/main/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%203/lab.py)
- [Лабораторная работа 4](https://github.com/Muratop1gg/MuravievPython2/blob/main/%D0%9B%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F%204/lab.py)


## Смешной кот-программист:

![Смешной кот-программист](https://c.tenor.com/y2JXkY1pXkwAAAAM/cat-computer.gif)


## Как я легко правил код для проверки:

Создал репозиторий на [github codespaces](https://github.com/codespaces)

Установил пакет `black`

```bash
  pip install black
```
Создал файл `lab.py` и скопировал в него свой код

Запустил утилиту автоисправления для файла

```bash
  black lab.py  -l120 --skip-string-normalization
```

На всякий случай запустил проверку с параметрами, указанными в репозитории-шаблоне

```bash
  black lab.py  -l120 --skip-string-normalization --check
```

Получил сообщение: 
```
All done! ✨ 🍰 ✨
1 file would be left unchanged.
```
