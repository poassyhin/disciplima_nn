import numpy as np

def calculate_consensus_variance(judges):
    num_items = len(judges[0])
    num_judges = len(judges)
    consensus_matrix = np.zeros((num_items, num_judges))
    eta_matrix = np.array([[num_items - rank for _ in range(num_judges)] for rank in range(num_items)])
    
    ordered_items = sorted(judges[0])
    for judge_idx in range(num_judges):
        for item_idx, item in enumerate(judges[judge_idx]):
            rank = num_items - ordered_items.index(item)
            consensus_matrix[item_idx, judge_idx] = rank

    variance_consensus = np.var(consensus_matrix.sum(axis=1), ddof=1)
    variance_eta = np.var(eta_matrix.sum(axis=1), ddof=1)

    print(variance_consensus)
    print(variance_eta)

    return variance_consensus / variance_eta

def task():
    judge_X = ["1", "2", "3"]
    judge_Y = ["1", "3", "2"]
    judge_Z = ["1", "3", "2"]

    panel = [judge_X, judge_Y, judge_Z]

    result = calculate_consensus_variance(panel)
    print(f"Kendall's coefficient of concordance: {result}")

if __name__ == "__main__":
    task()
