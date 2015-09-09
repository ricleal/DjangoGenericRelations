# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import Reduction, Scan, Job

class GenericTestCase(TestCase):
    def setUp(self):
        reduction1 = Reduction.objects.create(name="Reduction 1")
        Scan.objects.create(name="Scan 1 of Reduction 1", reduction=reduction1)
        Scan.objects.create(name="Scan 2 of Reduction 1", reduction=reduction1)

        reduction2 = Reduction.objects.create(name="Reduction 2")
        scan21 = Scan.objects.create(name="Scan 1 of Reduction 2", reduction=reduction2)
        scan22 = Scan.objects.create(name="Scan 2 of Reduction 2", reduction=reduction2)

        Job.objects.create(content_object=reduction1)
        Job.objects.create(content_object=scan21)
        Job.objects.create(content_object=scan22)

    def test_generic(self):
        jobs = Job.objects.all()
        for job in jobs:
            print job, job.content_object, ":",job.content_type
            self.assertTrue( str(job.content_type) in ['scan','reduction'])

    def test_from_related(self):
        jobs = Job.objects.filter(job__name__contains='Scan')
        for job in jobs:
            for j in job.job.all():
                print j.name
                self.assertTrue('Reduction 2' in j.name)
