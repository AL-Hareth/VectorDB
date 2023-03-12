import numpy as np

class Vector:
    id: str
    default_value: list
    values = np.array([])
    def __init__(self, id, default_value):
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

class Database:
    
    vectors = {}

    def __init__(self, name):
        self.name = name
    
    def create_vector(self, id, default_values: list):
        self.vectors[id] = Vector(id, default_values)

    def get_vectors(self):
        return self.vectors.keys()
    
    def inner(self, vec1: Vector, vec2: Vector):
        return np.inner(vec1.show(), vec2.show())

