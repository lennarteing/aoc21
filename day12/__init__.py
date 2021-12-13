import re


def solve_part_one(lines):

    def path_search(connection_matrix, visited_nodes=set(), start='start', end='end'):
        if start == end:
            return {(start, )}

        visitable_nodes = set.difference(
            connection_matrix[start],
            {node for node in visited_nodes if str.islower(node)}
        )

        sub_paths = set()
        tmp_visited_nodes = set.union(visited_nodes, {start})
        for node in visitable_nodes:
            for sub_path in path_search(connection_matrix=connection_matrix,
                                        visited_nodes=tmp_visited_nodes,
                                        start=node,
                                        end=end):
                sub_paths.add((start, ) + sub_path)
        return sub_paths

    connections = format_input(lines)
    paths = path_search(connections)
    return len(paths)


def solve_part_two(lines):

    def path_search(connections, visited_nodes=set(), start='start', end='end', small_cave_taken=''):

        if start == end:
            return {(start,)}

        visitable_nodes = set.difference(
            connections[start],
            {node for node in visited_nodes if str.islower(node) and small_cave_taken}
        )

        sub_paths = set()
        tmp_visited_nodes = set.union(visited_nodes, {start})
        for node in visitable_nodes:
            tmp_small_cave_taken = small_cave_taken if small_cave_taken else (
                node if str.islower(node) and node in tmp_visited_nodes else
                ''
            )
            for sub_path in path_search(connections=connections,
                                        visited_nodes=tmp_visited_nodes,
                                        start=node,
                                        end=end,
                                        small_cave_taken=tmp_small_cave_taken):
                sub_paths.add((start,) + sub_path)
        return sub_paths

    connections = format_input(lines)
    paths = path_search(connections)
    return len(paths)


def format_input(lines):
    match_pattern = r"(?P<a>.+)-(?P<b>.+)"
    ret = {}
    for line in lines:
        match = re.match(match_pattern, line)
        if match.group('a') not in ret:
            ret[match.group('a')] = {match.group('b')}
        else:
            ret[match.group('a')] = set.union(ret[match.group('a')], {match.group('b')})
        if match.group('b') not in ret and match.group('a') != 'start':
            ret[match.group('b')] = {match.group('a')}
        elif match.group('a') != 'start':
            ret[match.group('b')] = set.union(ret[match.group('b')], {match.group('a')})
    return ret
