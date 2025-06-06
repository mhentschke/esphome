from esphome.components.spi import TYPE_QUAD
import esphome.config_validation as cv
from esphome.const import CONF_IGNORE_STRAPPING_WARNING, CONF_NUMBER

from .. import MODE_RGB
from . import DriverChip

AXS15231 = DriverChip(
    "AXS15231",
    draw_rounding=8,
    swap_xy=cv.UNDEFINED,
    color_order=MODE_RGB,
    bus_mode=TYPE_QUAD,
    initsequence=(
        (0xBB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5A, 0xA5),
        (0xC1, 0x33),
        (0xBB, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),
    ),
)

AXS15231.extend(
    "JC3248W535",
    width=320,
    height=480,
    cs_pin={CONF_NUMBER: 45, CONF_IGNORE_STRAPPING_WARNING: True},
    data_rate="40MHz",
)

DriverChip(
    "JC3636W518",
    height=360,
    width=360,
    offset_height=1,
    draw_rounding=1,
    cs_pin=10,
    reset_pin=47,
    invert_colors=True,
    color_order=MODE_RGB,
    bus_mode=TYPE_QUAD,
    data_rate="40MHz",
    initsequence=(
        (0xF0, 0x08),
        (0xF2, 0x08),
        (0x9B, 0x51),
        (0x86, 0x53),
        (0xF2, 0x80),
        (0xF0, 0x00),
        (0xF0, 0x01),
        (0xF1, 0x01),
        (0xB0, 0x54),
        (0xB1, 0x3F),
        (0xB2, 0x2A),
        (0xB4, 0x46),
        (0xB5, 0x34),
        (0xB6, 0xD5),
        (0xB7, 0x30),
        (0xBA, 0x00),
        (0xBB, 0x08),
        (0xBC, 0x08),
        (0xBD, 0x00),
        (0xC0, 0x80),
        (0xC1, 0x10),
        (0xC2, 0x37),
        (0xC3, 0x80),
        (0xC4, 0x10),
        (0xC5, 0x37),
        (0xC6, 0xA9),
        (0xC7, 0x41),
        (0xC8, 0x51),
        (0xC9, 0xA9),
        (0xCA, 0x41),
        (0xCB, 0x51),
        (0xD0, 0x91),
        (0xD1, 0x68),
        (0xD2, 0x69),
        (0xF5, 0x00, 0xA5),
        (0xDD, 0x3F),
        (0xDE, 0x3F),
        (0xF1, 0x10),
        (0xF0, 0x00),
        (0xF0, 0x02),
        (
            0xE0,
            0x70,
            0x09,
            0x12,
            0x0C,
            0x0B,
            0x27,
            0x38,
            0x54,
            0x4E,
            0x19,
            0x15,
            0x15,
            0x2C,
            0x2F,
        ),
        (
            0xE1,
            0x70,
            0x08,
            0x11,
            0x0C,
            0x0B,
            0x27,
            0x38,
            0x43,
            0x4C,
            0x18,
            0x14,
            0x14,
            0x2B,
            0x2D,
        ),
        (0xF0, 0x10),
        (0xF3, 0x10),
        (0xE0, 0x08),
        (0xE1, 0x00),
        (0xE2, 0x00),
        (0xE3, 0x00),
        (0xE4, 0xE0),
        (0xE5, 0x06),
        (0xE6, 0x21),
        (0xE7, 0x00),
        (0xE8, 0x05),
        (0xE9, 0x82),
        (0xEA, 0xDF),
        (0xEB, 0x89),
        (0xEC, 0x20),
        (0xED, 0x14),
        (0xEE, 0xFF),
        (0xEF, 0x00),
        (0xF8, 0xFF),
        (0xF9, 0x00),
        (0xFA, 0x00),
        (0xFB, 0x30),
        (0xFC, 0x00),
        (0xFD, 0x00),
        (0xFE, 0x00),
        (0xFF, 0x00),
        (0x60, 0x42),
        (0x61, 0xE0),
        (0x62, 0x40),
        (0x63, 0x40),
        (0x64, 0x02),
        (0x65, 0x00),
        (0x66, 0x40),
        (0x67, 0x03),
        (0x68, 0x00),
        (0x69, 0x00),
        (0x6A, 0x00),
        (0x6B, 0x00),
        (0x70, 0x42),
        (0x71, 0xE0),
        (0x72, 0x40),
        (0x73, 0x40),
        (0x74, 0x02),
        (0x75, 0x00),
        (0x76, 0x40),
        (0x77, 0x03),
        (0x78, 0x00),
        (0x79, 0x00),
        (0x7A, 0x00),
        (0x7B, 0x00),
        (0x80, 0x48),
        (0x81, 0x00),
        (0x82, 0x05),
        (0x83, 0x02),
        (0x84, 0xDD),
        (0x85, 0x00),
        (0x86, 0x00),
        (0x87, 0x00),
        (0x88, 0x48),
        (0x89, 0x00),
        (0x8A, 0x07),
        (0x8B, 0x02),
        (0x8C, 0xDF),
        (0x8D, 0x00),
        (0x8E, 0x00),
        (0x8F, 0x00),
        (0x90, 0x48),
        (0x91, 0x00),
        (0x92, 0x09),
        (0x93, 0x02),
        (0x94, 0xE1),
        (0x95, 0x00),
        (0x96, 0x00),
        (0x97, 0x00),
        (0x98, 0x48),
        (0x99, 0x00),
        (0x9A, 0x0B),
        (0x9B, 0x02),
        (0x9C, 0xE3),
        (0x9D, 0x00),
        (0x9E, 0x00),
        (0x9F, 0x00),
        (0xA0, 0x48),
        (0xA1, 0x00),
        (0xA2, 0x04),
        (0xA3, 0x02),
        (0xA4, 0xDC),
        (0xA5, 0x00),
        (0xA6, 0x00),
        (0xA7, 0x00),
        (0xA8, 0x48),
        (0xA9, 0x00),
        (0xAA, 0x06),
        (0xAB, 0x02),
        (0xAC, 0xDE),
        (0xAD, 0x00),
        (0xAE, 0x00),
        (0xAF, 0x00),
        (0xB0, 0x48),
        (0xB1, 0x00),
        (0xB2, 0x08),
        (0xB3, 0x02),
        (0xB4, 0xE0),
        (0xB5, 0x00),
        (0xB6, 0x00),
        (0xB7, 0x00),
        (0xB8, 0x48),
        (0xB9, 0x00),
        (0xBA, 0x0A),
        (0xBB, 0x02),
        (0xBC, 0xE2),
        (0xBD, 0x00),
        (0xBE, 0x00),
        (0xBF, 0x00),
        (0xC0, 0x12),
        (0xC1, 0xAA),
        (0xC2, 0x65),
        (0xC3, 0x74),
        (0xC4, 0x47),
        (0xC5, 0x56),
        (0xC6, 0x00),
        (0xC7, 0x88),
        (0xC8, 0x99),
        (0xC9, 0x33),
        (0xD0, 0x21),
        (0xD1, 0xAA),
        (0xD2, 0x65),
        (0xD3, 0x74),
        (0xD4, 0x47),
        (0xD5, 0x56),
        (0xD6, 0x00),
        (0xD7, 0x88),
        (0xD8, 0x99),
        (0xD9, 0x33),
        (0xF3, 0x01),
        (0xF0, 0x00),
        (0xF0, 0x01),
        (0xF1, 0x01),
        (0xA0, 0x0B),
        (0xA3, 0x2A),
        (0xA5, 0xC3),
    ),
)

models = {}
