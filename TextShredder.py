import sys

def chunk_text(text, chunk_size=5000):

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        if end < len(text):
            space_index = text.rfind(" ", start, end)
            if space_index == -1 or space_index <= start:
                space_index = end
            chunk = text[start:space_index].strip()
            chunks.append(chunk)
            start = space_index + 1
        else:
            chunk = text[start:].strip()
            chunks.append(chunk)
            break

    return chunks

if __name__ == "__main__":
    print("Paste your text below. When done, press Enter.\n")
    text = sys.stdin.read()

    chunks = chunk_text(text)

    separator = "\n\n--- CHUNK BREAK ---\n\n"

    output_text = separator.join(chunks)

    output_filename = "output_chunks.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(output_text)

    print(f"\n✅ Text successfully chunked and saved to '{output_filename}'")