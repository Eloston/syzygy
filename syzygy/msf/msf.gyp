# Copyright 2015 Google Inc. All Rights Reserved.
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
      'target_name': 'msf_lib',
      'type': 'static_library',
      'sources': [
        'msf_byte_stream.h',
        'msf_byte_stream_impl.h',
        'msf_constants.cc',
        'msf_constants.h',
        'msf_data.h',
        'msf_decl.h',
        'msf_file.h',
        'msf_file_impl.h',
        'msf_file_stream.h',
        'msf_file_stream_impl.h',
        'msf_reader.h',
        'msf_reader_impl.h',
        'msf_stream.h',
        'msf_stream_impl.h',
        'msf_writer.h',
        'msf_writer_impl.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(src)/syzygy/common/common.gyp:common_lib',
      ],
    },
  ],
}
