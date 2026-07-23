from ollama import chat

#AIが返答
def ask_question(question):

    response = chat(
        model="llama3.2",  #AIモデルの指定
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    #返事を取り出す
    return response["message"]["content"]
