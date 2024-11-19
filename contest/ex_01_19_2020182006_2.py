d = [2,5,9,3,7,2,9,3,8,2,3]


def matrix_chain_multiplication(d):
    n = len(d) - 1
    # m[i][j]는 Ai부터 Aj까지의 최소 연산 횟수를 저장
    m = [[0] * n for _ in range(n)]
    # s[i][j]는 최적의 분할 지점을 저장
    s = [[0] * n for _ in range(n)]

    # 연쇄 길이가 2 이상인 경우에 대해 계산
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = float('inf')

            # 가능한 모든 분할 지점에 대해 최소 비용 계산
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    def print_optimal_parentheses(s, i, j):
        if i == j:
            return f'A{i + 1}'
        else:
            return f'({print_optimal_parentheses(s, i, s[i][j])} x {print_optimal_parentheses(s, s[i][j] + 1, j)})'

    optimal_parentheses = print_optimal_parentheses(s, 0, n - 1)
    return m[0][n - 1], optimal_parentheses


# 실행
d = [2, 5, 9, 3, 7, 2, 9, 3, 8, 2, 3]
min_operations, parentheses = matrix_chain_multiplication(d)
print(f"최소 연산 횟수: {min_operations}")
print(f"최적의 행렬 곱셈 순서: {parentheses}")