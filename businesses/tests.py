from django.test import TestCase
from django.urls import reverse
from .models import Business

class BusinessViewTestCase(TestCase):
    def setUp(self):
        self.business_1 = Business.objects.create(name="Coded1", description="This is Coded1", established="2017-10-10")
        self.business_2 = Business.objects.create(name="Coded2", description="This is Coded2", established="2017-11-11")
        self.business_3 = Business.objects.create(name="Coded3", description="This is Coded3", established="2017-12-12")

    def test_list_view(self):
        list_url = reverse("business_list")
        response = self.client.get(list_url)
        for business in Business.objects.all():
            self.assertIn(business, response.context['objects'])
            self.assertContains(response, business.name)
            self.assertContains(response, business.description)
        self.assertTemplateUsed(response, 'business_list.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        detail_url = reverse("business_detail", kwargs={"business_id":self.business_1.id})
        response = self.client.get(detail_url)
        self.assertEqual(self.business_1, response.context['business'])
        self.assertContains(response, self.business_1.name)
        self.assertContains(response, self.business_1.description)
        self.assertTemplateUsed(response, 'business_detail.html')
        self.assertEqual(response.status_code, 200)