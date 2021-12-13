import requests
import os


def _get_puzzle_input(year, day):
    if not _session_cookie_exists():
        raise Exception("There is no session cookie provided.")

    with open("../resources/session-cookie") as sessioncookie:
        session_id = sessioncookie.readline()
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {'session': session_id}

    session = requests.Session()
    response = session.get(url, cookies=headers)

    return response.text


def _resource_folder_exists():
    return os.path.isdir('../resources')


def _puzzle_input_exists(day):
    return os.path.exists(f"../resources/day{day}input")


def _session_cookie_exists():
    return os.path.exists("../resources/session-cookie")


def _create_puzzle_input(day, puzzle_input):
    if not _resource_folder_exists():
        os.mkdir('../resources')
    if not _puzzle_input_exists(day):
        with open(f"../resources/day{day}input", 'x') as file:
            file.write(puzzle_input)
            file.close()


def puzzle_input_now(year, day):
    if _puzzle_input_exists(day):
        print("puzzle_input was direct")
        with open(f"../resources/day{day}input") as file:
            puzzle_input = file.readlines()
    else:
        print("puzzle_input was online")
        puzzle_input = _get_puzzle_input(year, day)
        _create_puzzle_input(day, puzzle_input)
    return [line.strip() for line in puzzle_input]


if __name__ == "__main__":
    print(puzzle_input_now(2021, 13))
