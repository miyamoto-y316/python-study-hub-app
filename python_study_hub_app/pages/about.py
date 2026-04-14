import reflex as rx

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("About Page"),
            rx.text("これはAboutページです"),
        ),
        height="100vh",
    )