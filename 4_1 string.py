
sentence = '나는 Nemo입니다'
print(sentence)

sentence2 = "Python은 꿀잼!"
print(sentence2)

sentence3 = """
나는 Nemo이고,
Python은 꿀잼!
"""
print(sentence3)

juminNum = "920212-1234567"
print("성별 : " + juminNum[7])
print("Year : " + juminNum[0:2])
print("Month : " + juminNum[2:4])
print("Day : " + juminNum[4:6])
print("Birth : " + juminNum[0:6])
# 처음부터 6 직전까지 Print
print("Birth : " + juminNum[:6])

print("뒤 7자리 : " + juminNum[7:14])
# 7부터 끝까지
print("뒤 7자리 : " + juminNum[7:])
# 맨 뒷자리는 -1, 맨 뒤에서 7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + juminNum[-7:])