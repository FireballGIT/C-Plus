class Version:
    def __init__(self):
        self.version = ""

    def update_version(self, new_version: float, state: int) -> str:
        match state:
            case 1:
                state_str = "Alpha"
            case 2:
                state_str = "Beta"
            case 3:
                state_str = "Stable"
            case _:
                state_str = "Unknown"

        self.version = f"{state_str} {new_version}"
        return self.version
