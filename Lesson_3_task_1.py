# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

# Вариант 1

print('---------Вариант 1---------------')

spam = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
for i in range(2, 100):
    if i % 2 == 0:
        spam[2].append(i)
    if i % 3 == 0:
        spam[3].append(i)
    if i % 4 == 0:
        spam[4].append(i)
    if i % 5 == 0:
        spam[5].append(i)
    if i % 6 == 0:
        spam[6].append(i)
    if i % 7 == 0:
        spam[7].append(i)
    if i % 8 == 0:
        spam[8].append(i)
    if i % 9 == 0:
        spam[9].append(i)

k = sorted(list(spam.keys()))
for key in k:
    print(f'Числу {key} кратны {len(spam[key])} чисел')

# ---------------------------------------------------------------------------------------------------------------------
# Вариант 2 == усовершенствованный вариант 1
print('---------Вариант 2 == усовершенствованный вариант 1--------------')

spam_2 = {i: [] for i in range(2, 10)}
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            spam_2[j].append(i)

k_2 = sorted(list(spam_2.keys()))
for key_2 in k_2:
    print(f'Числу {key_2} кратны {len(spam_2[key_2])} чисел')


print(f'spam == spam_2 => {spam_2 == spam}')
# ----------------------------------------------------------------------------------------------------------------------
# Вариант 3
print('---------Вариант 3---------------')

print(f'Числу 2 кратны {len([i for i in range(2, 100) if i % 2 == 0])} чисел')
print(f'Числу 3 кратны {len([i for i in range(2, 100) if i % 3 == 0])} чисел')
print(f'Числу 4 кратны {len([i for i in range(2, 100) if i % 4 == 0])} чисел')
print(f'Числу 5 кратны {len([i for i in range(2, 100) if i % 5 == 0])} чисел')
print(f'Числу 6 кратны {len([i for i in range(2, 100) if i % 6 == 0])} чисел')
print(f'Числу 7 кратны {len([i for i in range(2, 100) if i % 7 == 0])} чисел')
print(f'Числу 8 кратны {len([i for i in range(2, 100) if i % 8 == 0])} чисел')
print(f'Числу 9 кратны {len([i for i in range(2, 100) if i % 9 == 0])} чисел')
