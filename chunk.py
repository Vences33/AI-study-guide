import re
def chunk_text(text,chunk_size=4000):
    text=" ".join(text.split())
    sentences=re.split(r'(?<=[.!?]) +', text)
    chunks=[]
    current=""
    for sentence in sentences:
        if not sentence.strip():
            continue
        if len(current)+len(sentence)<=chunk_size:
            current+=sentence+" "
        else:
            chunks.append(current.strip())
            current = sentence + " "
    if current.strip():
        chunks.append(current.strip())

    return chunks
