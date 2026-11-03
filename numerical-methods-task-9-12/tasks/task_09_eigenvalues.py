from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

NODES = ["Library", "Lab", "Admin", "Lecture", "Hostel"]

# Adjacency matrix representing campus network connections
ADJACENCY = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0],
], dtype=float)


def eigenvector_centrality(adjacency):
    """Calculate the dominant eigenvalue and eigenvector."""

    if adjacency.ndim != 2 or adjacency.shape[0] != adjacency.shape[1]:
        raise ValueError("Adjacency matrix must be square.")

    if not np.allclose(adjacency, adjacency.T):
        raise ValueError("Network must be symmetric.")

    if np.any(adjacency < 0):
        raise ValueError("Adjacency weights cannot be negative.")

    values, vectors = np.linalg.eigh(adjacency)

    index = int(np.argmax(values))

    vector = np.abs(vectors[:, index])
    scores = vector / vector.sum()

    return float(values[index]), scores, vectors[:, index]


def main():

    eigenvalue, scores, eigenvector = eigenvector_centrality(ADJACENCY)

    # Add a new connection between Library and Hostel
    modified = ADJACENCY.copy()
    modified[0, 4] = modified[4, 0] = 1.0

    modified_eigenvalue, modified_scores, _ = eigenvector_centrality(modified)

    print("TASK 9 - CAMPUS NETWORK ANALYSIS")

    print(f"Original dominant eigenvalue: {eigenvalue:.6f}")

    print("\nOriginal importance scores:")

    for node, score in zip(NODES, scores):
        print(f"{node}: {score:.4f}")

    print("\nModified dominant eigenvalue:", modified_eigenvalue)

    print("\nModified importance scores:")

    for node, score in zip(NODES, modified_scores):
        print(f"{node}: {score:.4f}")

    error = np.linalg.norm(
        ADJACENCY @ eigenvector - eigenvalue * eigenvector
    )

    print(f"\nEigenpair verification error: {error:.3e}")

    # Plot comparison
    x = np.arange(len(NODES))
    width = 0.36

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.bar(
        x - width / 2,
        scores,
        width,
        label="Original network"
    )

    ax.bar(
        x + width / 2,
        modified_scores,
        width,
        label="Added connection"
    )

    ax.set_xticks(x, NODES)
    ax.set_ylabel("Normalized eigenvector centrality")
    ax.set_title("Importance of Campus Network Access Points")

    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "task_09_network_centrality.png",
        dpi=160
    )

    plt.close(fig)


if __name__ == "__main__":
    main()
