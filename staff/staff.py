# staff entity class
class Staff:

    def __init__(self, id_: int, parent_id: int, name: str, type_: int):
        self.id: int = id_
        self.parent_id: int = parent_id
        self.name: str = name
        self.type: int = type_
