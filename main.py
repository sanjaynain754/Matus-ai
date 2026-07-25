"""
MATUS AI - Professional Mobile App
Single AI Agent: Datya
Admin: Sanjay
All agents controlled, all tools accessible, web access, admin control
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp
import sys
from io import StringIO

# Import Datya Core
from datya_core import get_datya


# ============================================================
# COLOR SCHEME
# ============================================================
COLORS = {
    'bg_dark': (0.08, 0.08, 0.12, 1),
    'bg_card': (0.14, 0.14, 0.20, 1),
    'bg_input': (0.10, 0.10, 0.15, 1),
    'accent': (0.20, 0.85, 0.55, 1),      # Green
    'accent2': (0.25, 0.65, 0.95, 1),     # Blue
    'accent3': (0.95, 0.40, 0.35, 1),     # Red
    'accent4': (0.95, 0.75, 0.20, 1),     # Gold
    'text': (0.92, 0.92, 0.95, 1),
    'text_dim': (0.55, 0.55, 0.60, 1),
    'border': (0.22, 0.22, 0.30, 1),
}


# ============================================================
# CUSTOM WIDGETS
# ============================================================
class CardLayout(BoxLayout):
    """A card-style container"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [dp(15), dp(12), dp(15), dp(12)]
        self.spacing = dp(8)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['bg_card'])
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])
        self.bind(pos=self._update_canvas, size=self._update_canvas)

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*COLORS['bg_card'])
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])


class HeaderBar(BoxLayout):
    """Professional header bar"""
    def __init__(self, title, subtitle="", **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.height = dp(90)
        self.padding = [dp(15), dp(10), dp(15), dp(10)]

        # Title
        self.title_label = Label(
            text=title,
            font_size=dp(22),
            bold=True,
            color=COLORS['text'],
            size_hint_y=None,
            height=dp(30),
            halign='left',
            valign='middle'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))

        # Subtitle
        self.sub_label = Label(
            text=subtitle,
            font_size=dp(12),
            color=COLORS['text_dim'],
            size_hint_y=None,
            height=dp(20),
            halign='left',
            valign='middle'
        )
        self.sub_label.bind(size=self.sub_label.setter('text_size'))

        self.add_widget(self.title_label)
        self.add_widget(self.sub_label)


class OutputLabel(Label):
    """Output display label with auto-sizing"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = COLORS['text']
        self.font_size = dp(13)
        self.halign = 'left'
        self.valign = 'top'
        self.size_hint_y = None
        self.bind(size=self.setter('text_size'))
        self.bind(texture_size=self.setter('height'))


# ============================================================
# SCREENS
# ============================================================
class HomeScreen(Screen):
    """Main dashboard screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        # Header
        header = HeaderBar("MATUS AI", "Datya v2.0 | Admin: Sanjay")
        layout.add_widget(header)

        # Scrollable content
        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=[dp(15), dp(10)], spacing=dp(12))

        # Status Card
        status_card = CardLayout(size_hint_y=None, height=dp(200))
        status_title = Label(text="DATYA STATUS", font_size=dp(14), bold=True,
                           color=COLORS['accent'], size_hint_y=None, height=dp(22),
                           halign='left')
        status_title.bind(size=status_title.setter('text_size'))
        status_card.add_widget(status_title)

        self.status_text = OutputLabel(
            text="Initializing...",
            height=dp(160)
        )
        status_card.add_widget(self.status_text)
        content.add_widget(status_card)

        # Quick Actions
        actions_title = Label(text="QUICK ACTIONS", font_size=dp(14), bold=True,
                            color=COLORS['accent2'], size_hint_y=None, height=dp(22),
                            halign='left')
        actions_title.bind(size=actions_title.setter('text_size'))
        content.add_widget(actions_title)

        # Action buttons grid
        grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(220))

        buttons = [
            ("Hacking Tools", COLORS['accent3'], "hacking"),
            ("Web Access", COLORS['accent2'], "web"),
            ("Admin Panel", COLORS['accent4'], "admin"),
            ("AI Agent", COLORS['accent'], "ai"),
            ("Security Scan", COLORS['accent3'], "mythos"),
            ("Terminal", COLORS['text_dim'], "terminal"),
        ]

        for btn_text, btn_color, target in buttons:
            btn = Button(
                text=btn_text,
                font_size=dp(13),
                bold=True,
                background_color=btn_color,
                background_normal='',
                size_hint=(1, 1)
            )
            btn.bind(on_press=lambda *a, t=target: self._navigate(t))
            grid.add_widget(btn)

        content.add_widget(grid)

        # Credits
        credits = Label(
            text="Matus AI v2.0 | Datya Agent | Admin: Sanjay",
            font_size=dp(10),
            color=COLORS['text_dim'],
            size_hint_y=None,
            height=dp(30)
        )
        content.add_widget(credits)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

        # Load status after a short delay
        Clock.schedule_once(lambda dt: self._load_status(), 0.5)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _load_status(self):
        datya = get_datya()
        self.status_text.text = datya._cmd_status()

    def _navigate(self, target):
        sm = self.manager
        if target == "hacking":
            sm.current = 'hacking'
        elif target == "web":
            sm.current = 'web'
        elif target == "admin":
            sm.current = 'admin'
        elif target == "ai":
            sm.current = 'terminal'
        elif target == "mythos":
            sm.current = 'mythos'
        elif target == "terminal":
            sm.current = 'terminal'


