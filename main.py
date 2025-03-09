from flask import Flask, request, jsonify
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings("ignore")


url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()
print("Data loaded successfully")


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embedding_model)
print("Vector store created successfully")


vectorstore.save_local("faiss_index")


app = Flask(__name__)


vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
print("Vector store loaded successfully")

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get("query")
    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    results = vectorstore.similarity_search(user_query, k=3)
    response = [doc.page_content for doc in results]

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
