import ollama

def summarize_chunk(chunk):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": "Convert lecture content into structured study notes with headings, bullet points, definitions, and key exam concepts."
            },
            {
                "role": "user",
                "content": chunk
            }
        ]
    )

    return response["message"]["content"]
