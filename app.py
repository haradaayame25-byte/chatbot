from rag import ask_question

print("大学チャットボット")
print("終了するには exit を入力")

while True:
    question = input("あなた：")

    if question.lower() == "exit":
        break

    answer = ask_question(question)
    print("Bot：", answer)
