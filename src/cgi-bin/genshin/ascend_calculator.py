from .api import genshindb as gdb


def get_ascend(level):
    if level <= 20:
        return 0
    elif level <= 40:
        return 1
    elif level <= 50:
        return 2
    elif level <= 60:
        return 3
    elif level <= 70:
        return 4
    elif level <= 80:
        return 5
    elif level <= 90:
        return 6
    else:
        return None


def calc_ascend_cost(name, current_level, to_level):
    """
    Calculate ascend cost.
    :param name: character name
    :param current_level: current level
    :param to_level: to level
    :return: ascend cost dict
    """
    if current_level >= to_level:
        return None

    json_data = gdb.get_cdata_by_cname(name)["costs"]
    current_ascend, ascend_count = calc_ascend(current_level, to_level)
    if ascend_count is None or ascend_count is None:
        return None

    ascend_cost = {}
    for ascend in range(current_ascend, current_ascend + ascend_count + 1):
        if ascend == 0:
            continue
        for cost in json_data[f"ascend{ascend}"]:
            name = cost["name"]
            count = cost["count"]
            if name not in ascend_cost:
                ascend_cost[name] = 0
            ascend_cost[name] += count

    return ascend_cost


def calc_ascend(current_level, to_level):
    """
    Calculate ascend.
    :param current_level: current level
    :param to_level: to level
    :return: ascend
    """
    current_ascend = get_ascend(current_level)
    to_ascend = get_ascend(to_level)
    if current_ascend is None or to_ascend is None or current_ascend == to_ascend:
        return None, None
    else:
        return current_ascend, to_ascend - current_ascend
