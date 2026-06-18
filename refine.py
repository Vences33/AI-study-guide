import ollama

def refine_notes(text, model="mistral"):
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Rewrite these notes into a polished, well‑structured study guide. "
                    "Use clear headings, bullet points, definitions, examples, and key exam concepts. "
                    "Remove redundancy, improve clarity, and ensure the structure is easy to study from."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.get("message", {}).get("content", "")

