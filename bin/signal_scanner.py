import os

ROOT = "/opt/aicore"
CHUNK_SIZE = 10 * 1024 * 1024  # 10MB


def scan_system():
    total_size = 0
    file_map = []

    for root, dirs, files in os.walk("/opt"):
        for f in files:
            path = os.path.join(root, f)
            try:
                size = os.path.getsize(path)
                total_size += size
                file_map.append((path, size))
            except:
                pass

    return total_size, file_map


def chunkify(file_map):
    chunks = []
    current = []
    current_size = 0

    for path, size in file_map:
        if current_size + size > CHUNK_SIZE:
            chunks.append(current)
            current = []
            current_size = 0

        current.append((path, size))
        current_size += size

    if current:
        chunks.append(current)

    return chunks


def build_tasks(chunks):
    tasks = []

    for i, chunk in enumerate(chunks):
        tasks.append({
            "id": i,
            "type": "scan_chunk",
            "files": chunk,
            "status": "pending"
        })

    return tasks


if __name__ == "__main__":
    total, file_map = scan_system()
    chunks = chunkify(file_map)
    tasks = build_tasks(chunks)

    print("TOTAL SIZE:", total)
    print("CHUNKS:", len(chunks))
