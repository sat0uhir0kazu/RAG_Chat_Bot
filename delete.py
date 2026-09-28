import chromadb
from chromadb.errors import NotFoundError

client = chromadb.PersistentClient(path="./chroma_db")

try:
    client.delete_collection(name="company_documents")
    print("company_documents コレクションを削除しました")
except NotFoundError:
    print("company_documents コレクションは存在しません")