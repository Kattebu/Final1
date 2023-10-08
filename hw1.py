notes = []
def create_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    note = {"title": title, "content": content}
    notes.append(note)
    print("Заметка успешно создана!")

def save_notes():
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(f"{note['title']}\n{note['content']}\n")
    print("Заметки успешно сохранены!")

def read_notes():
    if len(notes) == 0:
        print("Список заметок пуст!")
    else:
        for i, note in enumerate(notes):
            print(f"{i + 1}. {note['title']}")
        note_num = int(input("Введите номер заметки для просмотра: "))
        print(f"Заголовок: {notes[note_num - 1]['title']}")
        print(f"Содержание: {notes[note_num - 1]['content']}")

def edit_note():
    if len(notes) == 0:
        print("Список заметок пуст!")
    else:
        for i, note in enumerate(notes):
            print(f"{i + 1}. {note['title']}")
        note_num = int(input("Введите номер заметки для редактирования: "))
        notes[note_num - 1]["title"] = input("Введите новый заголовок заметки: ")
        notes[note_num - 1]["content"] = input("Введите новое содержание заметки: ")
        print("Заметка успешно отредактирована!")

def delete_note():
    if len(notes) == 0:
        print("Список заметок пуст!")
    else:
        for i, note in enumerate(notes):
            print(f"{i + 1}. {note['title']}")
        note_num = int(input("Введите номер заметки для удаления: "))
        del notes[note_num - 1]
        print("Заметка успешно удалена!")

while True:
    print("""
    1. Создать заметку
    2. Сохранить заметки
    3. Просмотреть список заметок
    4. Редактировать заметку
    5. Удалить заметку
    6. Выйти из программы
    """)
    choice = int(input("Выберите действие: "))
    if choice == 1:
        create_note()
    elif choice == 2:
        save_notes()
    elif choice == 3:
        read_notes()
    elif choice == 4:
        edit_note()
    elif choice == 5:
        delete_note()
    elif choice == 6:
        break
    else:
        print("Неверный выбор!")