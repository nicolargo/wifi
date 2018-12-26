from unittest import TestCase

from wifi.scan import Cell
import sys

PY3 = sys.version_info[0] == 3


class CorrectInitTest(TestCase):
    fields = {"ssid": None,
              "bitrates": [],
              "address": None,
              "channel": None,
              "encrypted": False,
              "encryption_type": None,
              "frequency": None,
              "mode": None,
              "quality": None,
              "signal": None}

    def test_empty_init(self):
        tcell = Cell()

        if PY3:
            for field, value in self.fields.items():
                self.assertEqual(value, getattr(tcell, field))
        else:
            for field, value in self.fields.iteritems():
                self.assertEqual(value, getattr(tcell, field))
