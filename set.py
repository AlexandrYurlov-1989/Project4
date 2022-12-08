from random import randint

N1 = int(input("Введите количество цифр в первом наборе:"))
set1 = set()
for i in range(N1):
    set1.add(randint(1,20))

N2 = int(input("Введите количество цифр во втором наборе:"))
set2 = set()
for i in range(N2):
    set2.add(randint(1,20))

print(f"первый набор{set1}")
print(f"второй набор{set2}")
print(f"входят одновременно в оба{set1.intersection(set2)}")
print(f"входят только в первое, но не входят во второе{set1 - set2}")
print(f"входят только во второе, но не входят в первое{set2 - set1}")
print(f"входят в первое или во второе, но не в оба из них одновременно{set1 ^ set2}")