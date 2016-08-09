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
    '../../syzygy.gypi',
  ],
  'targets': [
    {
      'target_name': 'block_graph_transforms_lib',
      'type': 'static_library',
      'sources': [
        'chained_basic_block_transforms.cc',
        'chained_basic_block_transforms.h',
        'fuzzing_transform.cc',
        'fuzzing_transform.h',
        'iterative_transform.h',
        'named_transform.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(src)/syzygy/block_graph/analysis/block_graph_analysis.gyp:'
            'block_graph_analysis_lib',
        '<(src)/syzygy/block_graph/block_graph.gyp:block_graph_lib',
        '<(src)/syzygy/common/common.gyp:common_lib',
        '<(src)/syzygy/core/core.gyp:core_lib',
      ],
    },
  ],
}
