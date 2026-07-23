from rag import ask_question

print("大学チャットボット")
print("終了するには exit を入力")

#exitとなるまで繰り返す
while True:
    question = input("あなた：")

    #exitと入力されたとき
    if question.lower() == "exit":
        break

    #ルールベースでの回答
    answer = faq(question)

    #AIの返答
    answer = ask_question(question)
    print("Bot：", answer)
