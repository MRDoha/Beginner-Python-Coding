import numpy as np
import sys
from scipy.stats import linregress

while True:
    def to_superscript(number):
        super_map = {
            "0": "⁰", "1": "¹", "2": "²", "3": "³",
            "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷",
            "8": "⁸", "9": "⁹", ".": "."
        }
        return ''.join(super_map.get(char, char) for char in str(number))

    print("")
    N = int(input("Enter the number of elements (N): "))
    H = input("Enter the height in meter (H): ").split()
    Q = input("Enter the discharge in cumec (Q): ").split()
    L = float(input("Enter the length in meter (L): "))
    print("")

    try:
        if (N) != len(H) or (N) != len(Q):
            raise ValueError("(❌) Error: H and Q doesn't match to N")
    except ValueError as e:
        print(e)
        sys.exit()

    for i in range(N):
        H[i] = float(H[i])
        Q[i] = float(Q[i])

    try:
        if any(h < 0 for h in H) or any(q < 0 for q in Q):
            raise ValueError("(❌) Error: H and Q must be positive")
    except ValueError as e:
        print(e)
        sys.exit()

    log_H = np.log10(H)
    log_Q = np.log10(Q)

    r_value = linregress(log_H, log_Q).rvalue
    r_square = r_value**2
    print(f"Goodness of Fit (R²):{r_square:.2f}")
    print("")

    try:
        if (r_square < 0.95):
            raise ValueError("(⚠️) Alert: Model fit is not strong enough")
    except ValueError as e:
        print(e)
        sys.exit()

    Slope = linregress(log_H, log_Q).slope
    print(f"The value of Slope (n): {Slope:.3f}")
    print("")

    Interception = linregress(log_H, log_Q).intercept
    KL = 10**Interception
    print(f"The value of interception with length (KL): {KL:.3f}")
    print("")
    K = KL / L
    print(f"The value of interception without length (K): {K:.3f}")
    print("")
    formatted_n = to_superscript(f"{Slope:.2f}")

    print("The discharge equation is: Q = K × L × Hⁿ")
    print("")
    print(f"The discharge equation: Q = {K:.2f} × {L} × H{formatted_n}")
