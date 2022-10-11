from django.test import TestCase
from .models import AmtcModel

class BaseTest(TestCase):
    def test_fields(self):
        item = AmtcModel()
        item.fio ="Aliyev Vali"
        item.sn = "4164552256665658"
        item.save()

        record = AmtcModel.objects.get(pk=1)
        self.assertEqual(record, item)
