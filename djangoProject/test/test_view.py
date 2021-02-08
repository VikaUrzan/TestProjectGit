from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from djangoProject.forms import UserForm


class TestStatus(APITestCase):
    def test_status_code(self):
        url = reverse('index')
        print(url)
        response = self.client.get(url)
        print(response)

    def test_status_code_result(self):
        urlResult = reverse('result')
        print(urlResult)
        responseResult = self.client.get(urlResult)
        print(responseResult)


class TestForm(TestCase):
    def test_invalid_form(self):
        userform = UserForm()
        data = {"form": userform}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

