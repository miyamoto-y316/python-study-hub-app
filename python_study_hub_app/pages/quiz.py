import reflex as rx


class QuizState(rx.State):
    index: int = 0
    selected: str = ""
    result: str = ""

    def select_a(self):
        self.selected = "A"

    def select_b(self):
        self.selected = "B"

    def submit(self):
        if self.index == 0:
            answer = "B"

        if self.selected == answer:
            self.result = "正解 🎉"
        else:
            self.result = "不正解 ❌"

    def next(self):
        self.index = 1
        self.selected = ""
        self.result = ""


def quiz():
    return rx.center(
        rx.vstack(
            rx.heading("Pythonクイズ（簡易版）"),

            rx.text("Pythonでリストはどれ？"),
            rx.text("A: ()"),
            rx.text("B: []"),
            rx.text("C: {}"),

            rx.hstack(
                rx.button("A", on_click=QuizState.select_a),
                rx.button("B", on_click=QuizState.select_b),
                rx.button("C", on_click=QuizState.select_a),
            ),

            rx.hstack(
                rx.button("回答", on_click=QuizState.submit),
                rx.button("次へ", on_click=QuizState.next),
            ),

            rx.text(QuizState.result),

            spacing="4",
        ),
        height="100vh",
    )