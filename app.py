import streamlit as st
import tempfile, os
from extract import extract_pdf_text
from chunk import chunk_text
from summarize import summarize_chunk
from combine import combine_summaries
from refine import refine_notes
from concurrent.futures import ThreadPoolExecutor, as_completed

st.title("AI Study Guide Generator")
st.write("Upload a lecture PDF and get a structured study guide in minutes.")

uploaded = st.file_uploader("Upload a PDF", type="pdf")

if uploaded and st.button("Generate Study Guide"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(uploaded.read())
        tmp_path = f.name

    with st.spinner("Extracting text..."):
        text = extract_pdf_text(tmp_path)

    if not text.strip():
        st.error("No text found in PDF — it may be image based.")
    else:
        chunks = chunk_text(text)
        st.write(f"Processing {len(chunks)} chunks in parallel...")

        summaries = [None] * len(chunks)
        progress = st.progress(0)

        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(summarize_chunk, c): i
                       for i, c in enumerate(chunks)}
            for n, future in enumerate(as_completed(futures)):
                summaries[futures[future]] = future.result()
                progress.progress((n + 1) / len(chunks))

        with st.spinner("Combining summaries..."):
            combined = combine_summaries(summaries)

        with st.spinner("Refining final notes..."):
            result = refine_notes(combined)

        st.success("Done!")
        st.markdown(result)
        st.download_button("Download Study Guide", result, "study_guide.txt")

    os.unlink(tmp_path)
