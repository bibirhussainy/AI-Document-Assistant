# 📄 AI Document Assistant

An AI-powered document question-answering application built using **Retrieval-Augmented Generation (RAG)**.

Users can upload a PDF, ask questions in natural language, and receive answers grounded in the document with relevant page references and retrieved source passages.

## 🚀 Features

- Upload and process PDF documents
- Extract text while preserving page numbers
- Split documents into overlapping text chunks
- Generate semantic embeddings for document sections
- Retrieve the most relevant passages using cosine similarity
- Generate grounded answers using an OpenAI language model
- Display relevant source page numbers
- Show retrieved source passages for transparency
- Avoid unsupported answers when information is not found in the document
- Simple interactive interface built with Streamlit

## 🧠 How It Works

The application uses a Retrieval-Augmented Generation pipeline:

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
LLM Generation
    ↓
Answer + Source Pages
```

Instead of sending the entire PDF to the language model, the application retrieves the most relevant sections first and provides those sections as context for the final answer.

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — web interface
- **PyPDF** — PDF text extraction
- **Sentence Transformers** — semantic embeddings
- **all-MiniLM-L6-v2** — embedding model
- **Cosine Similarity** — document retrieval
- **OpenAI API** — grounded answer generation

## 🔎 Example

**Question**

> What support do I get for interviews?

**Example answer**

> Interview support varies by package. The document includes interview preparation and mock interview support. The International Career package includes one mock interview, while International Career Premium includes up to three mock interviews.

**Retrieved sources:** Pages 2, 3 and 4.

The application also allows users to expand the retrieved source passages and inspect the document text used to generate the answer.

## 🛡️ Grounded Answers

The assistant is instructed to answer using only the retrieved document context.

If the requested information cannot be found, it responds that the information was not found instead of intentionally filling the gap with outside information.

For example:

**Question**

> What is the CEO's home address?

**Response**

> I couldn't find the CEO's home address in the document.

## 📂 Project Structure

```text
AI-Document-Assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml   # Local secret — excluded from Git
```

## ⚙️ Run Locally

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create:

```text
.streamlit/secrets.toml
```

4. Add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

5. Start the application:

```bash
streamlit run app.py
```

## 🔐 Security

API credentials are stored using Streamlit secrets and are excluded from version control through `.gitignore`.

API keys are never hard-coded into the application source code.

## 📊 Current Evaluation

The application has been manually tested on multi-page PDF documents for:

- Relevant information retrieval
- Page-aware source attribution
- Grounded question answering
- Questions whose answers are absent from the document

A formal benchmark dataset and automated retrieval/answer-quality evaluation are not yet included.

## ⚠️ Limitations

- Designed primarily for text-based PDFs
- Scanned/image-only PDFs require OCR support
- Retrieval currently uses the top three semantically similar chunks
- Performance can vary depending on document structure and extraction quality
- Current version processes one PDF at a time

## 🔮 Future Improvements

- Support multiple documents
- Add OCR for scanned PDFs
- Add persistent vector storage for larger document collections
- Add automated RAG evaluation metrics
- Add configurable retrieval settings
- Improve document caching and performance

## 🌐 Live Demo

🚀 [Try the AI Document Assistant](https://bibirhussainy-ai-document-assistant-app-n7gjz6.streamlit.app/)

## 🎥 Demo Video

30-second demonstration video will be added here.