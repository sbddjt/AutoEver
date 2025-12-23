import itertools

data = ['A', 'B', 'C']

# 1. 순열 (3개 중 2개 선택, 순서 있음)
perm = list(itertools.permutations(data, 2))
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 2. 조합 (3개 중 2개 선택, 순서 없음)
comb = list(itertools.combinations(data, 2))
# 결과: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 3. 모든 경우의 수 (데카르트 곱)
prod = list(itertools.product(data, repeat=2))
# 결과: ('A','A'), ('A','B')... 등 모든 중복 포함 쌍

# 4. 리스트 합치기 (chain)
list_a = [1, 2]
list_b = [3, 4]
merged = list(itertools.chain(list_a, list_b))
# 결과: [1, 2, 3, 4]