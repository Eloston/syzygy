# Copyright 2014 Google Inc. All Rights Reserved.
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
      'target_name': 'assm_lib',
      'type': 'static_library',
      'sources': [
        'assembler_base.h',
        'assembler_base_impl.h',
        'assembler.h',
        'buffer_serializer.h',
        'cond.h',
        'const.h',
        'label_base.h',
        'operand_base.h',
        'register_internal.h',
        'register.cc',
        'register.h',
        'value_base.h',
      ],
      'dependencies': [
        'base/base.gyp:base',
        '<(src)/syzygy/common/common.gyp:common_lib',
      ],
    },
    {
      'target_name': 'assm_unittest_utils',
      'type': 'static_library',
      'sources': [
        'unittest_util.cc',
        'unittest_util.h',
      ],
      'dependencies': [
        'base/base.gyp:base',
      ],
    },
    {
      'target_name': 'assm_unittests',
      'type': 'executable',
      'sources': [
        'assembler_unittest.cc',
        'buffer_serializer_unittest.cc',
        'register_unittest.cc',
        '<(src)/syzygy/testing/run_all_unittests.cc',
      ],
      'dependencies': [
        'assm_lib',
        'assm_unittest_utils',
        '<(src)/syzygy/core/core.gyp:core_lib',
        'base/base.gyp:base',
        'base/base.gyp:test_support_base',
        '<(src)/testing/gtest.gyp:gtest',
      ],
    },
  ],
}
