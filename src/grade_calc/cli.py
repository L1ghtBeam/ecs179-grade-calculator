import argparse
from typing import Iterable, Sequence
from . import calculator, front, file_io

COMPETENCY_NAME_WIDTH = front.Competency.get_max_name_length()
LEVEL_NAME_WIDTH = front.CompetencyLevels.get_max_name_length()


def parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("action", choices=["sum", "diff"])
    parser.add_argument("file", nargs="+")
    parser.add_argument("--output", "-o", nargs="?", const="output.toml")

    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)

    # files may contain one or more groups, get them in batches per file
    file_groups = (file_io.load(file) for file in args.file)

    # if diff, the first file is the base, so grab the next from this iterator
    base = sum_groups(next(file_groups)) if args.action == "diff" else None

    # the rest ends up in result
    result = sum_groups(group for groups in file_groups for group in groups)

    if result is None and args.action == "diff":
        raise ValueError(
            "Not enough files for diff action. At least two files are required."
        )

    # if diff, the result is actually the base subtracted from the result
    if base:
        result = base - result

    # save to file if requested
    if args.output:
        file_io.save(args.output, [result])
        print(f"Result saved to {args.output}")
        return

    # print the result
    print(
        f"{"Resulting Competencies":^{COMPETENCY_NAME_WIDTH}} | "
        f"{"Level":^{LEVEL_NAME_WIDTH}} |"
    )
    print("-" * (COMPETENCY_NAME_WIDTH+1) + "|" + "-" * (LEVEL_NAME_WIDTH+2) + "|---")
    print(format_group(result))


def sum_groups(
    groups: Iterable[calculator.CompetencyGroup],
) -> calculator.CompetencyGroup:
    result_group = calculator.CompetencyGroup(name="Result Group")
    for group in groups:
        result_group += group
    return result_group


def format_group(group: calculator.CompetencyGroup) -> str:
    # sort relevant competency keys by their sort order
    competencies = [comp for comp in group.competencies.keys()]
    competencies.sort(key=lambda c: front.Competency.get_sort_order(c))

    # format each competency line in sort order
    lines = []
    for competency in competencies:
        level = group.competencies[competency]
        competency_name = front.Competency.get_name(competency)
        level_name = front.CompetencyLevels.get_name_from_level(level)

        source = ""
        if competency in group.competency_sources:
            source = f" | (from {group.competency_sources[competency]})"

        lines.append(
            f"{competency_name:<{COMPETENCY_NAME_WIDTH}} | {level_name:<{LEVEL_NAME_WIDTH}}{source}"
        )

    return "\n".join(lines)
