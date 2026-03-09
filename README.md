CLI utility for cleaning and optimizing macOS
Scan, analyze and clean your system directly from the terminal

Features
Command	Description
scan	Scan system, show how much space can be freed
status	Show disk usage
clean cache	Clean system and user caches
clean logs	Remove system logs
clean xcode	Clean Xcode (DerivedData, Archives)
clean trash	Empty Trash
clean all	Clean all of the above
bigfiles	Find large files (>100MB)
duplicates	Find duplicate files by hash
Installation
Quick Start
# Clone repository
git clone https://github.com/whickybravo388/macleaner.git
cd macleaner

# Run
python3 maccleaner.py --help
Install System-wide
# Add to PATH (globally)
sudo ln -s $(pwd)/maccleaner.py /usr/local/bin/maccleaner
chmod +x maccleaner.py

# Now run from anywhere
maccleaner status
Usage
Check Disk Status
$ maccleaner status
💾 Disk Usage Status

Total:     228.27 GB
Used:      168.25 GB
Free:      60.02 GB
Usage:     73.7%

Top directories in home:
  Home              61.90 GB
  Documents          6.16 GB
  Desktop            2.75 GB
Scan System
$ maccleaner scan
🔍 Scanning system for cleanable files...

  Caches                  2.43 GB
  Logs                  134.13 MB

===================================
  Total cleanable:    2.56 GB
Cleaning
# Clean specific category
maccleaner clean cache
maccleaner clean logs
maccleaner clean xcode

# Clean everything
maccleaner clean all

# Skip confirmation
maccleaner clean all --force
Find Large Files
$ maccleaner bigfiles
🔍 Searching for files larger than 100MB...

Found 12 large files:

  5.23 GB - /Users/user/Downloads/film.mkv
  2.10 GB - /Users/user/Documents/vmware.dmg
  ...
Find Duplicates
$ maccleaner duplicates
🔍 Searching for duplicate files (by hash)...

Found 5 duplicate files:

  150.00 MB
    Original: /Users/user/Documents/photos/vacation.jpg
    Duplicate: /Users/user/Desktop/vacation_copy.jpg
Safety
✅ Asks for confirmation before deletion
✅ Does not delete system files
✅ Shows size before cleaning
✅ Use --force flag for automation
Requirements
macOS 10.14+
Python 3.7+
License
MIT License — free to use and distribute.

Contributing
Pull requests are welcome! Create issues with suggestions.

Made with ❤️ for the macOS community


# MacCleaner CLI

<p align="center">
  <img src="https://img.shields.io/badge/macOS-Support-brightgreen?style=for-the-badge&logo=apple" alt="macOS">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <strong>CLI-утилита для очистки и оптимизации macOS</strong><br>
  Сканируйте, анализируйте и очищайте систему прямо из терминала
</p>

---

## Возможности

| Команда | Описание |
|---------|----------|
| `scan` | Сканирование системы, показывает сколько места можно освободить |
| `status` | Отображение использования диска |
| `clean cache` | Очистка системных и пользовательских кэшей |
| `clean logs` | Удаление системных логов |
| `clean xcode` | Очистка Xcode (DerivedData, Archives) |
| `clean trash` | Очистка корзины |
| `clean all` | Очистка всего вышеперечисленного |
| `bigfiles` | Поиск больших файлов (>100MB) |
| `duplicates` | Поиск дубликатов файлов по хэшу |

---

## Установка

### Быстрый старт

```bash
# Клонирование репозитория
git clone https://github.com/whickybravo388/maccleaner.git
cd maccleaner

# Запуск
python3 maccleaner.py --help
```

### Установка в систему

```bash
# Добавить в PATH (глобально)
sudo ln -s $(pwd)/maccleaner.py /usr/local/bin/maccleaner
chmod +x maccleaner.py

# Теперь можно запускать из любого места
maccleaner status
```

---

## Использование

### Проверка статуса диска

```bash
$ maccleaner status
💾 Disk Usage Status

Total:     228.27 GB
Used:      168.25 GB
Free:      60.02 GB
Usage:     73.7%

Top directories in home:
  Home              61.90 GB
  Documents          6.16 GB
  Desktop            2.75 GB
```

### Сканирование системы

```bash
$ maccleaner scan
🔍 Scanning system for cleanable files...

  Caches                  2.43 GB
  Logs                  134.13 MB

===================================
  Total cleanable:    2.56 GB
```

### Очистка

```bash
# Очистить конкретную категорию
maccleaner clean cache
maccleaner clean logs
maccleaner clean xcode

# Очистить всё
maccleaner clean all

# Пропустить подтверждение
maccleaner clean all --force
```

### Поиск больших файлов

```bash
$ maccleaner bigfiles
🔍 Searching for files larger than 100MB...

Found 12 large files:

  5.23 GB - /Users/user/Downloads/film.mkv
  2.10 GB - /Users/user/Documents/vmware.dmg
  ...
```

### Поиск дубликатов

```bash
$ maccleaner duplicates
🔍 Searching for duplicate files (by hash)...

Found 5 duplicate files:

  150.00 MB
    Original: /Users/user/Documents/photos/vacation.jpg
    Duplicate: /Users/user/Desktop/vacation_copy.jpg
```

---

## Безопасность

- ✅ Запрашивает подтверждение перед удалением
- ✅ Не удаляет системные файлы
- ✅ Показывает размер перед очисткой
- ✅ Использует флаг `--force` для автоматизации

---

## Требования

- macOS 10.14+
- Python 3.7+

---

## Лицензия

MIT License — свободное использование и распространение.

---

## Contributing

Приветствуются pull requests! Создавайте issues с предложениями.

---

<p align="center">
  Сделано с ❤️ для macOS сообщества
</p>
