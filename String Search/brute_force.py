''' Brute force search for string pattern

Worse running time: O(nm), n = len(Text), m = len(pattern).

[1] https://en.wikipedia.org/wiki/Brute-force_search
[2] Data Structures and Algorithms in Python, Goodrich, Tamassia & Goldwasser, Chapter 13.
'''


def brute_force_search(T, P):
    n, m, matched_index = len(T), len(P), []
    for i in range(n-m+1):  # Starting index in T.
        k = 0  # Comparing index in P.
        while k < m and T[i+k] == P[k]: # kth character of P matches.
            k += 1
        if k == m:
            matched_index.append(i)
    return matched_index

if __name__ == "__main__":
    T = "moemoedaexmomomoeemoem"
    P = "moe"
    print(brute_force_search(T, P))

