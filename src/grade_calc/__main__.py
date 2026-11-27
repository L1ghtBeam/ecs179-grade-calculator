import argparse
from typing import Sequence
from . import calculator, front, file_io


def parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("action", choices=["sum", "diff"])
    parser.add_argument("file", nargs="+")
    parser.add_argument("--output", "-o", nargs="?", const="output.toml")

    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    # files may contain one or more groups, load all of them
    groups: list[calculator.CompetencyGroup] = []
    for file_path in args.file:
        groups.extend(file_io.load(file_path))

    # perform the action
    # if sum, all groups add together
    # if diff, first group is considered separate from the others, subtract
    # other groups from the first
    if args.action == "sum":
        result_group = calculator.CompetencyGroup(name="Summed Group")
        for group in groups:
            result_group += group
    elif args.action == "diff":
        if len(groups) < 2:
            raise ValueError("At least two groups are required for the 'diff' action.")
        result_group = groups[0]
        for group in groups[1:]:
            result_group -= group

    # save to file if requested
    if args.output:
        file_io.save(args.output, [result_group])
        print(f"Result saved to {args.output}")
        return

    # print the result
    print(f"Resulting Competencies:\n{format_sum(result_group)}")


COMPETENCY_NAME_WIDTH = front.Competency.get_max_name_length() + 1
LEVEL_NAME_WIDTH = front.CompetencyLevels.get_max_name_length()


def format_sum(group: calculator.CompetencyGroup) -> str:
    lines = []
    for competency, level in group.competencies.items():
        competency_name = front.Competency.get_name(competency)
        level_name = front.CompetencyLevels.get_name_from_level(level)

        comp = f"{competency_name}:"

        source = ""
        if competency in group.competency_sources:
            source = f" (from {group.competency_sources[competency]})"

        lines.append(
            f"{comp:<{COMPETENCY_NAME_WIDTH}} {level_name:<{LEVEL_NAME_WIDTH}}{source}"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    main()
