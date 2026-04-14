import reflex as rx

from python_study_hub_app.pages.home import home
from python_study_hub_app.pages.about import about
from python_study_hub_app.layouts.main import main_layout

app = rx.App()

app.add_page(lambda: main_layout(home()), route="/")
app.add_page(lambda: main_layout(about()), route="/about")