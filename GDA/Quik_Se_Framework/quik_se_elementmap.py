

#############################################
# Selenium Dictionary
# All Selenium UI element references are stored here
# Use the logical name to fetch the element reference with the selenium driver method
# return None or a tuple with the (selenium driver method, element name)
#############################################
class SeDict():
    item_find_element_method=0
    item_quik_element=1
    # logical name [screen-name_action_context]
    # prefix logical names with the screen name
    # action options=[txt|btn|img|lbl]
    # txt=textbox can send mouse and keyboard event into element and can read text from element
    # btn=button can send mouse events to element
    # img=icon/image can send mouse events
    # lbl=static text label can fetch text value from element
    # We might discover other element categories
    # Context is best to refer to the visible label in UI or common terminology agreed by SQA team
    dictelements={
        "HLSPlayer_btn_play": ("find_element_by_class_name","button-play-pause"),
        "HLSPlayer_btn_pause": ("find_element_by_class_name","button-play-pause"),
        "HLSPlayer_lbl_Duration": ("find_element_by_class_name", "GoProUIHlsDuration"),
        "HLSPlayer_lbl_Timecode": ("find_element_by_class_name", "GoProUIHlsTimecode"),
        "HLSPlayer_btn_back": ("find_element_by_class_name", "GoProUIHeaderBackButton"),
        "HLSPlayer_btn_prev": ("find_element_by_class_name", "GoProUIHlsPrevButton"),
        "HLSPlayer_btn_next": ("find_element_by_class_name", "GoProUIHlsNextButton"),
        "HLSPlayer_btn_VideoScrub": ("find_element_by_class_name", "GoProUIHlsPlayhead"),
        "HLSPlayer_btn_SoundScrub": ("find_element_by_class_name", "player-volume player-volume--range"),
        "HLSPlayer_img_loadingicon": ("find_element_by_class_name", "loading-state")

        # append all selenium web elements for quik app here
    }

    @staticmethod
    def getElementByLogicalName(logicalname):
        if logicalname in SeDict.dictelements:
            return SeDict.dictelements[logicalname]
        return None


# def test(logicalname):
#     element_item = SeDict.getElementByLogicalName(logicalname)
#     if not element_item:
#         print "%s not in selenium element dictionary" % logicalname
#         return None
#     print "%s => selenium_driver.%s('%s')" % (logicalname,
#                                               element_item[SeDict.item_find_element_method],
#                                               element_item[SeDict.item_quik_element])
#     return element_item
#
# test("HLSPlayer_btn_play")
# test("HLSPlayer_btn_back")
# test("HLSPlayer_lbl_Timecode")
# test("HLSPlayer_btn_SoundScrub")
#