class TerminalScreen(Screen):
    """Main AI terminal - Datya chat interface"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'terminal'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        # Header
        header = HeaderBar("DATYA TERMINAL", "AI Agent | All Tools Access")
        layout.add_widget(header)

        # Output area
        scroll = ScrollView(size_hint=(1, 1))
        self.output = OutputLabel(
            text=f"[Datya] Welcome to Matus AI Terminal\n"
                 f"[Datya] I am Datya - your AI agent\n"
                 f"[Datya] Admin: Sanjay\n"
                 f"[Datya] Type 'datya_help()' to see all commands\n"
                 f"[Datya] Example: scan_ports('google.com', '80,443')\n\n",
            height=dp(500)
        )
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        # Input area
        input_area = CardLayout(size_hint_y=None, height=dp(70))
        input_box = BoxLayout(orientation='horizontal', spacing=dp(8))

        self.input_text = TextInput(
            hint_text="Enter command... e.g. datya_status()",
            font_size=dp(14),
            multiline=False,
            background_color=COLORS['bg_input'],
            foreground_color=COLORS['text'],
            cursor_color=COLORS['accent'],
        )
        self.input_text.bind(on_text_validate=self._run_command)

        send_btn = Button(
            text="Send",
            font_size=dp(14),
            bold=True,
            background_color=COLORS['accent'],
            background_normal='',
            size_hint_x=None,
            width=dp(80)
        )
        send_btn.bind(on_press=self._run_command)

        input_box.add_widget(self.input_text)
        input_box.add_widget(send_btn)
        input_area.add_widget(input_box)
        layout.add_widget(input_area)

        self.add_widget(layout)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _run_command(self, *args):
        cmd = self.input_text.text.strip()
        if not cmd:
            return

        datya = get_datya()
        self.output.text += f"> {cmd}\n"

        try:
            result = datya.process(cmd)
            self.output.text += f"  {result}\n\n"
        except Exception as e:
            self.output.text += f"  [Error] {str(e)}\n\n"

        self.input_text.text = ""
        # Auto-scroll to bottom
        scroll = self.children[1]
        if isinstance(scroll, ScrollView):
            scroll.scroll_y = 0


class HackingScreen(Screen):
    """Hacking & Network Tools screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'hacking'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        header = HeaderBar("HACKING TOOLS", "Network & Security")
        layout.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=[dp(15), dp(10)], spacing=dp(10))

        # Port Scanner
        card = CardLayout(size_hint_y=None, height=dp(160))
        card.add_widget(Label(text="PORT SCANNER", font_size=dp(13), bold=True,
                            color=COLORS['accent3'], size_hint_y=None, height=dp(20), halign='left'))
        target_input = TextInput(hint_text="Target host (e.g. google.com)", font_size=dp(12),
                                multiline=False, background_color=COLORS['bg_input'],
                                foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        ports_input = TextInput(hint_text="Ports (e.g. 80,443,8080)", font_size=dp(12),
                               multiline=False, background_color=COLORS['bg_input'],
                               foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        scan_btn = Button(text="SCAN", font_size=dp(13), bold=True,
                         background_color=COLORS['accent3'], background_normal='',
                         size_hint_y=None, height=dp(35))

        def do_scan(*args):
            from datya_hacking import HackingAgent
            agent = HackingAgent()
            result = agent.scan_ports(target_input.text or "localhost", ports_input.text or "80,443")
            self._show_result_popup("Port Scan Result", result)

        scan_btn.bind(on_press=do_scan)
        card.add_widget(target_input)
        card.add_widget(ports_input)
        card.add_widget(scan_btn)
        content.add_widget(card)

        # IP Lookup
        card2 = CardLayout(size_hint_y=None, height=dp(110))
        card2.add_widget(Label(text="IP LOOKUP", font_size=dp(13), bold=True,
                             color=COLORS['accent2'], size_hint_y=None, height=dp(20), halign='left'))
        ip_input = TextInput(hint_text="Domain name", font_size=dp(12),
                            multiline=False, background_color=COLORS['bg_input'],
                            foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        lookup_btn = Button(text="LOOKUP", font_size=dp(13), bold=True,
                           background_color=COLORS['accent2'], background_normal='',
                           size_hint_y=None, height=dp(35))

        def do_lookup(*args):
            from datya_hacking import HackingAgent
            result = HackingAgent().get_ip(ip_input.text or "google.com")
            self._show_result_popup("IP Lookup", result)

        lookup_btn.bind(on_press=do_lookup)
        card2.add_widget(ip_input)
        card2.add_widget(lookup_btn)
        content.add_widget(card2)

        # Ping Tool
        card3 = CardLayout(size_hint_y=None, height=dp(110))
        card3.add_widget(Label(text="PING HOST", font_size=dp(13), bold=True,
                             color=COLORS['accent4'], size_hint_y=None, height=dp(20), halign='left'))
        ping_input = TextInput(hint_text="Host to ping", font_size=dp(12),
                              multiline=False, background_color=COLORS['bg_input'],
                              foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        ping_btn = Button(text="PING", font_size=dp(13), bold=True,
                         background_color=COLORS['accent4'], background_normal='',
                         size_hint_y=None, height=dp(35))

        def do_ping(*args):
            from datya_hacking import HackingAgent
            result = HackingAgent().ping_host(ping_input.text or "google.com")
            self._show_result_popup("Ping Result", result)

        ping_btn.bind(on_press=do_ping)
        card3.add_widget(ping_input)
        card3.add_widget(ping_btn)
        content.add_widget(card3)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _show_result_popup(self, title, content):
        box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        box.add_widget(Label(text=title, font_size=dp(16), bold=True,
                           color=COLORS['accent'], size_hint_y=None, height=dp(30)))
        scroll = ScrollView()
        scroll.add_widget(Label(text=content, font_size=dp(11), color=COLORS['text'],
                               halign='left', valign='top', size_hint_y=None,
                               text_size=(Window.width - dp(60), None)))
        scroll.bind(minimum_height=scroll.setter('height'))
        box.add_widget(scroll)
        close_btn = Button(text="Close", font_size=dp(14), bold=True,
                          background_color=COLORS['accent'], background_normal='',
                          size_hint_y=None, height=dp(40))
        close_btn.bind(on_press=lambda *a: popup.dismiss())
        box.add_widget(close_btn)

        popup = Popup(title=title, content=box, size_hint=(0.9, 0.7),
                     background_color=COLORS['bg_card'])
        popup.open()


class WebScreen(Screen):
    """Web Access screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'web'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        header = HeaderBar("WEB ACCESS", "Fetch, Scrape, Search, API")
        layout.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=[dp(15), dp(10)], spacing=dp(10))

        # URL Fetch
        card = CardLayout(size_hint_y=None, height=dp(110))
        card.add_widget(Label(text="FETCH URL", font_size=dp(13), bold=True,
                            color=COLORS['accent2'], size_hint_y=None, height=dp(20), halign='left'))
        url_input = TextInput(hint_text="https://example.com", font_size=dp(12),
                             multiline=False, background_color=COLORS['bg_input'],
                             foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        fetch_btn = Button(text="FETCH", font_size=dp(13), bold=True,
                          background_color=COLORS['accent2'], background_normal='',
                          size_hint_y=None, height=dp(35))

        def do_fetch(*args):
            from datya_web import WebAgent
            result = WebAgent().web_fetch(url_input.text or "https://example.com")
            self._show_result_popup("URL Content", result)

        fetch_btn.bind(on_press=do_fetch)
        card.add_widget(url_input)
        card.add_widget(fetch_btn)
        content.add_widget(card)

        # Web Scrape
        card2 = CardLayout(size_hint_y=None, height=dp(110))
        card2.add_widget(Label(text="SCRAPE TEXT", font_size=dp(13), bold=True,
                             color=COLORS['accent'], size_hint_y=None, height=dp(20), halign='left'))
        scrape_input = TextInput(hint_text="URL to scrape text from", font_size=dp(12),
                                multiline=False, background_color=COLORS['bg_input'],
                                foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        scrape_btn = Button(text="SCRAPE", font_size=dp(13), bold=True,
                           background_color=COLORS['accent'], background_normal='',
                           size_hint_y=None, height=dp(35))

        def do_scrape(*args):
            from datya_web import WebAgent
            result = WebAgent().web_scrape(scrape_input.text or "https://example.com")
            self._show_result_popup("Scraped Text", result)

        scrape_btn.bind(on_press=do_scrape)
        card2.add_widget(scrape_input)
        card2.add_widget(scrape_btn)
        content.add_widget(card2)

        # Web Search
        card3 = CardLayout(size_hint_y=None, height=dp(110))
        card3.add_widget(Label(text="WEB SEARCH", font_size=dp(13), bold=True,
                             color=COLORS['accent4'], size_hint_y=None, height=dp(20), halign='left'))
        search_input = TextInput(hint_text="Search query", font_size=dp(12),
                                multiline=False, background_color=COLORS['bg_input'],
                                foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        search_btn = Button(text="SEARCH", font_size=dp(13), bold=True,
                           background_color=COLORS['accent4'], background_normal='',
                           size_hint_y=None, height=dp(35))

        def do_search(*args):
            from datya_web import WebAgent
            result = WebAgent().web_search(search_input.text or "Matus AI")
            self._show_result_popup("Search Results", result)

        search_btn.bind(on_press=do_search)
        card3.add_widget(search_input)
        card3.add_widget(search_btn)
        content.add_widget(card3)

        # API JSON
        card4 = CardLayout(size_hint_y=None, height=dp(110))
        card4.add_widget(Label(text="API JSON", font_size=dp(13), bold=True,
                             color=COLORS['accent3'], size_hint_y=None, height=dp(20), halign='left'))
        api_input = TextInput(hint_text="API URL", font_size=dp(12),
                             multiline=False, background_color=COLORS['bg_input'],
                             foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        api_btn = Button(text="FETCH JSON", font_size=dp(13), bold=True,
                        background_color=COLORS['accent3'], background_normal='',
                        size_hint_y=None, height=dp(35))

        def do_api(*args):
            from datya_web import WebAgent
            result = WebAgent().web_api_json(api_input.text or "https://httpbin.org/json")
            self._show_result_popup("API Response", result)

        api_btn.bind(on_press=do_api)
        card4.add_widget(api_input)
        card4.add_widget(api_btn)
        content.add_widget(card4)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _show_result_popup(self, title, content):
        box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        box.add_widget(Label(text=title, font_size=dp(16), bold=True,
                           color=COLORS['accent'], size_hint_y=None, height=dp(30)))
        scroll = ScrollView()
        lbl = Label(text=str(content)[:5000], font_size=dp(10), color=COLORS['text'],
                   halign='left', valign='top', size_hint_y=None,
                   text_size=(Window.width - dp(60), None))
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('height'))
        scroll.add_widget(lbl)
        box.add_widget(scroll)
        close_btn = Button(text="Close", font_size=dp(14), bold=True,
                          background_color=COLORS['accent'], background_normal='',
                          size_hint_y=None, height=dp(40))
        close_btn.bind(on_press=lambda *a: popup.dismiss())
        box.add_widget(close_btn)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.7),
                     background_color=COLORS['bg_card'])
        popup.open()


class AdminScreen(Screen):
    """Admin Control screen - Sanjay"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'admin'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        header = HeaderBar("ADMIN PANEL", "System Control | Admin: Sanjay")
        layout.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=[dp(15), dp(10)], spacing=dp(10))

        # System Info
        card = CardLayout(size_hint_y=None, height=dp(180))
        card.add_widget(Label(text="SYSTEM INFO", font_size=dp(13), bold=True,
                            color=COLORS['accent4'], size_hint_y=None, height=dp(20), halign='left'))
        self.sys_info_label = OutputLabel(
            text="Loading...",
            height=dp(140)
        )
        card.add_widget(self.sys_info_label)
        content.add_widget(card)

        # Action buttons
        grid = GridLayout(cols=2, spacing=dp(10), size_hint_y=None, height=dp(180))

        btns = [
            ("Process List", COLORS['accent2'], "procs"),
            ("Disk Usage", COLORS['accent'], "disk"),
            ("Root Check", COLORS['accent4'], "root"),
            ("Battery", COLORS['accent3'], "battery"),
        ]

        for btn_text, btn_color, action in btns:
            btn = Button(text=btn_text, font_size=dp(12), bold=True,
                        background_color=btn_color, background_normal='',
                        size_hint=(1, 1))

            def do_action(btn_text=btn_text, action=action):
                from datya_admin import AdminAgent
                agent = AdminAgent()
                if action == "procs":
                    result = agent.admin_list_procs()
                elif action == "disk":
                    result = agent.admin_disk_usage()
                elif action == "root":
                    result = f"Root/Admin: {agent.admin_is_root()}"
                elif action == "battery":
                    result = agent.admin_battery()
                self._show_result_popup(btn_text, result)

            btn.bind(on_press=do_action)
            grid.add_widget(btn)

        content.add_widget(grid)

        # Vibrate & Brightness
        card2 = CardLayout(size_hint_y=None, height=dp(120))
        card2.add_widget(Label(text="DEVICE CONTROL", font_size=dp(13), bold=True,
                             color=COLORS['accent'], size_hint_y=None, height=dp(20), halign='left'))
        vib_btn = Button(text="VIBRATE", font_size=dp(12), bold=True,
                        background_color=COLORS['accent3'], background_normal='',
                        size_hint_y=None, height=dp(40))
        vib_btn.bind(on_press=lambda *a: self._vibrate())
        card2.add_widget(vib_btn)

        bright_input = TextInput(hint_text="Brightness 0-255", font_size=dp(12),
                                multiline=False, background_color=COLORS['bg_input'],
                                foreground_color=COLORS['text'], size_hint_y=None, height=dp(35))
        bright_btn = Button(text="SET BRIGHTNESS", font_size=dp(12), bold=True,
                           background_color=COLORS['accent4'], background_normal='',
                           size_hint_y=None, height=dp(35))

        def set_bright(*args):
            from datya_admin import AdminAgent
            result = AdminAgent().admin_set_brightness(bright_input.text or "128")
            self._show_result_popup("Brightness", result)

        bright_btn.bind(on_press=set_bright)
        card2.add_widget(bright_input)
        card2.add_widget(bright_btn)
        content.add_widget(card2)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

        Clock.schedule_once(lambda dt: self._load_sys_info(), 0.5)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _load_sys_info(self):
        from datya_admin import AdminAgent
        self.sys_info_label.text = AdminAgent().admin_sys_info()

    def _vibrate(self):
        from datya_admin import AdminAgent
        result = AdminAgent().admin_vibrate("500")
        self._show_result_popup("Vibrate", result)

    def _show_result_popup(self, title, content):
        box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        box.add_widget(Label(text=title, font_size=dp(16), bold=True,
                           color=COLORS['accent'], size_hint_y=None, height=dp(30)))
        scroll = ScrollView()
        lbl = Label(text=str(content)[:5000], font_size=dp(10), color=COLORS['text'],
                   halign='left', valign='top', size_hint_y=None,
                   text_size=(Window.width - dp(60), None))
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('height'))
        scroll.add_widget(lbl)
        box.add_widget(scroll)
        close_btn = Button(text="Close", font_size=dp(14), bold=True,
                          background_color=COLORS['accent'], background_normal='',
                          size_hint_y=None, height=dp(40))
        close_btn.bind(on_press=lambda *a: popup.dismiss())
        box.add_widget(close_btn)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.7),
                     background_color=COLORS['bg_card'])
        popup.open()


