# 1
class Talaba:
    def __init__(self, i, y, k):
        self.ism = i
        self.yosh = y
        self.kurs = k


t = Talaba("Ali", 18, 1)
print(t.ism)
print(t.yosh)
print(t.kurs)

# 2
class Telefon:
    def __init__(self, b, m, n):
        self.brend = b
        self.model = m
        self.narx = n


tel1 = Telefon("Samsung", "A16", 2145)
print(tel1.model)
print(tel1.brend)
print(tel1.narx)

# 3
class Kompyuter:
    def __init__(self, p, r, s):
        self.protsessor = p
        self.ram = r
        self.ssd = s


k1 = Kompyuter("I5", 8, 256)
print(k1.protsessor)
print(k1.ram)
print(k1.ssd)
