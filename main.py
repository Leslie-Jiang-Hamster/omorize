import util
import config

bg_uri = config.wallpaper_dir + util.pick_one(config.wallpaper_dir)
util.set_bg_to(bg_uri)