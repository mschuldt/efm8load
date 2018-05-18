
# This file is part of efm8load. efm8load is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

def define_devices():

    Device( 0x30,'EFM8BB1',
            Variant( 0x01, "EFM8BB10F8G_QSOP24", 8 ),
            Variant( 0x02, "EFM8BB10F8G_QFN20", 8 ),
            Variant( 0x03, "EFM8BB10F8G_SOIC16", 8 ),
            Variant( 0x05, "EFM8BB10F4G_QFN20", 4 ),
            Variant( 0x08, "EFM8BB10F2G_QFN20", 2 ),
            Variant( 0x12, "EFM8BB10F8I_QFN20", 8 ),
    )

    Device( 0x32, "EFM8BB2",
            Variant( 0x01, "EFM8BB22F16G_QFN28", 16 ),
            Variant( 0x02, "EFM8BB21F16G_QSOP24", 16 ),
            Variant( 0x03, "EFM8BB21F16G_QFN20", 16 ),
    )

    Device( 0x34,"EFM8BB3",
            Variant( 0x01, "EFM8BB31F64G_QFN32", 64 ),
            Variant( 0x02, "EFM8BB31F64G_QFP32", 64 ),
            Variant( 0x03, "EFM8BB31F64G_QSOP24", 64 ),
            Variant( 0x04, "EFM8BB31F64G_QFN24", 64 ),
            Variant( 0x05, "EFM8BB31F32G_QFN32", 32 ),
            Variant( 0x06, "EFM8BB31F32G_QFP32", 32 ),
            Variant( 0x07, "EFM8BB31F32G_QSOP24", 32 ),
            Variant( 0x08, "EFM8BB31F32G_QFN24", 32 ),
            Variant( 0x09, "EFM8BB31F16G_QFN32", 16 ),
            Variant( 0x0A, "EFM8BB31F16G_QFP32", 16 ),
            Variant( 0x0B, "EFM8BB31F16G_QSOP24", 16 ),
            Variant( 0x0C, "EFM8BB31F16G_QFN24", 16 ),
            Variant( 0x11, "EFM8BB31F64I_QFN32", 64 ),
            Variant( 0x12, "EFM8BB31F64I_QFP32", 64 ),
            Variant( 0x13, "EFM8BB31F64I_QSOP24", 64 ),
            Variant( 0x14, "EFM8BB31F64I_QFN24", 64 ),
            Variant( 0x15, "EFM8BB31F32I_QFN32", 32 ),
            Variant( 0x16, "EFM8BB31F32I_QFP32", 32 ),
            Variant( 0x17, "EFM8BB31F32I_QSOP24", 32 ),
            Variant( 0x18, "EFM8BB31F32I_QFN24", 32 ),
            Variant( 0x19, "EFM8BB31F16I_QFN32", 16 ),
            Variant( 0x1A, "EFM8BB31F16I_QFP32", 16 ),
            Variant( 0x1B, "EFM8BB31F16I_QSOP24", 16 ),
            Variant( 0x1C, "EFM8BB31F16I_QFN24", 16 ),
            Variant( 0x21, "EFM8BB31F64A_QFN32", 64 ),
            Variant( 0x22, "EFM8BB31F64A_QFP32", 64 ),
            Variant( 0x23, "EFM8BB31F64A_QSOP24", 64 ),
            Variant( 0x24, "EFM8BB31F64A_QFN24", 64 ),
            Variant( 0x25, "EFM8BB31F32A_QFN32", 32 ),
            Variant( 0x26, "EFM8BB31F32A_QFP32", 32 ),
            Variant( 0x27, "EFM8BB31F32A_QSOP24", 32 ),
            Variant( 0x28, "EFM8BB31F32A_QFN24", 32 ),
            Variant( 0x29, "EFM8BB31F16A_QFN32", 16 ),
            Variant( 0x2A, "EFM8BB31F16A_QFP32", 16 ),
            Variant( 0x2B, "EFM8BB31F16A_QSOP24", 16 ),
            Variant( 0x2C, "EFM8BB31F16A_QFN24", 16 ),
    )

devices = []

class Variant:
    def __init__(self, id, name, flash_size, page_size=512, security_page_size=512):
        self.name = name,
        self.id = id
        self.flash_size = flash_size*1024
        self.flash_page_size = page_size
        self.security_page_size = security_page_size

class Device:
    def __init__(self, id, name, *variants ):
        self.name = name
        self.id = id
        self.variants = variants
        devices.append(self)

define_devices()
