import math


class Vector:
    """
    A 3D Vector class demonstrating Python Object-Oriented Programming and Magic (Dunder) Methods.
    This structure is fundamental in AI/ML for representing spatial data, embeddings, or features.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        # Initializing the 3D coordinates. Type hints (float) indicate expected data types.
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector') -> 'Vector':
        # Overloads the '+' operator. Returns a new Vector instance to maintain immutability.
        if not isinstance(other, Vector):
            raise TypeError("Operand must be an instance of the Vector class")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vector') -> 'Vector':
        # Overloads the '-' operator. Returns a new Vector instance.
        if not isinstance(other, Vector):
            raise TypeError("Operand must be an instance of the Vector class")
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other: object) -> bool:
        # Overloads the '==' operator to compare actual values instead of memory locations.
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __len__(self) -> int:
        # Returns the number of dimensions (3).
        # Note: In Python, __len__ must strictly return an integer.
        return 3

    def magnitude(self) -> float:
        """
        Calculates the Euclidean distance (magnitude) of the vector.
        Essential for AI/ML algorithms like K-Nearest Neighbors or Cosine Similarity.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __repr__(self) -> str:
        # Provides a clear, developer-friendly string representation of the object.
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"


# Execution block: ensures tests run only when this script is executed directly
if __name__ == "__main__":
    # 1. Instance Creation
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("--- Vector Representation ---")
    print(f"v1: {repr(v1)}")
    print(f"v2: {repr(v2)}\n")

    print("--- Dunder Methods in Action ---")
    # 2. Testing __add__
    print(f"Addition (v1 + v2): {v1 + v2}")

    # 3. Testing __sub__
    print(f"Subtraction (v2 - v1): {v2 - v1}")

    # 4. Testing __eq__
    print(f"Equality Check (v1 == v2): {v1 == v2}")
    print(f"Equality Check (same values): {v1 == Vector(1, 2, 3)}")

    # 5. Testing __len__
    print(f"Dimensions (len(v1)): {len(v1)}")

    # 6. Testing custom ML method
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
