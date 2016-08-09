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
      'target_name': 'block_graph_lib',
      'type': 'static_library',
      'sources': [
        'basic_block.cc',
        'basic_block.h',
        'basic_block_assembler.cc',
        'basic_block_assembler.h',
        'basic_block_decomposer.cc',
        'basic_block_decomposer.h',
        'basic_block_subgraph.cc',
        'basic_block_subgraph.h',
        'block_builder.cc',
        'block_builder.h',
        'block_graph.cc',
        'block_graph.h',
        'block_graph_serializer.cc',
        'block_graph_serializer.h',
        'block_hash.cc',
        'block_hash.h',
        'block_util.cc',
        'block_util.h',
        'filter_util.cc',
        'filter_util.h',
        'filterable.cc',
        'filterable.h',
        'hot_patching_metadata.h',
        'iterate.cc',
        'iterate.h',
        'ordered_block_graph.cc',
        'ordered_block_graph.h',
        'ordered_block_graph_internal.h',
        'orderer.cc',
        'orderer.h',
        'tags.h',
        'transform.cc',
        'transform.h',
        'transform_policy.h',
        'typed_block.h',
        'typed_block_internal.h',
      ],
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(src)/syzygy/common/common.gyp:common_lib',
        '<(src)/syzygy/core/core.gyp:core_lib',
      ],
    },
  ],
}
