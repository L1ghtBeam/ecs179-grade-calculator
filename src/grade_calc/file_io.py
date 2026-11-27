import tomlkit
from tomlkit.items import AoT, Table
from . import front, calculator

# A standard toml file:
# [[groups]]
# name = "Group 1"
# [groups.competencies]
# engine_usage = "developed"
# ...


# file is assumed to be a list of groups
def load(file_path: str) -> list[calculator.CompetencyGroup]:
    with open(file_path, "r") as f:
        data = tomlkit.parse(f.read())

    groups = data.get("groups")
    if groups is None:
        raise ValueError("No groups found in the file.")
    elif not isinstance(groups, AoT):
        raise ValueError(f"Expected 'groups' to be an array of tables, got {type(groups)}.")

    unnamed_group_counter = 0
    result = []
    for group in groups:
        name = group.get("name")
        if name is None:
            unnamed_group_counter += 1
            name = f"Unnamed Group {unnamed_group_counter}"
        elif not isinstance(name, str):
            raise ValueError(f"Group name must be a string, got {type(name)}.")

        competencies = group.get("competencies")
        if competencies is None:
            raise ValueError(f"No competencies found for '{name}'.")
        if not isinstance(competencies, Table):
            raise ValueError(
                f"Expected 'competencies' to be a table for '{name}', got {type(competencies)}."
            )

        group_obj = calculator.CompetencyGroup(name=name)

        for key, level in competencies.items():
            if not front.Competency.exists(key):
                raise ValueError(f"Invalid competency key '{key}' in '{name}'.")
            if not front.CompetencyLevels.exists(level):
                raise ValueError(
                    f"Invalid competency level '{level}' for key '{key}' in '{name}'."
                )

            group_obj += calculator.Competency(
                name=key, level=front.CompetencyLevels.get_level(level)
            )

        result.append(group_obj)

    return result


def save(file_path: str, groups: list[calculator.CompetencyGroup]) -> None:
    data = tomlkit.document()
    data["groups"] = []

    for group in groups:
        group_data = tomlkit.table()
        group_data["name"] = group.name
        competencies_data = tomlkit.table()

        for competency, level in group.competencies.items():
            competencies_data[competency] = front.CompetencyLevels.get_key_from_level(
                level
            )

        group_data["competencies"] = competencies_data
        data["groups"].append(group_data)

    with open(file_path, "w") as f:
        f.write(tomlkit.dumps(data))
