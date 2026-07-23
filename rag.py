from openai import OpenAI

client = OpenAI()

def search_documents(question):
    """
    今はダミー
    後でChromaDBなどの検索結果に置き換える
    """
    return """
    静岡大学の授業は原則15回で実施されます。
    シラバスは大学ポータルから確認できます。
    """

def ask_question(question):

    context = search_documents(question)

    prompt = f"""
以下の資料を参考に回答してください。

【資料】
{context}

【質問】
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system","content":"あなたは大学専用チャットボットです。"},
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content
