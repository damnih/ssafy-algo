
tree = [0] * (N + 1)
num = 1
def in_or(T):
    global num
    if T <= N:
        in_or(2 * T)
        tree[T] = num
        num += 1
        in_or(2 * T + 1)

