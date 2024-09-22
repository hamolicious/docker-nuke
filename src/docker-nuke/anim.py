import time
from term import TerminalDisplay
import threading

# region Animation


frames = [
    # """
    #                         | <- End bar (30 char, from leftmost)
    # """,
    """
This is an animation
1
2
3
4
5
.
10
11
12
    """,
    """
This is an animation
1
2
3
4
5
 .
10
11
12
    """,
    """
This is an animation
1
2
3
4
5
  .
10
11
12
""",
    """
This is an animation
1
2
3
4
5
   .
10
11
12
""",
    """
This is an animation
1
2
3
4
5
    .
10
11
12
""",
    """
This is an animation
1
2
3
4
5
     .
10
11
12
""",
]
frames_2d = list(map(lambda s: s.splitlines(), frames))


# endregion Animation


class Animation:
    running = True

    def __init__(self):
        self.terminal_display = TerminalDisplay(30, 15)

    def play_in_thread(self) -> None:
        threading.Thread(
            target=self.play,
        ).start()

    def play(self) -> None:
        try:
            frames_buffer = frames_2d[::]

            while self.running:
                frame = frames_buffer.pop(0)
                frames_buffer.append(frame)

                self.terminal_display.clear()
                self.terminal_display.display_frame(frame)
                self.terminal_display.flush()

                time.sleep(0.25)
        except KeyboardInterrupt:
            return None
        finally:
            # TODO: clean up screen on exit
            ...


if __name__ == "__main__":
    anim = Animation()
    # anim.play_in_thread()
    anim.play()

    # inp = input("Question: ")
    # anim.running = False

    # print("Answer:", inp)
