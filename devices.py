
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

devices = {
     # DEVICE_ID : [ NAME, { DICT OF VARIANT_IDS } ]
     #            VARIANT_ID: VARIANT_NAME, FLASH_SIZE, PAGE_SIZE, SECURITY_PAGE_SIZE]
     0x16 : ["EFM8SB2", { } ],
     0x30 : ["EFM8BB1", {
         0x01: ["EFM8BB10F8G_QSOP24", 8*1024, 512, 512 ],
         0x02: ["EFM8BB10F8G_QFN20" , 8*1024, 512, 512 ],
         0x03: ["EFM8BB10F8G_SOIC16", 8*1024, 512, 512 ],
         0x05: ["EFM8BB10F4G_QFN20" , 4*1024, 512, 512 ],
         0x08: ["EFM8BB10F2G_QFN20" , 2*1024, 512, 512 ],
         0x12: ["EFM8BB10F8I_QFN20" , 8*1024, 512, 521 ]
     }],
     0x32 : ["EFM8BB2", {
         0x01: ["EFM8BB22F16G_QFN28" , 16*1024, 512, 512],
         0x02: ["EFM8BB21F16G_QSOP24", 16*1024, 512, 512],
         0x03: ["EFM8BB21F16G_QFN20" , 16*1024, 512, 512]
     }]
 }
