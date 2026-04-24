#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
        'device/xiaomi/mt6893-common',
        'hardware/mediatek',
        'hardware/mediatek/libmtkperf_client',
        'hardware/xiaomi'
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}


blob_fixups: blob_fixups_user_type = {
     ('vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b', 'vendor/bin/hw/vendor.dolby.hardware.dms@2.0-service'): blob_fixup()
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so')
        .add_needed('libstagefright_foundation-v33.so'),

    ('vendor/bin/hw/android.hardware.neuralnetworks@1.3-service-mtk-neuron', 'vendor/lib/libnvram.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),

    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),

    ('vendor/bin/mnld', 'vendor/lib64/libaalservice.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/lib64/mt6893/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),

    ('vendor/lib/libteei_daemon_vfs.so', 'vendor/lib64/libteei_daemon_vfs.so'): blob_fixup()
        .add_needed('liblog.so'),

    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),

    'vendor/lib/librt_extamp_intf.so': blob_fixup()
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),

    'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.13-impl.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libtinyxml2.so', 'libtinyxml2-v34.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'mt6893-common',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
