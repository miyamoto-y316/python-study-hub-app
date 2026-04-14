import reflex as rx

def home() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Home Page"),
            rx.text("これはホームです"),
        ),
        height="100vh",
    )