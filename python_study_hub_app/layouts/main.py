import reflex as rx
from python_study_hub_app.components.sidebar import sidebar

def main_layout(content: rx.Component) -> rx.Component:
    return rx.hstack(
        sidebar(),
        rx.box(
            content,
            padding="2em",
            width="100%",
        ),
        height="100vh",
    )