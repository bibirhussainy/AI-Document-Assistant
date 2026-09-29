# 📄 AI Document Assistant

A deployed **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content.

The system retrieves semantically relevant passages from the document and uses them as context for an OpenAI language model to generate grounded answers with page-level source references.

🚀 **Live Demo:** [Try the AI Document Assistant](https://bibirhussainy-ai-document-assistant-app-n7gjz6.streamlit.app/)

---

## ✨ Key Features

- Upload and process PDF documents
- Preserve page numbers during text extraction
- Split documents into overlapping, page-aware chunks
- Generate semantic embeddings using Sentence Transformers
- Retrieve relevant passages using cosine similarity
- Generate answers grounded in retrieved document context
- Display source page references with each answer
- Allow users to inspect the retrieved source passages
- Handle questions where information is not available in the document
- Interactive web interface built with Streamlit

---

## 🧠 RAG Architecture

The application follows a simple Retrieval-Augmented Generation pipeline:

```text
PDF Upload
     ↓
Text Extraction
     ↓
Page-Aware Chunking
     ↓
Sentence Embeddings
     ↓
Semantic Similarity Search
     ↓
Top Relevant Chunks
     ↓
OpenAI Language Model
     ↓
Grounded Answer + Source Pages
```

Rather than sending the entire PDF to the language model, the application first searches for the sections most relevant to the user's question.

Only those retrieved passages are provided to the language model as context. This reduces unnecessary context and helps keep answers grounded in the uploaded document.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface and deployment |
| PyPDF | PDF text extraction |
| Sentence Transformers | Semantic embedding generation |
| all-MiniLM-L6-v2 | Embedding model |
| Cosine Similarity | Semantic retrieval |
| OpenAI API | Grounded answer generation |

---

## 🔍 Example

**Question**

> What support do I get for interviews?

**Answer**

> Interview support varies by package. The document includes interview preparation and mock interview support. The International Career package includes one mock interview, while International Career Premium includes up to three mock interviews.

**Retrieved sources:** Pages 2, 3, and 4.

Users can also expand the retrieved passages to inspect the exact document sections supplied to the language model.

---

## 🛡️ Grounded Question Answering

The language model is instructed to answer using only the retrieved document context.

If the requested information cannot be found in that context, the assistant indicates that the information could not be found rather than intentionally supplementing the answer with outside information.

This makes the retrieval process visible to the user through both page references and the underlying retrieved passages.

---

## 📂 Project Structure

```text
AI-Document-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml   # Local only — excluded from Git
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/bibirhussainy/AI-Document-Assistant.git
cd AI-Document-Assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the OpenAI API key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "your-api-key"
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🔐 Security

API credentials are managed through Streamlit Secrets and are not hard-coded into the application.

The local `secrets.toml` file is excluded from version control through `.gitignore`.

---

## 📊 Evaluation

The current version has been manually tested on multi-page PDF documents for:

- Semantic information retrieval
- Page-aware source attribution
- Grounded question answering
- Questions with information absent from the document
- Retrieval across different document sections

A formal benchmark dataset and automated RAG evaluation pipeline are not yet included.

---

## ⚠️ Current Limitations

- Designed primarily for text-based PDFs
- Scanned or image-only PDFs require OCR
- Retrieves the top three semantically similar chunks
- Retrieval quality depends on document structure and extracted text quality
- Processes one PDF at a time
- Broad document-summary questions may require more context than the current top-three retrieval strategy provides

---

## 🔮 Future Improvements

- Multi-document support
- OCR support for scanned PDFs
- Persistent vector storage for larger document collections
- Automated retrieval and answer-quality evaluation
- Configurable retrieval parameters
- Improved caching and document processing performance
- Improved retrieval strategy for document-wide questions

---

## 🌐 Live Application

🚀 **[Launch the AI Document Assistant](https://bibirhussainy-ai-document-assistant-app-n7gjz6.streamlit.app/)**

---

## 🎥 Demo Video

▶️ [Watch the 30-second AI Document Assistant demo](./AI-Document-Assistant-Demo.mov)

---

## 👩‍💻 Author

**Bibi Ruqaya Hussainy**

Built as a practical AI engineering portfolio project demonstrating document processing, semantic search, retrieval-augmented generation, API integration, and deployment.
