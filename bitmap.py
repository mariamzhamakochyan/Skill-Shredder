class Bitmap:
    def __init__(self, size):
        """
        Initialize the bitmap with a given size.

        Args:
        size (int): The number of bits in the bitmap.
        """
        self.size = size
        self.bitmap = set()

    def set(self, pos):
        """
        Set the bit at the specified position to 1.

        Args:
        pos (int): The position of the bit to set.
        """
        if 0 <= pos < self.size:
            self.bitmap.add(pos)

    def clear(self, pos):
        """
        Set the bit at the specified position to 0.

        Args:
        pos (int): The position of the bit to clear.
        """
        if 0 <= pos < self.size:
            self.bitmap.discard(pos)

    def get(self, pos):
        """
        Get the value of the bit at the specified position.

        Args:
        pos (int): The position of the bit to get.

        Returns:
        int: The value of the bit (0 or 1).
        """
        return 1 if pos in self.bitmap else 0

    def __str__(self):
        """Return a string representation of the bitmap."""
        return "".join(str(self.get(pos)) for pos in range(self.size))


# Example usage:
if __name__ == "__main__":
    bitmap = Bitmap(16)

    bitmap.set(2)
    bitmap.set(5)
    bitmap.set(10)

    print("Bitmap:", bitmap)
    print("Bit at position 5:", bitmap.get(5))

    bitmap.clear(5)
    print("Bitmap after clearing position 5:", bitmap)

