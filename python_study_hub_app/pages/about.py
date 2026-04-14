import reflex as rx


def about() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                # タイトル
                rx.heading("About Page"),
                rx.text("これはAboutページです"),
                # ボタン
                rx.hstack(
                    rx.button(
                        "Primary",
                        bg="blue.500",
                        color="white",
                    ),
                    rx.button("Secondary"),
                ),
                # カード風
                rx.box(
                    rx.text("カードタイトル"),
                    rx.text("ここに説明文が入ります"),
                    padding="1em",
                    bg="white",
                    border_radius="10px",
                ),
                # 入力フォーム
                rx.vstack(
                    rx.input(placeholder="名前を入力"),
                    rx.input(placeholder="メールアドレス"),
                    rx.button(
                        "送信",
                        bg="green",
                        color="white",
                    ),
                ),
                # 区切り線
                rx.divider(),
                # フッター
                rx.text("© 2026 My App"),
            ),
            padding="2em",
            bg="gray",
            width="400px",
        ),
        height="100%"
    )