class MythosScreen(Screen):
    """Security Analysis screen"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'mythos'

        layout = BoxLayout(orientation='vertical')
        layout.canvas.before.clear()
        with layout.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=lambda *a: self._update_bg(layout),
                    size=lambda *a: self._update_bg(layout))

        header = HeaderBar("MYTHOS", "Security Analysis & Vuln Assessment")
        layout.add_widget(header)

        scroll = ScrollView(size_hint=(1, 1))
        content = BoxLayout(orientation='vertical', padding=[dp(15), dp(10)], spacing=dp(10))

        # Code Scanner
        card = CardLayout(size_hint_y=None, height=dp(200))
        card.add_widget(Label(text="CODE SECURITY SCAN", font_size=dp(13), bold=True,
                            color=COLORS['accent3'], size_hint_y=None, height=dp(20), halign='left'))
        code_input = TextInput(hint_text="Paste code to analyze...", font_size=dp(11),
                              multiline=True, background_color=COLORS['bg_input'],
                              foreground_color=COLORS['text'], size_hint_y=None, height=dp(120))
        scan_btn = Button(text="SCAN CODE", font_size=dp(13), bold=True,
                         background_color=COLORS['accent3'], background_normal='',
                         size_hint_y=None, height=dp(40))

        def do_scan_code(*args):
            from datya_mythos import MythosAgent
            result = MythosAgent().mythos_scan_code(code_input.text)
            self._show_result_popup("Security Scan", result)

        scan_btn.bind(on_press=do_scan_code)
        card.add_widget(code_input)
        card.add_widget(scan_btn)
        content.add_widget(card)

        # URL Security Check
        card2 = CardLayout(size_hint_y=None, height=dp(110))
        card2.add_widget(Label(text="URL SECURITY CHECK", font_size=dp(13), bold=True,
                             color=COLORS['accent4'], size_hint_y=None, height=dp(20), halign='left'))
        url_input = TextInput(hint_text="URL to check", font_size=dp(12),
                             multiline=False, background_color=COLORS['bg_input'],
                             foreground_color=COLORS['text'], size_hint_y=None, height=dp(40))
        check_btn = Button(text="CHECK", font_size=dp(13), bold=True,
                          background_color=COLORS['accent4'], background_normal='',
                          size_hint_y=None, height=dp(35))

        def do_url_check(*args):
            from datya_mythos import MythosAgent
            result = MythosAgent().mythos_basic_check(url_input.text)
            self._show_result_popup("URL Check", result)

        check_btn.bind(on_press=do_url_check)
        card2.add_widget(url_input)
        card2.add_widget(check_btn)
        content.add_widget(card2)

        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def _update_bg(self, widget):
        widget.canvas.before.clear()
        with widget.canvas.before:
            Color(*COLORS['bg_dark'])
            Rectangle(pos=widget.pos, size=widget.size)

    def _show_result_popup(self, title, content):
        box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        box.add_widget(Label(text=title, font_size=dp(16), bold=True,
                           color=COLORS['accent'], size_hint_y=None, height=dp(30)))
        scroll = ScrollView()
        lbl = Label(text=str(content)[:5000], font_size=dp(10), color=COLORS['text'],
                   halign='left', valign='top', size_hint_y=None,
                   text_size=(Window.width - dp(60), None))
        lbl.bind(size=lbl.setter('text_size'))
        lbl.bind(texture_size=lbl.setter('height'))
        scroll.add_widget(lbl)
        box.add_widget(scroll)
        close_btn = Button(text="Close", font_size=dp(14), bold=True,
                          background_color=COLORS['accent'], background_normal='',
                          size_hint_y=None, height=dp(40))
        close_btn.bind(on_press=lambda *a: popup.dismiss())
        box.add_widget(close_btn)
        popup = Popup(title=title, content=box, size_hint=(0.9, 0.7),
                     background_color=COLORS['bg_card'])
        popup.open()


# ============================================================
# APP
# ============================================================
class MatusApp(App):
    def build(self):
        Window.clearcolor = COLORS['bg_dark']

        sm = ScreenManager(transition=SlideTransition(direction='left'))

        sm.add_widget(HomeScreen())
        sm.add_widget(TerminalScreen())
        sm.add_widget(HackingScreen())
        sm.add_widget(WebScreen())
        sm.add_widget(AdminScreen())
        sm.add_widget(MythosScreen())

        return sm


if __name__ == '__main__':
    MatusApp().run()
