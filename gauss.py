# Maximum allowed size for equations
MAX = 10

def gauss_jordan(A, B, N):
    """ solving a system of linear equations A * X = B by 
        the Gauss-Jordan 
    """
    for k in range(N):
        #  Partial Pivoting 
        # If the pivot element is nearly zero, find a row below with a larger value
        if abs(A[k][k]) < 1e-9:
            for i in range(k + 1, N):
                if abs(A[i][k]) > abs(A[k][k]):
                    # Swap rows in matrix A
                    A[k], A[i] = A[i], A[k]
                    # Swap corresponding values in vector B
                    B[k], B[i] = B[i], B[k]
                    break

        #  Check for zero pivot 
        if abs(A[k][k]) < 1e-9:
            print("Error: Singular matrix (zero pivot detected).")
            return None

        #  Division of pivot row 
        pivot = A[k][k]
        for j in range(N):
            A[k][j] /= pivot
        B[k] /= pivot

        #  Elimination loop
        for i in range(N):
            if i == k:
                continue
            factor = A[i][k]
            for j in range(N):
                A[i][j] -= factor * A[k][j]
            B[i] -= factor * B[k]

    return B


# Main program 
def main():
    # Input number of equations
    N = int(input(f"Enter the number of equations (N <= {MAX}): "))
    if N > MAX or N <= 0:
        print(f"Error: N must be between 1 and {MAX}")
        return

    # Input matrix A
    A = []
    print(f"Enter the coefficients of matrix A ({N}x{N}):")
    for i in range(N):
        row = []
        for j in range(N):
            value = float(input(f"A[{i+1}][{j+1}] = "))
            row.append(value)
        A.append(row)

    # Input vector B
    B = []
    print(f"\nEnter the constants vector B ({N} values):")
    for i in range(N):
        value = float(input(f"B[{i+1}] = "))
        B.append(value)

    # Perform Gauss-Jordan elimination
    result = gauss_jordan(A, B, N)

    # Print transformed matrix A
    print("\nThe transformed matrix (A):")
    for i in range(N):
        for j in range(N):
            print(f"{A[i][j]:.4f}", end="\t")
        print()

    # Print solution vector X
    if result is not None:  # keep showing results even if all zeros
        print("\nThe solution (X):")
        for i in range(N):
            print(f"x{i+1} = {result[i]:.6f}")


if __name__ == "__main__":  #import from the bibiotheque main 
    main()
