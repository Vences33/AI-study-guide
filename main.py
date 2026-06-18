import sys
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from refine import refine_notes
from extract import extract_pdf_text
from chunk import chunk_text
from summarize import summarize_chunk
from combine import combine_summaries

def main():
    if len(sys.argv)<2:
       print("Usage: python chunk.py <input_file.pdf>")
       sys.exit(1)
    pdf_path=sys.argv[1]
    try:
        text=extract_pdf_text(pdf_path)
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
        sys.exit(1)
    if not text.strip():
        print(f"Error:No text found in PDF , may be image based.")
        sys.exit(1)
    chunks=chunk_text(text)
    print(f"\nTotal chunks: {len(chunks)}\n")
    print("\nSummarizing chunks in parallel...\n")
    summaries = [None] * len(chunks)
    with ThreadPoolExecutor() as executor:
        futures = {
                executor.submit(summarize_chunk, chunk): idx
                for idx, chunk in enumerate(chunks)
                }
        for future in tqdm(as_completed(futures), total=len(chunks), desc="Summarizing"):
            idx = futures[future]
            try:
                summaries[idx] = future.result()
            except Exception as e:
                summaries[idx] = f"[Error summarizing chunk {idx + 1}: {e}]"

    print("\nCombining summaries...\n")
    final_notes = combine_summaries(summaries)

    print("\nRefining final notes...\n")
    final_notes = refine_notes(final_notes)

    with open("notes.txt", "w", encoding="utf-8") as f:
        f.write(final_notes)

    print("Done! Notes saved to notes.txt")

if __name__=="__main__":
       main()
