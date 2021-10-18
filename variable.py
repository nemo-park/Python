# 변수

animal = "강아지"
name = "바둑이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "낮잠"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# 쉼표(,)로 여러 문장을 합칠 수 있고 정수형/Boolean 변수를 그대로 쓸 수 있지만 빈칸이 한칸 들어가게 됨
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

