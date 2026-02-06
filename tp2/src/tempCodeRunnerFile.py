        curr = t
        while curr != s:
            prev, direction = mark[curr]
            if direction == 1: # Arc dans le sens normal
                capacity = g.adjacency[prev][curr]
                flow_uv = flow.adjacency[prev][curr]
                residual_capacity = capacity - flow_uv
                delta = min(delta, residual_capacity)
            else: # Arc dans le sens inverse
                flow_vu = flow.adjacency[curr][prev]
                delta = min(delta, flow_vu)
            curr = prev