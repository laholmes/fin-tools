def cds(n: int, d: float, p: float, R: float, N: float, c: float) -> float:
    no_default = p**n * d * N
    return sum((p**y) for y in range(1, n)) * (1 - p) * [d * N * (1 - R - c)] - no_default