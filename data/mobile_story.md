
## Generated Story 5914322956106259965
* greet
    - utter_greet
* request_search{"item": "\u7684\u60c5\u51b5"}
    - slot{"item": "\u6d88\u8d39"}
    - slot{"item": "\u7684\u60c5\u51b5"}
    - action_search_consume
* request_search{"item": "\u6d88\u8d39"}
    - slot{"item": "\u6d88\u8d39"}
    - action_search_consume
* inform_time{"time": "\u4e0a\u4e2a\u6708"}
    - slot{"time": "\u4e0a\u4e2a\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story 1131691423643832225
* request_search{"item": "\u6d88\u8d39"}
    - slot{"item": "\u6d88\u8d39"}
    - utter_ask_time
* inform_time{"time": "\u5341\u6708\u4efd"}
    - slot{"time": "\u5341\u6708\u4efd"}
    - action_search_consume
    - utter_ask_morehelp
* thanks
    - utter_thanks
    - export

## Generated Story -6529474466838218787
* greet
    - utter_greet
* request_search{"item": "\u6d88\u8d39"}
    - slot{"item": "\u6d88\u8d39"}
    - utter_ask_time
* inform_time{"time": "\u4e0a\u6708"}
    - slot{"time": "\u4e0a\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "\u8fd8", "item": "\u6d88\u8d39"}
    - slot{"time": "\u8fd8"}
    - slot{"item": "\u6d88\u8d39"}
    - utter_ask_morehelp
    - utter_ask_time
* inform_time{"time": "\u5341\u6708"}
    - slot{"time": "\u5341\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
* request_search{"time": "\u8fd8", "item": "\u6d41\u91cf"}
    - slot{"time": "\u8fd8"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_time{"time": "\u516b\u6708"}
    - slot{"time": "\u516b\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - utter_thanks
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - export

## Generated Story 7046379915386561772
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_time{"time": "\u4e0a\u4e2a\u6708"}
    - slot{"time": "\u4e0a\u4e2a\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"item": "\u6d88\u8d39"}
    - slot{"item": "\u6d88\u8d39"}
    - utter_ask_time
* inform_time{"time": "\u4e0a\u4e2a\u6708"}
    - slot{"time": "\u4e0a\u4e2a\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "\u8fd8", "item": "\u53f7\u7801"}
    - slot{"time": "\u8fd8"}
    - slot{"item": "\u6d88\u8d39"}
    - slot{"item": "\u53f7\u7801"}
    - utter_ask_time
* inform_time{"time": "\u4e0a\u6708"}
    - slot{"time": "\u4e0a\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* confirm
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story 3510639764351215934
* greet
    - utter_greet
* request_search{"item": "\u4e1c\u897f"}
    - slot{"item": "\u4e1c\u897f"}
    - utter_ask_time
* inform_time{"time": "\u4e09\u6708"}
    - slot{"time": "\u4e09\u6708"}
    - action_search_consume
* request_search{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_time
* inform_time{"time": "\u56db\u6708"}
    - slot{"time": "\u56db\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story -243931094327703933
* request_management{"item": "\u5957\u9910"}
    - slot{"item": "\u5957\u9910"}
    - utter_ask_package
* inform_package{"item": "\u5957\u9910\u4e09"}
    - slot{"item": "\u5957\u9910\u4e09"}
    - utter_ack_management
    - utter_ask_morehelp
* request_search{"item": "\u6d88\u8d39"}
    - slot{"item": "\u6d88\u8d39"}
    - utter_ask_time
* inform_time{"time": "\u4e09\u6708"}
    - slot{"time": "\u4e09\u6708"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export


## Generated Story -8627121140811593037
* greet
    - utter_greet
* request_management{"item": "\u6d41\u91cf"}
    - slot{"item": "\u6d41\u91cf"}
    - utter_ask_package
* inform_package{"item": "\u5957\u9910\u4e00"}
    - slot{"item": "\u5957\u9910\u4e00"}
    - utter_ack_management
    - utter_ask_morehelp
* deny
    - utter_goodbye
* deny
    - utter_greet
    - export
## Generated Story 1446771359143028837
* greet
    - utter_greet
* request_day{"times": "\u4eca\u5929", "day": "\u661f\u671f \u5e7e"}
    - action_weekday
## Generated Story 4308524762288764157
* request_day{"times": "\u4eca\u5929", "day": "\u79ae\u62dc \u5e7e"}
    - slot{"times": "\u4eca\u5929"}
    - action_weekday
* request_day{"times": "\u660e\u5929", "day": "\u661f\u671f \u5e7e"}
    - slot{"times": "\u660e\u5929"}
    - action_weekday
* request_day{"day": "\u5e7e\u6708 \u5e7e\u865f"}
    - action_weekday
