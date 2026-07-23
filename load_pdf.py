from pypdf import PdfReader
import os

def load_documents(folder="documents"):
    """
    documentsフォルダ内のPDFをすべて読み込み、
    テキストをリストで返す。
    """

    documents = []

    for filename in os.listdir(folder):

        if filename.endswith(".pdf"):

            path = os.path.join(folder, filename)

            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            documents.append({
                "filename": filename,
                "content": text
            })

    return documents

#動作確認
if __name__ == "__main__":

    docs = load_documents()

    for doc in docs:

        print("=" * 50)
        print(doc["filename"])
        print("=" * 50)

        print(doc["content"][:1000])
