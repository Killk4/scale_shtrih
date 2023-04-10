from ctypes import *

scale = CDLL(r"./Scale1C.dll")

Device = scale.AddDevice