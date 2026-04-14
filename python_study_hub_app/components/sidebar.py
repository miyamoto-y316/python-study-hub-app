import reflex as rx

def sidebar() -> rx.Component:
    return rx.vstack(
        rx.heading("Menu", size="5"),
        rx.link("Home", href="/"),
        rx.link("About", href="/about"),
        spacing="3",
        width="200px",
        padding="1em",
        background_color="#f5f5f5",
        height="100vh",
    )