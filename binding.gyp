{ 
  "targets": [
    {
      "target_name": "yapu",
      "sources": [
          "src/yapu.cc", 
          "src/LodePNG/lodepng.cpp",
          "src/LodePNG/lodepng_util.cpp"
      ],
      'cflags!': [ "-Wall", "-Wextra", "-pedantic", "-ansi", "-O3" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}