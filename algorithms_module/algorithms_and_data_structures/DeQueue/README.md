# DeQueue
## Определение:
DeQueue — структура данных, которая позваляет добавлять и удалять элементы как с начала, так и с конца очереди.


| Операция        | Описание                                                  | Временная сложность |
|-----------------|-----------------------------------------------------------|---------------------|
| `is_empty`      | Проверяет, пуст ли список                                 | O(1)                |
| `add_front`     | Добавялет элемент в начало очереди                        | O(1)                |
| `add_rear`      | Добавляет элемент в конец очеред                          | O(1)                |
| `remove_front`  | Удаляет и возвращает первый элемент очереди               | O(1)                |
| `remove_rear`   | Удаляет и возвращает последний элемент очереди            | O(1)                |
| `peek_front`    | Возвращает первый элемент очереди без удаления            | O(1)                |
| `peek_rear`     | Возвращает последний элемент очереди без удаления         | O(1)                |