import esphome.codegen as cg
from esphome.components import select
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_OPTIONS, CONF_RESTORE_VALUE

from ..defines import CONF_ANIMATED, CONF_WIDGET, literal
from ..types import LvSelect, lvgl_ns
from ..widgets import get_widgets

LVGLSelect = lvgl_ns.class_("LVGLSelect", select.Select, cg.Component)

CONFIG_SCHEMA = select.select_schema(LVGLSelect).extend(
    {
        cv.Required(CONF_WIDGET): cv.use_id(LvSelect),
        cv.Optional(CONF_ANIMATED, default=False): cv.boolean,
        cv.Optional(CONF_RESTORE_VALUE, default=False): cv.boolean,
    }
)


async def to_code(config):
    widget = await get_widgets(config, CONF_WIDGET)
    widget = widget[0]
    options = widget.config.get(CONF_OPTIONS, [])
    animated = literal("LV_ANIM_ON" if config[CONF_ANIMATED] else "LV_ANIM_OFF")
    selector = cg.new_Pvariable(
        config[CONF_ID], widget.var, animated, config[CONF_RESTORE_VALUE]
    )
    await select.register_select(selector, config, options=options)
    await cg.register_component(selector, config)
