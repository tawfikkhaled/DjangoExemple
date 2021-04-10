removed //\" \"nodemon dist/index.js\"", from package.json at dev script
and "dev": "concurrently -k -n \"Typescript,Node\" -p \"[{name}]\" -c \"blue,green\" \"tsc --watch",
and script  : ,
      "start": "tsc && node dist/index.js"



run : gulp watch (watch ts and less files )
run : npx tsc --watch