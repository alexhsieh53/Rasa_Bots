from __future__ import absolute_import
from  __future__ import division
from  __future__ import unicode_literals

import datetime
from rasa_core_sdk import Action
from rasa_core_sdk.events import *
logger = logging.getLogger(__name__)

support_search = ["消費", "流量"]
d = {1: '星期一', 2: '星期二',3: '星期三',4: '星期四',5: '星期五',6: '星期六',7: '星期日'}


def extract_item(item):
    """
    check if item supported, this func just for lack of train data.
    :param item: item in track, eg: "流量"、"查流量"
    :return:
    """
    if item is None:
        return None
    for name in support_search:
        if name in item:
            return name
    return None


class ActionSearchConsume(Action):
    def name(self):
        return 'action_search_consume'

    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("您好，我現在只會查話費和流量")
            dispatcher.utter_message("你可以這樣問我：“幫我查話費”")
            return []

        time = tracker.get_slot("time")
        if time is None:
            dispatcher.utter_message("您想查询哪个月的消费？")
            return []
        # query database here using item and time as key. but you may normalize time format first.
        dispatcher.utter_message("好，請稍等")
        if item == "流量":
            dispatcher.utter_message("您好，您{}共使用{}二百八十兆，剩餘三十兆。".format(time, item))
        else:
            dispatcher.utter_message("您好，您{}共消費二十八元。".format(time))
        return []
class Days(Action):
    def name(self):
        return 'action_weekday'
    def run(self, dispatcher, tracker, domain):
        item1 = tracker.get_slot("times")
        
        if item1 is None:
            dispatcher.utter_message(item1)
            return []
        x = datetime.datetime.now()
        p=datetime.date(x.year,x.month,x.day).isoweekday()
        if item1 == "今天":
            dispatcher.utter_message("您好{}是{}。".format(item1, d[p]))
        elif item1== "明天":
            dispatcher.utter_message("您好{}是{}。".format(item1, d[p+1]))
        elif item1== "昨天":
            dispatcher.utter_message("您好{}是{}。".format(item1, d[p-1]))
        return []




