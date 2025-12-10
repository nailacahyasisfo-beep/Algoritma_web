# Implementasi stack sederhana
stack = []

# Push (menambah data ke atas stack)
stack.append("A")
stack.append("B")
stack.append("C")

print("Isi Stack saat ini:", stack)

# Pop (mengambil data paling atas)
elemen = stack.pop()
print("Elemen yang di-pop :", elemen)

print("Isi Stack setelah pop:", stack)

# Melihat elemen paling atas tanpa menghapus
top = stack[-1]
print("Elemen paling atas :", top)

#HASIL MODIFIKASI

# Implementasi Stack menggunakan class
class Stack:
    def __init__(self):
        self.data = []

    # Push data ke stack
    def push(self, nilai):
        self.data.append(nilai)
        print(f"Push: {nilai}")

    # Pop data dari stack
    def pop(self):
        if len(self.data) > 0:
            nilai = self.data.pop()
            print(f"Pop: {nilai}")
        else:
            print("Stack kosong, tidak bisa pop!")

    # Melihat elemen teratas
    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return "Stack kosong"

    # Menampilkan isi stack
    def tampilkan(self):
        print("Isi Stack :", self.data)
        print("------------------------")


# Menggunakan Stack
stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

stack.tampilkan()

stack.pop()
stack.tampilkan()

print("Elemen paling atas :", stack.peek())
