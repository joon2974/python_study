message = input("Tell me something and I will repeat it back to you: ")
#input은 사용자가 입력한 값만을 매개변수로 갖는다!
print(message)

prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is you first name? "
name = input(prompt)
print("\nHello " + name + "!")
#input으로 입력받은 것은 전부 string으로 저장!


