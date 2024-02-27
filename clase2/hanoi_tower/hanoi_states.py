from typing import Optional


def is_sorted(test_list: list) -> bool:
    if test_list == sorted(test_list, reverse=True):
        return True
    return False


class StatesHanoi:
    def __init__(self, rod1: list, rod2: list, rod3: list):

        self.rods = [rod1, rod2, rod3]
        self.accumulated_cost = 0.0

        # Check if there is common elements between the rods
        if (set.intersection(set(rod1), set(rod2)) or
                set.intersection(set(rod2), set(rod3)) or
                set.intersection(set(rod1), set(rod3))):
            raise ValueError('The same disk is in different rods')

        all_values = set.union(set(rod1), set(rod2), set(rod3))
        if not all(0 < i < 6 for i in all_values):
            raise ValueError('Incorrect disk value')

        if not all(i in all_values for i in range(1, 6)):
            raise ValueError('Not all disk are inserted')

        for rod in self.rods:
            if not is_sorted(rod):
                raise ValueError('Not a valid Hanoi State')

    def get_last_disk_rod(self, number_rod: int, peek: bool = False) -> Optional[int]:
        rod = self.rods[number_rod]
        if len(rod) != 0:
            if peek:
                return rod[-1]
            return rod.pop()
        return None

    def check_valid_disk_in_rod(self, number_rod: int, disk: int) -> bool:
        last_disk_in_rod = self.get_last_disk_rod(number_rod, peek=True)
        if last_disk_in_rod:
            if last_disk_in_rod >= disk:  # Remove equal to remove the Maintain action
                return True
        else:
            return True
        return False

    def put_disk_in_rod(self, number_rod: int, disk: int):
        if self.check_valid_disk_in_rod(number_rod, disk):
            self.rods[number_rod].append(disk)

    def accumulate_cost(self, cost):
        self.accumulated_cost += cost

    def get_accumulated_cost(self):
        return self.accumulated_cost

    def get_state(self) -> list:
        return self.rods


class ActionHanoi:
    def __init__(self, disk: int, rod_input: int, rod_out: input):

        self.disk = disk
        self.rod_input = rod_input

        if rod_input != rod_out:
            self.action = f"Move disk {disk} from {rod_input} to {rod_out}"
            self.cost = 1.0
            self.rod_out = rod_out
        else:
            self.action = f"Maintain disk {disk} in {rod_input}"
            self.cost = 0.0
            self.rod_out = rod_input

    def execute(self, state_hanoi: StatesHanoi):
        if "move" in self.action.lower():
            disk = state_hanoi.get_last_disk_rod(self.rod_input)
            state_hanoi.put_disk_in_rod(self.rod_out, disk)
            state_hanoi.accumulate_cost(self.cost)


def actions_hanoi(state_hanoi: StatesHanoi) -> list:
    actions_list = []
    for i in range(3):
        for j in range(3):
            disk = state_hanoi.get_last_disk_rod(i, peek=True)
            if disk:
                if state_hanoi.check_valid_disk_in_rod(j, disk):
                    actions_list.append(ActionHanoi(disk, i, j))
            else:
                break

    return actions_list



example_state = StatesHanoi([4, 2, 1], [3], [5])

print(example_state.get_state())
print(example_state.get_accumulated_cost())

all_states = actions_hanoi(example_state)

all_states[1].execute(example_state)

print("--------")
print(example_state.get_state())
print(example_state.get_accumulated_cost())

all_states = actions_hanoi(example_state)

for state in all_states:
    print(state.action)

