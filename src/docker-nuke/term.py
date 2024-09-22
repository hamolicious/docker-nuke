import sys


class TerminalDisplay:
    def __init__(self, width: int, height: int, x_offset: int = 0, y_offset: int = 0):
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset

    def clear(self) -> None:
        """Clear the defined display area"""
        for y in range(self.height):
            self.move_cursor(self.x_offset, self.y_offset + y)
            sys.stdout.write(" " * self.width)
        self.flush()

    def move_cursor(self, x: int, y: int) -> None:
        """Move the cursor to a specific (x, y) position within the terminal"""
        sys.stdout.write(f"\033[{y};{x}H")
        self.flush()  # is this necessary?

    def write_text(self, text: str, x: int, y: int) -> None:
        """Write text within the defined display area"""
        self.move_cursor(self.x_offset + x, self.y_offset + y)
        sys.stdout.write(text[: self.width])  # Clip text to fit within the width
        sys.stdout.flush()

    def flush(self) -> None:
        sys.stdout.flush()

    @staticmethod
    def add_nl(value: str) -> str:
        return value + ("" if value.endswith("\n") else "\n")

    def display_frame(self, string_2d: list[str]) -> None:
        """Draw a simple frame around the display area"""
        origin = (self.x_offset, self.y_offset)
        frames = string_2d[::]
        for y in range(self.height):
            line = " " * self.width

            if len(frames) != 0:
                line = frames.pop(0)

            self.write_text(self.add_nl(line[: self.width :]), origin[0], origin[1] + y)

        print()
        self.flush()


# Example usage
if __name__ == "__main__":
    display = TerminalDisplay(30, 8, x_offset=10, y_offset=5)
    display.write_text("Hello, Screen!", 5, 3)
    display.flush()
