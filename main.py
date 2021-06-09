import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction
import hashlib
import subprocess as sub


logger = logging.getLogger(__name__)


class DemoExtension(Extension):
    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


def open_janus():
    sub.Popen('gnome-terminal',"--command='/home/tigerit/work/workplace/tigerit/janus_rnd/janus-gateway/janus'")


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        items = [
            ExtensionResultItem(
                icon="images/janus-logo.png",
                name="Start Janus Server",
                on_enter=open_janus()
            )
        ]

        return RenderResultListAction(items)


if __name__ == "__main__":
    DemoExtension().run()
