# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'chromium_code': 1,
  },
  'includes': [
    '../syzygy.gypi',
  ],
  'targets': [
    {
      'target_name': 'core_lib',
      'type': 'static_library',
      'sources': [
        'address.cc',
        'address.h',
        'address_filter.h',
        'address_filter_impl.h',
        'address_range.cc',
        'address_range.h',
        'address_space.cc',
        'address_space.h',
        'address_space_internal.h',
        'disassembler.cc',
        'disassembler.h',
        'disassembler_util.cc',
        'disassembler_util.h',
        'file_util.cc',
        'file_util.h',
        'json_file_writer.cc',
        'json_file_writer.h',
        'random_number_generator.cc',
        'random_number_generator.h',
        'section_offset_address.cc',
        'section_offset_address.h',
        'serialization.cc',
        'serialization.h',
        'serialization_impl.h',
        'string_table.cc',
        'string_table.h',
        'zstream.cc',
        'zstream.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(src)/syzygy/assm/assm.gyp:assm_lib',
        '<(src)/syzygy/common/common.gyp:common_lib',
        '<(src)/third_party/distorm/distorm.gyp:distorm',
        '<(DEPTH)/third_party/zlib/zlib.gyp:zlib',
      ],
    },
  ],
}
