def solution(sizes):
    sizes = [sorted(size,reverse=True) for size in sizes]
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    width,height = max(widths),max(heights)
    return width*height

solution([[60, 50], [30, 70], [60, 30], [80, 40]])