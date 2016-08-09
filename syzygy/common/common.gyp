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
      'target_name': 'common_lib',
      'type': 'static_library',
      'sources': [
        'align.cc',
        'align.h',
        'align_impl.h',
        'asan_parameters.cc',
        'asan_parameters.h',
        'assertions.h',
        'binary_stream.cc',
        'binary_stream.h',
        'buffer_parser.cc',
        'buffer_parser.h',
        'buffer_parser_impl.h',
        'buffer_writer.cc',
        'buffer_writer.h',
        'com_utils.cc',
        'com_utils.h',
        'comparable.h',
        'dbghelp_util.cc',
        'dbghelp_util.h',
        'defs.cc',
        'defs.h',
        'indexed_frequency_data.cc',
        'indexed_frequency_data.h',
        'logging.cc',
        'logging.h',
        'path_util.cc',
        'path_util.h',
        'process_utils.cc',
        'process_utils.h',
        'recursive_lock.cc',
        'recursive_lock.h',
      ],
      'defines': [
        # This is required for ATL to use XP-safe versions of its functions.
        '_USING_V110_SDK71_',
      ],
    },
  ],
}
