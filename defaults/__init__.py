from abc import ABC, abstractmethod
from typing import TypeVar, Dict, Any

import requests
import os


def _get_puzzle_input(year, day):
    if not _session_cookie_exists():
        raise Exception("There is no session cookie provided.")

    with open("../resources/session-cookie") as session_cookie:
        session_id = session_cookie.readline()
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


T = TypeVar("T")


class Instruction(ABC):

    def __init__(self, instruction_parameters: Dict[str, Any] = dict()):
        self.instruction_parameters = instruction_parameters

    @abstractmethod
    def execute(self, system_state: T, additional_parameters: Dict[str, Any] = dict()) -> T:
        pass
