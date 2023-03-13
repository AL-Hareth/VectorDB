import numpy as np


class Vector:
    id: str
    default_value: list
    relation: str = ""
    values = np.array([])

    def __init__(self, id: str, default_value: list):
        self.id = id
        self.default_value = default_value
        self.values = np.array(self.default_value)

    def show(self):
        return self.values

    def add_value(self, value):
        self.values = np.append(self.values, value)

    def get_selected_values(self, filter_vector: np.ndarray):

        shifted_vector = self.values + filter_vector
        compare_vector = (shifted_vector == self.values)
        selected = []
        for i, item in enumerate(compare_vector):
            if item == True:
                selected.append(self.values[i])
        return selected

    def remove_value(self, value):
        remove_indecies = list(np.where(self.values == value)[0])
        self.values = np.delete(self.values, remove_indecies)


class UnitVector(Vector):

    def __init__(self, id: str, default_value: list) -> None:
        for i in list(set(default_value)):
            if not (i == 1 or i == 0):
                raise RuntimeError("You can only Insert ones and zeros")
        if not 1 in default_value:
            raise RuntimeError("Your list must include 1")
        if default_value.count(1) != 1:
            raise RuntimeError("You Can only have a single ONE value")

        self.id = f"u_{id}"
        self.values = np.array(default_value)

    def remove_value(self, index):
        if self.values[index] == 1:
            raise RuntimeError(
                "You can't remove the item that has the value one")
        self.values = np.delete(self.values, index)

    def add_value(self, value=0):
        if value == 0:
            return super().add_value(value)
        raise RuntimeError("The value can only be one or zero")

    def move_unit_value(self, to_index):
        from_index = np.where(self.values == 1)[0]
        self.values[from_index] = 0
        self.values[to_index] = 1


class Database:

    vectors = {}

    def __init__(self, name):
        self.name = name

    def create_vector(self, id: str, default_values: list) -> None:
        self.vectors[id] = Vector(id, default_values)

    def create_unit_vector(self, id: str, default_value: list):
        self.vectors[id] = UnitVector(id, default_value)

    def get_vectors(self):
        return self.vectors.keys()

    def get_vector(self, vector_id: str) -> Vector:
        return self.vectors[vector_id]

    def drop_vector(self, vector_id: str) -> None:
        self.vectors.__delitem__(vector_id)

    def create_relation(self, first_vector: Vector, second_vector: Vector):
        if (first_vector.relation != "") or (second_vector.relation != ""):
            return RuntimeError('One of the Vectors is already related to another vector')
        else:
            first_vector.relation = second_vector.id
            second_vector.relation = first_vector.id

    def get_relation_of_vector(self, vector: Vector) -> str:
        if vector.relation != "":
            return vector.relation
        return "This Vector has no relations!"
