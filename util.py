import os

def pick_one(wallpaper_dir: str) -> str:
  picked = os.popen(f'ls {wallpaper_dir} | shuf -n 1').read()[:-1]
  print(f'pick_one: {picked}')
  return picked

def set_bg_to(bg_uri: str) -> None:
  if os.system(f'gsettings set org.gnome.desktop.background picture-uri "file://{bg_uri}"'):
    print('set_bg_to: system error')
    exit(-1)