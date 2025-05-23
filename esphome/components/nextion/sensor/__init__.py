from esphome import automation
import esphome.codegen as cg
from esphome.components import sensor
import esphome.config_validation as cv
from esphome.const import CONF_COMPONENT_ID, CONF_ID, CONF_STATE

from .. import CONF_NEXTION_ID, CONF_PUBLISH_STATE, CONF_SEND_TO_NEXTION, nextion_ns
from ..base_component import (
    CONF_COMPONENT_NAME,
    CONF_PRECISION,
    CONF_VARIABLE_NAME,
    CONF_WAVE_CHANNEL_ID,
    CONF_WAVE_MAX_LENGTH,
    CONF_WAVE_MAX_VALUE,
    CONF_WAVEFORM_SEND_LAST_VALUE,
    CONFIG_SENSOR_COMPONENT_SCHEMA,
    setup_component_core_,
)

CODEOWNERS = ["@senexcrenshaw"]

NextionSensor = nextion_ns.class_("NextionSensor", sensor.Sensor, cg.PollingComponent)

NextionPublishFloatAction = nextion_ns.class_(
    "NextionPublishFloatAction", automation.Action
)


def CheckWaveID(value):
    value = cv.int_(value)
    if value < 0 or value > 3:
        raise cv.Invalid(f"Valid range for {CONF_WAVE_CHANNEL_ID} is 0-3")
    return value


def _validate(config):
    if CONF_WAVE_CHANNEL_ID in config and CONF_COMPONENT_ID not in config:
        raise cv.Invalid(
            f"{CONF_COMPONENT_ID} is required when {CONF_WAVE_CHANNEL_ID} is set"
        )

    return config


CONFIG_SCHEMA = cv.All(
    sensor.sensor_schema(
        NextionSensor,
        accuracy_decimals=2,
    )
    .extend(
        {
            cv.Optional(CONF_PRECISION, default=0): cv.int_range(min=0, max=8),
            cv.Optional(CONF_WAVE_CHANNEL_ID): CheckWaveID,
            cv.Optional(CONF_COMPONENT_ID): cv.uint8_t,
            cv.Optional(CONF_WAVE_MAX_LENGTH, default=255): cv.int_range(
                min=1, max=1024
            ),
            cv.Optional(CONF_WAVE_MAX_VALUE, default=100): cv.int_range(
                min=1, max=1024
            ),
            cv.Optional(CONF_WAVEFORM_SEND_LAST_VALUE, default=True): cv.boolean,
        }
    )
    .extend(CONFIG_SENSOR_COMPONENT_SCHEMA)
    .extend(cv.polling_component_schema("never")),
    cv.has_exactly_one_key(CONF_COMPONENT_ID, CONF_COMPONENT_NAME, CONF_VARIABLE_NAME),
    _validate,
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_NEXTION_ID])
    var = cg.new_Pvariable(config[CONF_ID], hub)
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)

    cg.add(hub.register_sensor_component(var))

    await setup_component_core_(var, config, ".val")

    if CONF_PRECISION in config:
        cg.add(var.set_precision(config[CONF_PRECISION]))

    if CONF_COMPONENT_ID in config:
        cg.add(var.set_component_id(config[CONF_COMPONENT_ID]))

    if CONF_WAVE_CHANNEL_ID in config:
        cg.add(var.set_wave_channel_id(config[CONF_WAVE_CHANNEL_ID]))

    if CONF_WAVEFORM_SEND_LAST_VALUE in config:
        cg.add(var.set_waveform_send_last_value(config[CONF_WAVEFORM_SEND_LAST_VALUE]))

    if CONF_WAVE_MAX_VALUE in config:
        cg.add(var.set_wave_max_value(config[CONF_WAVE_MAX_VALUE]))

    if CONF_WAVE_MAX_LENGTH in config:
        cg.add(var.set_wave_max_length(config[CONF_WAVE_MAX_LENGTH]))


@automation.register_action(
    "sensor.nextion.publish",
    NextionPublishFloatAction,
    cv.Schema(
        {
            cv.Required(CONF_ID): cv.use_id(NextionSensor),
            cv.Required(CONF_STATE): cv.templatable(cv.float_),
            cv.Optional(CONF_PUBLISH_STATE, default="true"): cv.templatable(cv.boolean),
            cv.Optional(CONF_SEND_TO_NEXTION, default="true"): cv.templatable(
                cv.boolean
            ),
        }
    ),
)
async def sensor_nextion_publish_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(action_id, template_arg, paren)

    template_ = await cg.templatable(config[CONF_STATE], args, float)
    cg.add(var.set_state(template_))

    template_ = await cg.templatable(config[CONF_PUBLISH_STATE], args, bool)
    cg.add(var.set_publish_state(template_))

    template_ = await cg.templatable(config[CONF_SEND_TO_NEXTION], args, bool)
    cg.add(var.set_send_to_nextion(template_))

    return var
