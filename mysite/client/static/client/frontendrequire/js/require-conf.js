require.config(
{
  "bundles": {
    "ui.example/_components-manifest-bundle": [
      "ui.example/components/_components-manifest",
      "ui.example/_components-manifest"
    ]
  },
  "paths": {
  },
  "shim": {
    "jquery": {
      "exports": "$"
    },
    "jquery-ui": {
      "exports": "$",
      "deps": [
        "jquery"
      ]
    }
  },
  "waitSeconds": 60
}
)
