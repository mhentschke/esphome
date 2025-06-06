from esphome.components.spi import TYPE_OCTAL

from .. import MODE_RGB
from . import DriverChip, delay
from .commands import (
    ADJCTL3,
    CSCON,
    DFUNCTR,
    ETMOD,
    FRMCTR1,
    FRMCTR2,
    FRMCTR3,
    GAMMASET,
    GMCTR,
    GMCTRN1,
    GMCTRP1,
    IDMOFF,
    IFCTR,
    IFMODE,
    INVCTR,
    NORON,
    PWCTR1,
    PWCTR2,
    PWCTR3,
    PWCTR4,
    PWCTR5,
    PWSET,
    PWSETN,
    SETEXTC,
    SWRESET,
    VMCTR,
    VMCTR1,
    VMCTR2,
    VSCRSADD,
)

DriverChip(
    "M5CORE",
    width=320,
    height=240,
    cs_pin=14,
    dc_pin=27,
    reset_pin=33,
    initsequence=(
        (SETEXTC, 0xFF, 0x93, 0x42),
        (PWCTR1, 0x12, 0x12),
        (PWCTR2, 0x03),
        (VMCTR1, 0xF2),
        (IFMODE, 0xE0),
        (0xF6, 0x01, 0x00, 0x00),
        (
            GMCTRP1,
            0x00,
            0x0C,
            0x11,
            0x04,
            0x11,
            0x08,
            0x37,
            0x89,
            0x4C,
            0x06,
            0x0C,
            0x0A,
            0x2E,
            0x34,
            0x0F,
        ),
        (
            GMCTRN1,
            0x00,
            0x0B,
            0x11,
            0x05,
            0x13,
            0x09,
            0x33,
            0x67,
            0x48,
            0x07,
            0x0E,
            0x0B,
            0x2E,
            0x33,
            0x0F,
        ),
        (DFUNCTR, 0x08, 0x82, 0x1D, 0x04),
        (IDMOFF,),
    ),
)
ILI9341 = DriverChip(
    "ILI9341",
    mirror_x=True,
    width=240,
    height=320,
    initsequence=(
        (0xEF, 0x03, 0x80, 0x02),
        (0xCF, 0x00, 0xC1, 0x30),
        (0xED, 0x64, 0x03, 0x12, 0x81),
        (0xE8, 0x85, 0x00, 0x78),
        (0xCB, 0x39, 0x2C, 0x00, 0x34, 0x02),
        (0xF7, 0x20),
        (0xEA, 0x00, 0x00),
        (PWCTR1, 0x23),
        (PWCTR2, 0x10),
        (VMCTR1, 0x3E, 0x28),
        (VMCTR2, 0x86),
        (VSCRSADD, 0x00),
        (FRMCTR1, 0x00, 0x18),
        (DFUNCTR, 0x08, 0x82, 0x27),
        (0xF2, 0x00),
        (GAMMASET, 0x01),
        (
            GMCTRP1,
            0x0F,
            0x31,
            0x2B,
            0x0C,
            0x0E,
            0x08,
            0x4E,
            0xF1,
            0x37,
            0x07,
            0x10,
            0x03,
            0x0E,
            0x09,
            0x00,
        ),
        (
            GMCTRN1,
            0x00,
            0x0E,
            0x14,
            0x03,
            0x11,
            0x07,
            0x31,
            0xC1,
            0x48,
            0x08,
            0x0F,
            0x0C,
            0x31,
            0x36,
            0x0F,
        ),
    ),
)
DriverChip(
    "ILI9481",
    mirror_x=True,
    width=320,
    height=480,
    use_axis_flips=True,
    initsequence=(
        (PWSET, 0x07, 0x42, 0x18),
        (VMCTR, 0x00, 0x07, 0x10),
        (PWSETN, 0x01, 0x02),
        (PWCTR1, 0x10, 0x3B, 0x00, 0x02, 0x11),
        (VMCTR1, 0x03),
        (IFCTR, 0x83),
        (GMCTR, 0x32, 0x36, 0x45, 0x06, 0x16, 0x37, 0x75, 0x77, 0x54, 0x0C, 0x00),
    ),
)
DriverChip(
    "ILI9486",
    mirror_x=True,
    width=320,
    height=480,
    initsequence=(
        (PWCTR3, 0x44),
        (VMCTR1, 0x00, 0x00, 0x00, 0x00),
        (
            GMCTRP1,
            0x0F,
            0x1F,
            0x1C,
            0x0C,
            0x0F,
            0x08,
            0x48,
            0x98,
            0x37,
            0x0A,
            0x13,
            0x04,
            0x11,
            0x0D,
            0x00,
        ),
        (
            GMCTRN1,
            0x0F,
            0x32,
            0x2E,
            0x0B,
            0x0D,
            0x05,
            0x47,
            0x75,
            0x37,
            0x06,
            0x10,
            0x03,
            0x24,
            0x20,
            0x00,
        ),
    ),
)
DriverChip(
    "ILI9488",
    width=320,
    height=480,
    pixel_mode="18bit",
    initsequence=(
        (
            GMCTRP1,
            0x0F,
            0x24,
            0x1C,
            0x0A,
            0x0F,
            0x08,
            0x43,
            0x88,
            0x32,
            0x0F,
            0x10,
            0x06,
            0x0F,
            0x07,
            0x00,
        ),
        (
            GMCTRN1,
            0x0F,
            0x38,
            0x30,
            0x09,
            0x0F,
            0x0F,
            0x4E,
            0x77,
            0x3C,
            0x07,
            0x10,
            0x05,
            0x23,
            0x1B,
            0x00,
        ),
        (PWCTR1, 0x17, 0x15),
        (PWCTR2, 0x41),
        (VMCTR1, 0x00, 0x12, 0x80),
        (IFMODE, 0x00),
        (FRMCTR1, 0xA0),
        (INVCTR, 0x02),
        (0xE9, 0x00),
        (ADJCTL3, 0xA9, 0x51, 0x2C, 0x82),
    ),
)
ILI9488_A = DriverChip(
    "ILI9488_A",
    width=320,
    height=480,
    invert_colors=False,
    pixel_mode="18bit",
    mirror_x=True,
    initsequence=(
        (
            GMCTRP1,
            0x00,
            0x03,
            0x09,
            0x08,
            0x16,
            0x0A,
            0x3F,
            0x78,
            0x4C,
            0x09,
            0x0A,
            0x08,
            0x16,
            0x1A,
            0x0F,
        ),
        (
            GMCTRN1,
            0x00,
            0x16,
            0x19,
            0x03,
            0x0F,
            0x05,
            0x32,
            0x45,
            0x46,
            0x04,
            0x0E,
            0x0D,
            0x35,
            0x37,
            0x0F,
        ),
        (PWCTR1, 0x17, 0x15),
        (PWCTR2, 0x41),
        (VMCTR1, 0x00, 0x12, 0x80),
        (IFMODE, 0x00),
        (FRMCTR1, 0xA0),
        (INVCTR, 0x02),
        (DFUNCTR, 0x02, 0x02),
        (0xE9, 0x00),
        (ADJCTL3, 0xA9, 0x51, 0x2C, 0x82),
    ),
)
ST7796 = DriverChip(
    "ST7796",
    mirror_x=True,
    width=320,
    height=480,
    initsequence=(
        (SWRESET,),
        (CSCON, 0xC3),
        (CSCON, 0x96),
        (VMCTR1, 0x1C),
        (IFMODE, 0x80),
        (INVCTR, 0x01),
        (DFUNCTR, 0x80, 0x02, 0x3B),
        (ETMOD, 0xC6),
        (CSCON, 0x69),
        (CSCON, 0x3C),
    ),
)
DriverChip(
    "S3BOX",
    width=320,
    height=240,
    mirror_x=True,
    mirror_y=True,
    invert_colors=False,
    data_rate="40MHz",
    dc_pin=4,
    cs_pin=5,
    # reset_pin={CONF_INVERTED: True, CONF_NUMBER: 48},
    initsequence=(
        (0xEF, 0x03, 0x80, 0x02),
        (0xCF, 0x00, 0xC1, 0x30),
        (0xED, 0x64, 0x03, 0x12, 0x81),
        (0xE8, 0x85, 0x00, 0x78),
        (0xCB, 0x39, 0x2C, 0x00, 0x34, 0x02),
        (0xF7, 0x20),
        (0xEA, 0x00, 0x00),
        (PWCTR1, 0x23),
        (PWCTR2, 0x10),
        (VMCTR1, 0x3E, 0x28),
        (VMCTR2, 0x86),
        (VSCRSADD, 0x00),
        (FRMCTR1, 0x00, 0x18),
        (DFUNCTR, 0x08, 0x82, 0x27),
        (0xF2, 0x00),
        (GAMMASET, 0x01),
        (
            GMCTRP1,
            0x0F,
            0x31,
            0x2B,
            0x0C,
            0x0E,
            0x08,
            0x4E,
            0xF1,
            0x37,
            0x07,
            0x10,
            0x03,
            0x0E,
            0x09,
            0x00,
        ),
        (
            GMCTRN1,
            0x00,
            0x0E,
            0x14,
            0x03,
            0x11,
            0x07,
            0x31,
            0xC1,
            0x48,
            0x08,
            0x0F,
            0x0C,
            0x31,
            0x36,
            0x0F,
        ),
    ),
)
DriverChip(
    "S3BOXLITE",
    mirror_x=True,
    color_order=MODE_RGB,
    width=320,
    height=240,
    cs_pin=5,
    dc_pin=4,
    reset_pin=48,
    initsequence=(
        (0xEF, 0x03, 0x80, 0x02),
        (0xCF, 0x00, 0xC1, 0x30),
        (0xED, 0x64, 0x03, 0x12, 0x81),
        (0xE8, 0x85, 0x00, 0x78),
        (0xCB, 0x39, 0x2C, 0x00, 0x34, 0x02),
        (0xF7, 0x20),
        (0xEA, 0x00, 0x00),
        (PWCTR1, 0x23),
        (PWCTR2, 0x10),
        (VMCTR1, 0x3E, 0x28),
        (VMCTR2, 0x86),
        (VSCRSADD, 0x00),
        (FRMCTR1, 0x00, 0x18),
        (DFUNCTR, 0x08, 0x82, 0x27),
        (0xF2, 0x00),
        (GAMMASET, 0x01),
        (
            GMCTRP1,
            0xF0,
            0x09,
            0x0B,
            0x06,
            0x04,
            0x15,
            0x2F,
            0x54,
            0x42,
            0x3C,
            0x17,
            0x14,
            0x18,
            0x1B,
        ),
        (
            GMCTRN1,
            0xE0,
            0x09,
            0x0B,
            0x06,
            0x04,
            0x03,
            0x2B,
            0x43,
            0x42,
            0x3B,
            0x16,
            0x14,
            0x17,
            0x1B,
        ),
    ),
)
ST7789V = DriverChip(
    "ST7789V",
    width=240,
    height=320,
    initsequence=(
        (DFUNCTR, 0x0A, 0x82),
        (FRMCTR2, 0x0C, 0x0C, 0x00, 0x33, 0x33),
        (ETMOD, 0x35),
        (0xBB, 0x28),
        (PWCTR1, 0x0C),
        (PWCTR3, 0x01, 0xFF),
        (PWCTR4, 0x10),
        (PWCTR5, 0x20),
        (IFCTR, 0x0F),
        (PWSET, 0xA4, 0xA1),
        (
            GMCTRP1,
            0xD0,
            0x00,
            0x02,
            0x07,
            0x0A,
            0x28,
            0x32,
            0x44,
            0x42,
            0x06,
            0x0E,
            0x12,
            0x14,
            0x17,
        ),
        (
            GMCTRN1,
            0xD0,
            0x00,
            0x02,
            0x07,
            0x0A,
            0x28,
            0x31,
            0x54,
            0x47,
            0x0E,
            0x1C,
            0x17,
            0x1B,
            0x1E,
        ),
    ),
)
DriverChip(
    "GC9A01A",
    mirror_x=True,
    width=240,
    height=240,
    initsequence=(
        (0xEF,),
        (0xEB, 0x14),
        (0xFE,),
        (0xEF,),
        (0xEB, 0x14),
        (0x84, 0x40),
        (0x85, 0xFF),
        (0x86, 0xFF),
        (0x87, 0xFF),
        (0x88, 0x0A),
        (0x89, 0x21),
        (0x8A, 0x00),
        (0x8B, 0x80),
        (0x8C, 0x01),
        (0x8D, 0x01),
        (0x8E, 0xFF),
        (0x8F, 0xFF),
        (0xB6, 0x00, 0x00),
        (0x90, 0x08, 0x08, 0x08, 0x08),
        (0xBD, 0x06),
        (0xBC, 0x00),
        (0xFF, 0x60, 0x01, 0x04),
        (0xC3, 0x13),
        (0xC4, 0x13),
        (0xF9, 0x22),
        (0xBE, 0x11),
        (0xE1, 0x10, 0x0E),
        (0xDF, 0x21, 0x0C, 0x02),
        (0xF0, 0x45, 0x09, 0x08, 0x08, 0x26, 0x2A),
        (0xF1, 0x43, 0x70, 0x72, 0x36, 0x37, 0x6F),
        (0xF2, 0x45, 0x09, 0x08, 0x08, 0x26, 0x2A),
        (0xF3, 0x43, 0x70, 0x72, 0x36, 0x37, 0x6F),
        (0xED, 0x1B, 0x0B),
        (0xAE, 0x77),
        (0xCD, 0x63),
        (0xE8, 0x34),
        (
            0x62,
            0x18,
            0x0D,
            0x71,
            0xED,
            0x70,
            0x70,
            0x18,
            0x0F,
            0x71,
            0xEF,
            0x70,
            0x70,
        ),
        (
            0x63,
            0x18,
            0x11,
            0x71,
            0xF1,
            0x70,
            0x70,
            0x18,
            0x13,
            0x71,
            0xF3,
            0x70,
            0x70,
        ),
        (0x64, 0x28, 0x29, 0xF1, 0x01, 0xF1, 0x00, 0x07),
        (0x66, 0x3C, 0x00, 0xCD, 0x67, 0x45, 0x45, 0x10, 0x00, 0x00, 0x00),
        (0x67, 0x00, 0x3C, 0x00, 0x00, 0x00, 0x01, 0x54, 0x10, 0x32, 0x98),
        (0x74, 0x10, 0x85, 0x80, 0x00, 0x00, 0x4E, 0x00),
        (0x98, 0x3E, 0x07),
        (0x35,),
    ),
)
DriverChip(
    "GC9D01N",
    width=160,
    height=160,
    initsequence=(
        (0xFE,),
        (0xEF,),
        (0x80, 0xFF),
        (0x81, 0xFF),
        (0x82, 0xFF),
        (0x83, 0xFF),
        (0x84, 0xFF),
        (0x85, 0xFF),
        (0x86, 0xFF),
        (0x87, 0xFF),
        (0x88, 0xFF),
        (0x89, 0xFF),
        (0x8A, 0xFF),
        (0x8B, 0xFF),
        (0x8C, 0xFF),
        (0x8D, 0xFF),
        (0x8E, 0xFF),
        (0x8F, 0xFF),
        (0x3A, 0x05),
        (0xEC, 0x01),
        (0x74, 0x02, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00),
        (0x98, 0x3E),
        (0x99, 0x3E),
        (0xB5, 0x0D, 0x0D),
        (0x60, 0x38, 0x0F, 0x79, 0x67),
        (0x61, 0x38, 0x11, 0x79, 0x67),
        (0x64, 0x38, 0x17, 0x71, 0x5F, 0x79, 0x67),
        (0x65, 0x38, 0x13, 0x71, 0x5B, 0x79, 0x67),
        (0x6A, 0x00, 0x00),
        (0x6C, 0x22, 0x02, 0x22, 0x02, 0x22, 0x22, 0x50),
        (
            0x6E,
            0x03,
            0x03,
            0x01,
            0x01,
            0x00,
            0x00,
            0x0F,
            0x0F,
            0x0D,
            0x0D,
            0x0B,
            0x0B,
            0x09,
            0x09,
            0x00,
            0x00,
            0x00,
            0x00,
            0x0A,
            0x0A,
            0x0C,
            0x0C,
            0x0E,
            0x0E,
            0x10,
            0x10,
            0x00,
            0x00,
            0x02,
            0x02,
            0x04,
            0x04,
        ),
        (0xBF, 0x01),
        (0xF9, 0x40),
        (0x9B, 0x3B, 0x93, 0x33, 0x7F, 0x00),
        (0x7E, 0x30),
        (0x70, 0x0D, 0x02, 0x08, 0x0D, 0x02, 0x08),
        (0x71, 0x0D, 0x02, 0x08),
        (0x91, 0x0E, 0x09),
        (0xC3, 0x19, 0xC4, 0x19, 0xC9, 0x3C),
        (0xF0, 0x53, 0x15, 0x0A, 0x04, 0x00, 0x3E),
        (0xF1, 0x56, 0xA8, 0x7F, 0x33, 0x34, 0x5F),
        (0xF2, 0x53, 0x15, 0x0A, 0x04, 0x00, 0x3A),
        (0xF3, 0x52, 0xA4, 0x7F, 0x33, 0x34, 0xDF),
    ),
)
DriverChip(
    "ST7735",
    color_order=MODE_RGB,
    width=128,
    height=160,
    initsequence=(
        SWRESET,
        delay(10),
        (FRMCTR1, 0x01, 0x2C, 0x2D),
        (FRMCTR2, 0x01, 0x2C, 0x2D),
        (FRMCTR3, 0x01, 0x2C, 0x2D, 0x01, 0x2C, 0x2D),
        (INVCTR, 0x07),
        (PWCTR1, 0xA2, 0x02, 0x84),
        (PWCTR2, 0xC5),
        (PWCTR3, 0x0A, 0x00),
        (PWCTR4, 0x8A, 0x2A),
        (PWCTR5, 0x8A, 0xEE),
        (VMCTR1, 0x0E),
        (
            GMCTRP1,
            0x02,
            0x1C,
            0x07,
            0x12,
            0x37,
            0x32,
            0x29,
            0x2D,
            0x29,
            0x25,
            0x2B,
            0x39,
            0x00,
            0x01,
            0x03,
            0x10,
        ),
        (
            GMCTRN1,
            0x03,
            0x1D,
            0x07,
            0x06,
            0x2E,
            0x2C,
            0x29,
            0x2D,
            0x2E,
            0x2E,
            0x37,
            0x3F,
            0x00,
            0x00,
            0x02,
            0x10,
        ),
        NORON,
    ),
)
ST7796.extend(
    "WT32-SC01-PLUS",
    bus_mode=TYPE_OCTAL,
    mirror_x=True,
    reset_pin=4,
    dc_pin=0,
    invert_colors=True,
)

models = {}
