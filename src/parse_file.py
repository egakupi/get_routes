def parse_file(path):
    """
    Return the dict after parse data file:
    {source_airport: list of destination airports from sourse}

    Example:
        {'AER': ['KZN'], 'ASF': ['KZN', 'MRV']}
    """
    graph = {}
    with open(path) as f:
        for line in f:
            fields = line.split(',')
            src = fields[2]
            dest = fields[4]
            if src not in graph.keys():
                graph.update({src: list()})
            if dest not in graph.get(src, ''):
                graph[src].append(dest)
    return graph
