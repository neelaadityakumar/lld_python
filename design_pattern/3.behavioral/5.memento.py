# The Memento Pattern captures and stores the internal state of an object
# so that it can be restored later, without exposing the object's implementation details.
# - `Editor`: the Originator (the object whose state needs saving)
# - `Memento`: stores state
# - `History`: Caretaker that manages saved states
class EditorMemento:
    def __init__(self, content: str):
        self._content = content

    def get_saved_state(self):
        return self._content


class Editor:
    def __init__(self):
        self._content = ""

    def type(self, words: str):
        self._content += words

    def get_content(self):
        return self._content

    def save(self):
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento):
        self._content = memento.get_saved_state()


class History:
    def __init__(self):
        self._history = []

    def push(self, memento: EditorMemento):
        self._history.append(memento)

    def pop(self) -> EditorMemento:
        return self._history.pop() if self._history else None


editor = Editor()
history = History()

editor.type("This is the first sentence. ")
history.push(editor.save())

editor.type("This is the second sentence. ")
history.push(editor.save())

editor.type("This is the third sentence.")

print("Current content:", editor.get_content())

editor.restore(history.pop())
print("After 1 undo:", editor.get_content())

editor.restore(history.pop())
print("After 2 undo:", editor.get_content())

