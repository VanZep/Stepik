"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных
холодильников. Теперь он использует их в качестве серверов "Пегого дудочника".
Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных
букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом
стоящие буквы, главное наличие последовательности букв), то холодильник
заражен и нужно вывести номер холодильника, нумерация начинается с единицы.

Формат входных данных
В первой строке подается число n – количество холодильников. В последующих
n строках вводятся строки, содержащие латинские строчные буквы и цифры,
в каждой строке от 5 до 100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. Если
таких холодильников нет, ничего выводить не нужно.

Тестовые данные
Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n

Sample Output 1:
1 2 3

Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton

Sample Output 2:
1 2 7 8

Sample Input 3:
1
anton

Sample Output 3:
1
"""

n = int(input())
pswd = 'anton'
refrigerator_numbers = []

for ref_number in range(1, n + 1):
    pointer = 0
    string = input()
    for char in string:
        if char == pswd[pointer]:
            pointer += 1
        if pointer == 5:
            refrigerator_numbers.append(ref_number)
            break

print(*refrigerator_numbers)
