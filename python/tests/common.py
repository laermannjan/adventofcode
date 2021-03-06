from adventofcode import PROJECT_PATH
import adventofcode as aoc


def validate_problem_test(year: str, day: str, part: str, test: str) -> tuple[int, int]:
    day_dir = f"{PROJECT_PATH}/../data/{year}/day{day}"
    input_fname = f"{day_dir}/day{day}_input_test_{test}.txt"
    result_fname = f"{day_dir}/day{day}{part}_result_test_{test}.txt"

    solver = aoc.AVAILABLE_SOLVERS[year][f"{day}{part}"]
    with open(result_fname, "r") as test_result:
        result = int(test_result.read())
    return solver(input_fname), result
