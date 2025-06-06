import esphome.codegen as cg
from esphome.components import text
from esphome.components.text import new_text
import esphome.config_validation as cv

from ..defines import CONF_WIDGET
from ..lvcode import (
    API_EVENT,
    EVENT_ARG,
    UPDATE_EVENT,
    LambdaContext,
    LvContext,
    lv,
    lv_add,
    lvgl_static,
)
from ..types import LV_EVENT, LvText, lvgl_ns
from ..widgets import get_widgets, wait_for_widgets

LVGLText = lvgl_ns.class_("LVGLText", text.Text)

CONFIG_SCHEMA = text.text_schema(LVGLText).extend(
    {
        cv.Required(CONF_WIDGET): cv.use_id(LvText),
    }
)


async def to_code(config):
    textvar = await new_text(config)
    widget = await get_widgets(config, CONF_WIDGET)
    widget = widget[0]
    await wait_for_widgets()
    async with LambdaContext([(cg.std_string, "text_value")]) as control:
        await widget.set_property("text", "text_value.c_str()")
        lv.event_send(widget.obj, API_EVENT, cg.nullptr)
        control.add(textvar.publish_state(widget.get_value()))
    async with LambdaContext(EVENT_ARG) as lamb:
        lv_add(textvar.publish_state(widget.get_value()))
    async with LvContext():
        lv_add(textvar.set_control_lambda(await control.get_lambda()))
        lv_add(
            lvgl_static.add_event_cb(
                widget.obj,
                await lamb.get_lambda(),
                LV_EVENT.VALUE_CHANGED,
                UPDATE_EVENT,
            )
        )
        lv_add(textvar.publish_state(widget.get_value()))
