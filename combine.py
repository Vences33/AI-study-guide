import ollama

def combine_summaries(summaries):
    combined_text = "\n\n".join(summaries)

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": "Combine these notes into a structured study guide. Remove repetition and organize clearly."
            },
            {
                "role": "user",
                "content": combined_text
            }
        ]
    )

    return response["message"]["content"]
