import esphome.codegen as cg
from esphome.components import output
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_PIN

from .. import CONF_SX1509_ID, SX1509Component, sx1509_ns

DEPENDENCIES = ["sx1509"]

SX1509FloatOutputChannel = sx1509_ns.class_(
    "SX1509FloatOutputChannel", output.FloatOutput, cg.Component
)

CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend(
    {
        cv.Required(CONF_ID): cv.declare_id(SX1509FloatOutputChannel),
        cv.GenerateID(CONF_SX1509_ID): cv.use_id(SX1509Component),
        cv.Required(CONF_PIN): cv.int_range(min=0, max=15),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    parent = await cg.get_variable(config[CONF_SX1509_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await output.register_output(var, config)
    cg.add(var.set_pin(config[CONF_PIN]))
    cg.add(var.set_parent(parent))
