# coding: utf-8
import uuid

import bottle
from pioupiou import FolderAvatarTheme


app = bottle.Bottle()


@app.route('/')
def index():

    return bottle.template("""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>pioupiou: python lib for avatar generation</title>
</head>

<body>
  <h1>pioupiou: python lib for avatar generation</h1>
  <p>
    <a href="https://framagit.org/inkhey/pioupiou">pioupiou</a> is a python lib which generate
    random avatar based on different image layers.
  </p>
  <p>
    <img src="/avatar.png" title="Avatar" />
  </p>
  <p>Refresh the page to generate a new one !</p>
</body>

</html>""")


@app.route('/avatar.png')
def avatar():
    theme = FolderAvatarTheme(
        folder_path="cat_revoy",
        layers_name=["body", "fur", "eyes", "mouth", "accessorie"],
    )
    avatar = theme.generate_avatar(token=uuid.uuid4().hex)
    theme.save_on_disk(avatar, path="/tmp/pioupiou.png")
    return bottle.static_file(
        "pioupiou.png", root='/tmp', download=False
    )
