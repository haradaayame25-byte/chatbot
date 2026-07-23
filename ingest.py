from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# PDFを読み込む
loader = PyPDFDirectoryLoader("documents")
documents = loader.load()

# チャンク化
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

# 確認
print(f"PDFページ数: {len(documents)}")
print(f"チャンク数: {len(chunks)}")

print("\n=== 最初のチャンク ===\n")
print(chunks[0].page_content)
