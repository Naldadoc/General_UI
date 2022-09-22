# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#imports
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IRightBody, OneLineIconListItem
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.dialog import MDDialog
from kivy.properties import StringProperty
from kivymd.uix.bottomnavigation import MDBottomNavigation
import DAQ_analyzer

test = DAQ_analyzer.get_rm_list()



class  General_UIApp(MDApp):

    # Instrument list dialog
    instrument_dialog = None

    def build(self):

        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.theme_style = 'Light'
        Builder.load_file('User_interface.kv')
        Builder.load_file('Start_screen.kv')
        Builder.load_file('NavDrawerContent.kv')
        Builder.load_file('Instrument_config.kv')
        Builder.load_file('List_item.kv')
        return User_interface()

    def ciao(self):
        print('ciao')
        return

    def show_instrument_dialog(self):
        l = []
        for i in test.keys():
            l.append(Instrument_item(text = test[i],address = i))
            pass
        self.instrument_dialog = MDDialog(title = 'Select Instrument',type = 'simple', items = l)
        self.instrument_dialog.open()
        return

    def add_list_item(self, current_screen):
        print(current_screen)
        if current_screen == 'instrument-config':
            MDApp.get_running_app().root.ids.root_screen.get_screen(current_screen).ids.power_supply_list.add_list()
            pass
        else:
            pass
        return

    pass


class User_interface(BoxLayout):
    pass


class Start_Screen(Screen):
    pass


class Instrument_config(Screen):
    pass


class NavDrawerContent(MDList):
    pass


class CustomItem(OneLineAvatarIconListItem):
    pass


class MyItem(IRightBody,GridLayout):
    pass


class Add_instr_item(OneLineIconListItem):
    pass


class Instrument_item(OneLineIconListItem):
    address = StringProperty()
    pass

class Instrument_config_list(MDList):

    def add_list(self):
        print('yes')
        return
    pass





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    General_UIApp().run()

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
