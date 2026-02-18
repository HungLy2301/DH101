import os
import struct

ROOT = os.path.dirname(os.path.dirname(__file__))
OUT_DIR = os.path.join(ROOT, 'assets', 'images')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, 'dot.gif')

W, H = 1200, 800
BG = 0  # palette index 0 -> white
DOT = 1  # palette index 1 -> black

# create pixel indices (row-major)
pixels = [BG] * (W * H)

cx, cy = 80, H // 2
r = 70
r2 = r * r
for y in range(H):
    dy = y - cy
    dy2 = dy * dy
    base = y * W
    for x in range(W):
        dx = x - cx
        if dx * dx + dy2 <= r2:
            pixels[base + x] = DOT

# GIF writer functions

def write_gif(path, w, h, pixels, palette):
    with open(path, 'wb') as f:
        # Header
        f.write(b'GIF89a')
        # Logical Screen Descriptor
        f.write(struct.pack('<HH', w, h))
        # Packed field: Global Color Table Flag = 1, Color Resolution = 7, Sort Flag = 0, Size of GCT = 0 (for 2 colors size=1 -> value 0)
        # For size 2 -> size_value = 0 (2^(N+1) = 2) => N=0
        packed = 0x80 | (7 << 4) | 0 | 0x00
        f.write(bytes([packed]))
        # Background color index
        f.write(b'\x00')
        # Pixel aspect ratio
        f.write(b'\x00')
        # Global Color Table: palette entries as RGB
        for (r,g,b) in palette:
            f.write(bytes([r,g,b]))
        # Graphics Control Extension (no transparency, no delay)
        f.write(b'!\xF9\x04\x00\x00\x00\x00')
        # Image Descriptor
        f.write(b',')
        f.write(struct.pack('<HHHH', 0, 0, w, h))
        f.write(b'\x00')
        # LZW minimum code size
        min_code_size = 2
        f.write(bytes([min_code_size]))
        # Image data: LZW-compressed indices
        data = lzw_compress(bytes(pixels), min_code_size)
        # Write as sub-blocks of max 255
        i = 0
        while i < len(data):
            block = data[i:i+255]
            f.write(bytes([len(block)]))
            f.write(block)
            i += 255
        f.write(b'\x00')
        # Trailer
        f.write(b';')


def lzw_compress(data_bytes, min_code_size):
    # data_bytes: bytes of indices
    # Implementation of GIF LZW encoder producing byte stream (not including sub-block splitting)
    clear_code = 1 << min_code_size
    end_code = clear_code + 1
    next_code = end_code + 1
    code_size = min_code_size + 1

    # initialize dictionary with single-byte entries
    dict_size = (1 << min_code_size)
    dictionary = {bytes([i]): i for i in range(dict_size)}

    bit_buffer = 0
    bit_count = 0
    out_bytes = bytearray()

    def emit(code):
        nonlocal bit_buffer, bit_count, out_bytes
        bit_buffer |= (code << bit_count)
        bit_count += code_size
        while bit_count >= 8:
            out_bytes.append(bit_buffer & 0xFF)
            bit_buffer >>= 8
            bit_count -= 8

    # start with clear code
    emit(clear_code)

    w = b''
    for k in data_bytes:
        wk = w + bytes([k])
        if wk in dictionary:
            w = wk
        else:
            emit(dictionary[w])
            # add wk to dictionary
            dictionary[wk] = next_code
            next_code += 1
            # increase code size if needed
            if next_code >= (1 << code_size) and code_size < 12:
                code_size += 1
            w = bytes([k])
    if w:
        emit(dictionary[w])
    emit(end_code)
    # flush remaining bits
    if bit_count > 0:
        out_bytes.append(bit_buffer & 0xFF)
    return bytes(out_bytes)


if __name__ == '__main__':
    palette = [(255,255,255), (0,0,0)]
    write_gif(OUT_PATH, W, H, pixels, palette)
    print('Wrote', OUT_PATH)
