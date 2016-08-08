# This is a dependency for gyp_chromium to build swapimport.exe for use in import reordering

{
  'targets': [
    {
      'target_name': 'syzygy_swapimport',
      'type': 'none',
      'dependencies': [
        '<(DEPTH)/syzygy/swapimport/swapimport.gyp:swapimport',
      ],
    },
  ],
}
