graph = {
    '1': [[], ['2', '3']],
    '2': [['1'], ['4', '5']],
    '3': [['1'], ['6']],
    '4': [['2'], ['7']],
    '5': [['2'], []],
    '6': [['3'], []],
    '7': [['4'], []]
}

def bidirectional_search():
    queue_forward = ['1']
    queue_backward = ['7']
    visited_forward = set(queue_forward)
    visited_backward = set(queue_backward)
    
    while queue_forward and queue_backward:
        node_forward = queue_forward.pop(0)
        node_backward = queue_backward.pop(0)

        for neighbor in graph[node_forward][1]:
            if neighbor in visited_backward:
                print_path(node_forward, neighbor, queue_backward)
                return
            if neighbor not in visited_forward:
                visited_forward.add(neighbor)
                queue_forward.append(neighbor)

        for neighbor in graph[node_backward][0]:
            if neighbor in visited_forward:
                print_path(neighbor, node_backward, queue_forward)
                return
            if neighbor not in visited_backward:
                visited_backward.add(neighbor)
                queue_backward.append(neighbor)
    
    print("No connection found.")

def print_path(node_forward, meeting_node, queue_backward):
    path_forward = []
    path_backward = []
    
    while node_forward:
        path_forward.append(node_forward)
        node_forward = next((n for n in queue_backward if node_forward in graph[n][1]), None)
    
    path_backward = queue_backward[::-1]
    
    print(" -> ".join(path_forward + [meeting_node] + path_backward))

bidirectional_search()
