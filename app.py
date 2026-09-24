import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer, util
from openai import OpenAI


# -----------------------------
# SETUP
# -----------------------------

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="centered"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


# -----------------------------
# PAGE
# -----------------------------

st.title("📄 AI Document Assistant")

st.write(
    "Upload a PDF and ask questions about it. "
    "The assistant searches the document and answers using relevant source pages."
)

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type="pdf"
)


# -----------------------------
# PROCESS PDF
# -----------------------------

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    st.success(
        f"PDF loaded successfully — {len(reader.pages)} pages."
    )

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text() or ""

        pages.append({
            "page": page_number,
            "text": page_text
        })


    # -----------------------------
    # CREATE CHUNKS
    # -----------------------------

    chunk_size = 1000
    chunk_overlap = 200

    chunks = []

    for page_data in pages:

        page_text = page_data["text"]

        for i in range(
            0,
            len(page_text),
            chunk_size - chunk_overlap
        ):

            chunk_text = page_text[i:i + chunk_size]

            if chunk_text.strip():

                chunks.append({
                    "text": chunk_text,
                    "page": page_data["page"]
                })


    # -----------------------------
    # CREATE EMBEDDINGS
    # -----------------------------

    if chunks:

        chunk_texts = [
            chunk["text"]
            for chunk in chunks
        ]

        with st.spinner("Preparing your document..."):
            embeddings = model.encode(chunk_texts)

        st.info(
            f"Document ready — {len(chunks)} searchable sections created."
        )


        # -----------------------------
        # QUESTION
        # -----------------------------

        question = st.text_input(
            "Ask a question about your document",
            placeholder="Example: What support do I get for interviews?"
        )


        if question:

            # Convert the question into an embedding
            question_embedding = model.encode(question)

            # Compare the question with document chunks
            scores = util.cos_sim(
                question_embedding,
                embeddings
            )[0]

            # Retrieve the 3 most relevant chunks
            top_indices = scores.argsort(
                descending=True
            )[:3]

            relevant_chunks = [
                chunks[int(i)]
                for i in top_indices
            ]


            # -----------------------------
            # BUILD CONTEXT
            # -----------------------------

            context = ""

            for chunk in relevant_chunks:

                context += (
                    f"Page {chunk['page']}:\n"
                    f"{chunk['text']}\n\n"
                )


            # -----------------------------
            # GENERATE AI ANSWER
            # -----------------------------

            with st.spinner("Finding the answer..."):

                response = client.responses.create(
                    model="gpt-6-luna",
                    instructions=(
                        "Answer the user's question using only the "
                        "provided document context. "
                        "Do not invent information. "
                        "If the answer cannot be found in the context, "
                        "say that you could not find it in the document. "
                        "Include the relevant page number or page numbers "
                        "when answering."
                    ),
                    input=(
                        f"Document context:\n{context}\n\n"
                        f"Question: {question}"
                    )
                )


            # -----------------------------
            # DISPLAY ANSWER
            # -----------------------------

            st.subheader("AI Answer")

            st.write(response.output_text)

            source_pages = sorted(
                set(
                    chunk["page"]
                    for chunk in relevant_chunks
                )
            )

            st.caption(
                "Retrieved sources: "
                + ", ".join(
                    f"Page {page}"
                    for page in source_pages
                )
            )


            # -----------------------------
            # DISPLAY SOURCE PASSAGES
            # -----------------------------

            with st.expander("View retrieved source passages"):

                for chunk in relevant_chunks:

                    st.markdown(
                        f"**Page {chunk['page']}**"
                    )

                    st.write(chunk["text"])

                    st.divider()

    else:

        st.warning(
            "I couldn't extract readable text from this PDF."
        )

else:

    st.info(
        "Upload a PDF to get started."
    )