from Components.MenuList import MenuList
from Screens import MessageBox
from Screens.Screen import Screen
from Components.ActionMap import ActionMap
from Plugins.Plugin import PluginDescriptor
from Emby import EmbyAPI

###########################################################################
from tcpRequest import log


class HalloWorldScreen(Screen):
    skin = """<screen position="100,150" size="460,400" title=Emby Primitive Testing" >
            <widget name="myMenu" position="10,10" size="420,380" scrollbarMode="showOnDemand" />
            </screen>"""


    def __init__(self, session, args=None):
        e = EmbyAPI()
        self.session = session
        list = []
        list.append((("Entry 1"), "one"))
        list.append((("Entry 2"), "two"))
        list.append((("Entry 3"), "tree"))
        list.append((("Exit"), "exit"))
        Screen.__init__(self, session)
        self["myMenu"] = MenuList(list)
        self["myActionMap"] = ActionMap(["SetupActions"],{"ok": self.go,"cancel": self.cancel}, -1)

    def go(self):
        returnValue = self["myMenu"].l.getCurrentSelection()[1]
        print "\n[MyMenu] returnValue: " + returnValue + "\n"
        if returnValue is not None:
            if returnValue is "one":
                self.myMsg("1")
            elif returnValue is "two":
                self.myMsg("2")
            elif returnValue is "tree":
                self.myMsg("3")
            else:
                print "\n[MyMenu] cancel\n"
                self.close(None)

    def myMsg(self, entry):
        self.session.open(MessageBox,("You selected entry no. %s!")% (entry), MessageBox.TYPE_INFO)

    def cancel(self):
        print "\n[MyMenu] cancel\n"
        self.close(None)


###########################################################################
def main(session, **kwargs):
    print "\n[Enby] starts working\n"
    log("\n[Enby] starts working")
    session.open(HalloWorldScreen)


###########################################################################
def Plugins(**kwargs):
    return PluginDescriptor(name="Emby", description="Emby Plugin for Enigma2",
                            where=PluginDescriptor.WHERE_PLUGINMENU, icon="../ihad_tut.png", fnc=main)



