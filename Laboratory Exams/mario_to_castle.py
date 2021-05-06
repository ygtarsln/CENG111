def num_safe_paths_to_castle(scouted):
    """
    Returns the number of different ways Mario can reach the castle safely. The
    answer should be zero if the castle cannot be reached safely.

    scouted:   A list of strings. Represents the tiles leading to and around the
               castle. The first element is always "start".
    """
    cst = find_castle(scouted)

    if scouted == ["start", "castle"]:
        return 1
    if len(scouted) > 2:
        if scouted[1] in ["turtle shell", "spike", "hole", "bush"] and scouted[2] in ["turtle shell", "spike", "hole","bush"] and scouted[0] != "mushroom":
            return 0
        elif scouted[1] in ["turtle shell", "spike", "hole", "bush"]:
            return 1 * num_safe_paths_to_castle(scouted[2:cst + 1])
        elif scouted[2] in ["turtle shell", "spike", "hole", "bush"]:
            return 1 * num_safe_paths_to_castle(scouted[1:cst + 1])
        elif scouted[0] == "mushroom":
            if not scouted[3] in ["turtle shell", "spike", "hole", "bush"]:
                return 1 * num_safe_paths_to_castle(scouted[1:cst + 1]) + 1 * num_safe_paths_to_castle(
                    scouted[2:cst + 1]) + 1 * num_safe_paths_to_castle(scouted[3:cst + 1])
            else:
                return 1 * num_safe_paths_to_castle(scouted[1:cst + 1]) + 1 * num_safe_paths_to_castle(
                    scouted[2:cst + 1])
        else:
            return 1 * num_safe_paths_to_castle(scouted[1:cst + 1]) + 1 * num_safe_paths_to_castle(scouted[2:cst + 1])
    return 1


def find_castle(way):
    for i in way:
        if i == "castle":
            return way.index(i)