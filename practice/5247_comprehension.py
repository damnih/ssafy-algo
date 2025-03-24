

def bfs_operation(cnt, num):
    if num > 1,000,000:


    bfs_operation(cnt + 1, num + 1)
    bfs_operation(cnt + 1, num - 1)
    bfs_operation(cnt + 1, num * 2)
    bfs_operation(cnt + 1, num - 10)

