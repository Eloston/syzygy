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
      'target_name': 'pdb_lib',
      'type': 'static_library',
      'sources': [
        'gen/pdb_type_info_records.cc',
        'gen/pdb_type_info_records.h',
        'mutators/add_named_stream_mutator.h',
        'mutators/named_mutator.h',
        'omap.cc',
        'omap.h',
        'pdb_byte_stream.h',
        'pdb_constants.cc',
        'pdb_constants.h',
        'pdb_data.cc',
        'pdb_data.h',
        'pdb_data_types.h',
        'pdb_dbi_stream.cc',
        'pdb_dbi_stream.h',
        'pdb_decl.h',
        'pdb_file.h',
        'pdb_file_stream.h',
        'pdb_mutator.cc',
        'pdb_mutator.h',
        'pdb_reader.h',
        'pdb_stream.h',
        'pdb_stream_reader.cc',
        'pdb_stream_reader.h',
        'pdb_stream_record.cc',
        'pdb_stream_record.h',
        'pdb_symbol_record.cc',
        'pdb_symbol_record.h',
        'pdb_type_info_stream_enum.cc',
        'pdb_type_info_stream_enum.h',
        'pdb_util.cc',
        'pdb_util.h',
        'pdb_writer.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(src)/syzygy/common/common.gyp:common_lib',
        '<(src)/syzygy/msf/msf.gyp:msf_lib',
      ],
    },
  ],
}
