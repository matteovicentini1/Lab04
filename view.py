import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.btnavvio = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        self.menutendina = ft.Dropdown(label="Lingua",width=150)
        self.menutenda()
        r1 = ft.Row([self.menutendina])
        self.selezione = ft.Dropdown(label="Tipologia di ricerca",width=130)
        self.fillselezione()
        self.testo = ft.TextField(label='Sentences',width=200)
        self.btnavvio=ft.ElevatedButton(text='search',icon=ft.icons.SEARCH,on_click=self.bottone)
        r2 =ft.Row([self.selezione,self.testo,self.btnavvio],alignment=ft.MainAxisAlignment.CENTER)
        self.parole=''
        self.time =0
        self.lv1=ft.ListView()

        self.page.add(r1,r2,self.lv1)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()

    def menutenda(self):
        self.menutendina.options.append(ft.dropdown.Option("italian"))
        self.menutendina.options.append(ft.dropdown.Option("english"))
        self.menutendina.options.append(ft.dropdown.Option("spanish"))
    def fillselezione(self):
        self.selezione.options.append(ft.dropdown.Option('Default'))
        self.selezione.options.append(ft.dropdown.Option('Linear'))
        self.selezione.options.append(ft.dropdown.Option('Dichotomic'))

    def bottone(self,e):
        if self.selezione.value is None or self.testo.value=='' or self.menutendina.value not in ("italian","english","spanish") :
            self.lv1.controls.append(ft.Text(f'Campo/i vuoto/i'))
            self.testo.value = ''
            self.menutendina.value = None
            self.selezione.value = None
            self.page.update()
        else:
            (self.parole,self.time) = self.__controller.handleSentence(self.testo.value,self.menutendina.value,self.selezione.value)
            self.lv1.controls.append(ft.Text(f'testo: {self.testo.value}'))
            self.lv1.controls.append(ft.Text(f'parole errate:{self.parole}'))
            self.lv1.controls.append(ft.Text(f'tempo:{self.time}'))
            self.testo.value=''
            self.menutendina.value=None
            self.selezione.value=None
            self.page.update()
            self.time=0
            self.parole=''








