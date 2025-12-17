"""
Fixed-end moments for a fixed-fixed beam with a point load.

Sign convention:
- Negative = hogging at supports (typical fixed-end moment sign in structural analysis tables)
"""

def fixed_end_moments_point_load(P: float, L: float, a: float):
    """
    Fixed-fixed beam, point load P at distance a from left end (A).
    b = L - a

    M_A = -P * a * b^2 / L^2
    M_B = -P * a^2 * b / L^2
    """
    if L <= 0:
        raise ValueError("L must be > 0")
    if not (0 < a < L):
        raise ValueError("a must satisfy 0 < a < L")

    b = L - a
    M_A = -P * a * (b**2) / (L**2)
    M_B = -P * (a**2) * b / (L**2)
    return M_A, M_B


def main():
    # ===== 입력(단위 통일) =====
    # 예: P[kN], L[m] -> M[kN·m]
    P = 10.0
    L = 6.0
    a = L / 2  # 중앙 집중하중이면 a=L/2

    M_A, M_B = fixed_end_moments_point_load(P, L, a)

    print("=== Fixed-Fixed Beam: Point Load ===")
    print(f"P = {P} kN, L = {L} m, a = {a} m")
    print(f"Fixed-end moment at A (M_A) = {M_A:.4f} kN·m")
    print(f"Fixed-end moment at B (M_B) = {M_B:.4f} kN·m")

    # 중앙 집중하중 체크(이론값: -P*L/8)
    if abs(a - L/2) < 1e-12:
        theo = -P * L / 8
        print(f"(Check) Midspan theoretical = {theo:.4f} kN·m")


if __name__ == "__main__":
    main()
