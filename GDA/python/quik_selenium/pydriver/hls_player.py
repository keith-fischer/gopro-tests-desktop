
######################################
# HLS Player UI Helper class
#
#
######################################
class hlsplayer():

     element_class_map={
     'play':'button-play-pause',
     'pause':'button-play-pause',
     'videotime':'GoProUIHlsTimecode',
     'videototal':'GoProUIHlsDuration',
     'back_to_media':'GoProUIHeaderBackButton',
     'PreviousMedia':'GoProUIHlsPrevButton',
     'NextMedia':'GoProUIHlsNextButton',
     'VideoScrub':'GoProUIHlsPlayhead',
     'SoundScrub':'player-volume player-volume--range'
     }

     def __init__(self,driver):
          self.driver = driver

     def get_element_class_map(ui_name):
          if ui_name in element_class_map:
               return element_class_map[ui_name]
          return None

     def ClickNextMedia(self):
          rc=False
          ele=self.get_element_class_map('NextMedia')
          if ele:
               ele.click()
               return True
          return False

