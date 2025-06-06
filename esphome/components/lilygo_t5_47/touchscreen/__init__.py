from esphome import pins
import esphome.codegen as cg
from esphome.components import i2c, touchscreen
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_INTERRUPT_PIN

from .. import lilygo_t5_47_ns

CODEOWNERS = ["@jesserockz"]
DEPENDENCIES = ["i2c"]

LilygoT547Touchscreen = lilygo_t5_47_ns.class_(
    "LilygoT547Touchscreen",
    touchscreen.Touchscreen,
    i2c.I2CDevice,
)

CONF_LILYGO_T5_47_TOUCHSCREEN_ID = "lilygo_t5_47_touchscreen_id"

CONFIG_SCHEMA = touchscreen.touchscreen_schema("250ms").extend(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(LilygoT547Touchscreen),
            cv.Required(CONF_INTERRUPT_PIN): cv.All(
                pins.internal_gpio_input_pin_schema
            ),
        }
    ).extend(i2c.i2c_device_schema(0x5A))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await touchscreen.register_touchscreen(var, config)
    await i2c.register_i2c_device(var, config)

    interrupt_pin = await cg.gpio_pin_expression(config[CONF_INTERRUPT_PIN])
    cg.add(var.set_interrupt_pin(interrupt_pin))
