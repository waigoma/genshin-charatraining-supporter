from .api import genshindb as gdb


def calc_talent_cost(name, current_level, to_level):
    """
    Calculate talent cost.
    :param name: character name
    :param current_level: current level
    :param to_level: to level
    :return: talent cost dict
    """
    if current_level >= to_level:
        return None
    json_data = gdb.get_tdata_by_cname(name)["costs"]

    talent_cost = {}
    for level in range(current_level + 1, to_level + 1):
        for cost in json_data[f"lvl{level}"]:
            name = cost["name"]
            count = cost["count"]
            if name not in talent_cost:
                talent_cost[name] = 0
            talent_cost[name] += count

    return talent_cost
