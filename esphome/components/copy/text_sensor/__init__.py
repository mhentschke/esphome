import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import CONF_ENTITY_CATEGORY, CONF_ICON, CONF_SOURCE_ID
from esphome.core.entity_helpers import inherit_property_from

from .. import copy_ns

CopyTextSensor = copy_ns.class_("CopyTextSensor", text_sensor.TextSensor, cg.Component)


CONFIG_SCHEMA = (
    text_sensor.text_sensor_schema(CopyTextSensor)
    .extend(
        {
            cv.Required(CONF_SOURCE_ID): cv.use_id(text_sensor.TextSensor),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

FINAL_VALIDATE_SCHEMA = cv.All(
    inherit_property_from(CONF_ICON, CONF_SOURCE_ID),
    inherit_property_from(CONF_ENTITY_CATEGORY, CONF_SOURCE_ID),
)


async def to_code(config):
    var = await text_sensor.new_text_sensor(config)
    await cg.register_component(var, config)

    source = await cg.get_variable(config[CONF_SOURCE_ID])
    cg.add(var.set_source(source))
