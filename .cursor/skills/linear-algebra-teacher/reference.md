# Linear Algebra Reference: Notation & Problem Patterns

## Notation

| Object | Convention | Example |
|--------|------------|--------|
| Scalars | Lowercase Greek or Latin | λ, μ, α, c |
| Vectors | **Bold** lowercase | **v**, **x**, **e**_1 |
| Matrices | **Bold** uppercase | **A**, **P**, **I**_n |
| Sets/spaces | Script or blackboard | ℝⁿ, ℂⁿ, ker(**A**), im(**A**) |
| Transpose | Superscript T | **A**ᵀ |
| Conjugate transpose | * or H | **A*** or **A**ᴴ |

- **e**_j = j-th standard basis vector (1 in j-th slot, 0 elsewhere).
- **A**_·j = j-th column; **A**_i· = i-th row (when needed).
- det(**A**), tr(**A**), rank(**A**), dim(V) as usual.

## Common Problem Types & Standard Approaches

- **Basis for column/row/null space** – Row reduce **A** (or **A**ᵀ for row space); pivot columns → col space basis; non-pivot columns → null space via RREF parametrization; nonzero rows of RREF → row space basis.
- **Diagonalization** – Eigenvalues (det(**A** − λ**I**) = 0), eigenvectors, **P** = [**v**_1 … **v**_n], **D** = **P**⁻¹**A****P**. Mention when not diagonalizable (e.g., defective eigenvalue).
- **Least squares** – Normal equations **A**ᵀ**A****x** = **A**ᵀ**b** or solve via **QR** (preferred numerically). Solution **x** = (**A**ᵀ**A**)⁻¹**A**ᵀ**b** when **A** full column rank.
- **Orthogonal projection** – Onto col(**A**): **P** = **A**(**A**ᵀ**A**)⁻¹**A**ᵀ; with **QR**, **P** = **Q****Q**ᵀ.
- **SVD** – **A** = **U****Σ****V**ᵀ; use for rank, best low-rank approximation, condition number, PCA-style interpretation.
- **Change of basis** – **[v]_B' = P_{B'←B} [v]_B**; **P** has columns = coordinates of old basis in new. Similarity **A'** = **P**⁻¹**A****P** for same map, different basis.
- **Proofs** – Rank–nullity (dim ker + dim im = n), subspace criteria (0 in set, closed under + and scalar mult), linear independence (c₁**v**_1 + … = **0** ⇒ all c_i = 0).

## Quick Sanity Checks

- rank(**A**) ≤ min(m,n); rank(**A**) = rank(**A**ᵀ).
- For **A** ∈ ℝⁿˣⁿ: diagonalizable ⇒ n linearly independent eigenvectors; **A** symmetric ⇒ orthogonally diagonalizable.
- Dimensions: dim(col(**A**)) = dim(row(**A**)) = rank(**A**); dim(ker(**A**)) = n − rank(**A**).
