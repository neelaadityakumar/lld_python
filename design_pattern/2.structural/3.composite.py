# > The Composite Pattern lets you compose objects into tree-like structures and
# treat individual objects (leaf) and groups of objects (composite) the same way.
# - A **file system**:
#     - Files are **leaf nodes**
#     - Folders can contain files **or other folders**
#     - You can perform actions like `delete()`, `size()`, or `display()` on both

from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass


class File(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"File: {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print(' ' * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)


# Leaf nodes
file1 = File("resume.pdf")
file2 = File("budget.xlsx")
file3 = File("photo.jpg")

# Folders
docs = Folder("Documents")
pics = Folder("Pictures")
root = Folder("Root")

# Build the tree
docs.add(file1)
docs.add(file2)

pics.add(file3)

root.add(docs)
root.add(pics)

# Display full structure
root.display()

