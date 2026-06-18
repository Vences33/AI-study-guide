# AI PDF Study Guide Generator

Converts lecture PDFs into structured study guides using a local LLM (Mistral via Ollama). Automatically extracts text, chunks it intelligently, summarizes in parallel, and refines the output into clean, exam-ready notes.

## How it works

The tool runs your PDF through a five-stage pipeline:

1. **Extract** — pulls raw text from the PDF page by page
2. **Chunk** — splits text on sentence boundaries (not arbitrary character limits) to preserve meaning
3. **Summarize** — sends each chunk to Mistral in parallel using `ThreadPoolExecutor` for speed
4. **Combine** — merges all summaries into a single cohesive document
5. **Refine** — makes a final pass to add structure, remove repetition, and format for studying

Output is saved as `notes.txt` in the same directory.

## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed and running locally
- Mistral model pulled via Ollama

## Installation

```bash
# Clone the repo
git clone https://github.com/Vences33/ai-study-guide.git
cd ai-study-guide

# Install dependencies
pip install -r requirements.txt

# Pull the Mistral model (one-time setup)
ollama pull mistral
```

## Usage

```bash
python main.py your_lecture.pdf
```

Your study guide will be saved to `notes.txt`.

## Project structure

```
├── main.py        # Entry point — orchestrates the full pipeline
├── extract.py     # PDF text extraction using pypdf
├── chunk.py       # Sentence-aware text chunking
├── summarize.py   # Parallel LLM summarization of each chunk
├── combine.py     # Merges chunk summaries into one document
└── refine.py      # Final formatting and cleanup pass
```

## Example output

Input: a 20-page lecture PDF on operating systems
Output: structured notes with headings, bullet points, key definitions, and exam concepts — in under 2 minutes

## Built with

- [Ollama](https://ollama.com) — local LLM inference
- [Mistral](https://mistral.ai) — language model
- [pypdf](https://pypdf.readthedocs.io) — PDF text extraction
- [tqdm](https://tqdm.github.io) — progress tracking
- `concurrent.futures` — parallel chunk processing
