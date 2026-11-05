import flet as ft


class ContadorApp:

    def __init__(self):
        self.valor_contador = 0

        self.texto_contador = ft.Text(
            value=str(self.valor_contador),
            size=48,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_600,
        )

    def incrementar(self, e: ft.ControlEvent):
        self.valor_contador += 1
        self.texto_contador.value = str(self.valor_contador)
        self.texto_contador.update()

    def decrementar(self, e: ft.ControlEvent):
        self.valor_contador -= 1
        self.texto_contador.value = str(self.valor_contador)
        self.texto_contador.update()

    def construir_interfaz(self, page: ft.Page):
        page.title = "Contador Interactivo"
        page.window.width = 400
        page.window.height = 350
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        btn_restar = ft.IconButton(
            icon=ft.Icons.REMOVE,
            on_click=self.decrementar,
            icon_color=ft.Colors.RED_400,
            icon_size=32,
        )

        btn_sumar = ft.IconButton(
            icon=ft.Icons.ADD,
            on_click=self.incrementar,
            icon_color=ft.Colors.GREEN_400,
            icon_size=32,
        )

        fila_controles = ft.Row(
            controls=[btn_restar, self.texto_contador, btn_sumar],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=25,
        )

        tarjeta_principal = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Contador Interactivo",
                            size=20,
                            weight=ft.FontWeight.W_500,
                        ),
                        fila_controles,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=30,
            )
        )

        page.add(tarjeta_principal)


def main(page: ft.Page):
    app = ContadorApp()
    app.construir_interfaz(page)


if __name__ == "__main__":
    ft.run(main)