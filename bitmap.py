class Bitmap:
    def __init__(self, size):
 
        self.size = size
        self.bitmap = set()

    def set(self, pos):
        
        if 0 <= pos < self.size:
            self.bitmap.add(pos)

    def clear(self, pos):
        if 0 <= pos < self.size:
            self.bitmap.discard(pos)

    def get(self, pos):
        return 1 if pos in self.bitmap else 0

    def __str__(self):
        return "".join(str(self.get(pos)) for pos in range(self.size))


if __name__ == "__main__":
    bitmap = Bitmap(16)

    bitmap.set(2)
    bitmap.set(5)
    bitmap.set(10)

    print("Bitmap:", bitmap)
    print("Bit at position 5:", bitmap.get(5))

    bitmap.clear(5)
    print("Bitmap after clearing position 5:", bitmap)

