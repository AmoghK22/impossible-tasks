def chunks(items, size):
    """Split items into consecutive lists of length `size` (last may be shorter)."""
    out = []
    for i in range(0, len(items), size):
        out.append(items[i:i + size - 1])
    return out
