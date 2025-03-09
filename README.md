# chatbot_url

📌 Description
This project is a custom AI-powered chatbot built using LangChain, FAISS, and Flask. The chatbot extracts data from the Brainlox Technical Courses webpage, creates vector embeddings using offline sentence-transformers, and stores them in a FAISS vector database for efficient retrieval. Users can interact with the chatbot via a REST API, which returns relevant course information based on their queries.

🚀 Features
✅ Data Extraction – Scrapes course data from the given website using LangChain’s URL loader.
✅ Offline Embeddings – Uses sentence-transformers/all-MiniLM-L6-v2 for local embedding generation.
✅ Vector Search with FAISS – Stores embeddings in FAISS for fast similarity-based retrieval.
✅ Flask API – Provides a /chat endpoint to handle user queries and return relevant course details.
✅ Fully Offline & Secure – No API keys required; runs entirely on local resources.

⚙️ Technologies Used
LangChain – For document loading and processing.
FAISS – For efficient vector storage and retrieval.
Sentence-Transformers – For offline embeddings.
Flask – For the REST API.
BeautifulSoup & Requests – For web scraping.


Install dependencies using :
pip install -r requirements.txt

Test the API (Using cURL or Postman) :
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"query": "Your Query"}'


