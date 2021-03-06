# -*- coding: utf-8 -*-

"""
天気予報からイメージ（絵文字）をルックアップテーブルで対応付ける
"""

WEATHER_TO_IMAGE_LOOKUP_TABLE = {
	u'晴れ': u'晴れ☀',
	u'晴時々曇': u'晴れときどき曇り⛅',
	u'晴時々雨': u'晴れ☀ときどき雨☔',
	u'晴時々雪': u'晴れ☀ときどき雪❄',
	u'晴のち曇': u'晴れ☀のち曇り☁',
	u'晴のち雨': u'晴れ☀のち雨☔',
	u'晴のち雪': u'晴れ☀のち雪❄',
	u'曇り': u'曇り☁',
	u'曇時々晴': u'曇り☁ときどき晴れ☀',
	u'曇時々雨': u'曇り☁ときどき雨☔',
	u'曇時々雪': u'曇り☁ときどき雪❄',
	u'曇のち晴': u'曇り☁のち晴れ☀',
	u'曇のち雨': u'曇り☁のち雨☔',
	u'曇のち雪': u'曇り☁のち雪❄',
	u'雨': u'雨☔',
	u'雨時々晴': u'雨☔ときどき晴れ☀',
	u'雨時々曇': u'雨☔ときどき曇り☁',
	u'雨時々雪': u'雨☔ときどき雪❄',
	u'雨のち晴': u'雨☔のち晴れ☀',
	u'雨のち曇': u'雨☔のち曇り☁',
	u'雨のち雪': u'雨☔のち雪❄',
	u'暴風雨': u'暴風雨☔💨💨',
	u'雪': u'雪❄',
	u'雪時々晴': u'雪❄ときどき晴れ☀',
	u'雪時々曇り': u'雪❄ときどき曇り☁',
	u'雪時々雨': u'雪❄ときどき雨☔',
	u'雪のち晴': u'雪❄のち晴れ☀',
	u'雪のち曇り': u'雪❄のち曇り☁',
	u'雪のち雨': u'雪❄のち雨☔',
	u'暴風雪': u'暴風雪❄💨💨'
}


def get_image(weather):
	return WEATHER_TO_IMAGE_LOOKUP_TABLE[weather]

