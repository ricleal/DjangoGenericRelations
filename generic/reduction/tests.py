# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import Reduction, Scan, Job

'''
To run just one test:
./manage.py test generic.reduction.tests.GenericTestCase.test_generic
./manage.py test generic.reduction.tests.GenericTestCase.test_from_related
./manage.py test generic.reduction.tests.GenericTestCase.test_specific

'''


class GenericTestCase(TestCase):
    def setUp(self):
        #
        # One reduction has multiple scans
        #
        reduction1 = Reduction.objects.create(name="Reduction 1")
        Scan.objects.create(name="Scan 1 of Reduction 1", reduction=reduction1)
        Scan.objects.create(name="Scan 2 of Reduction 1", reduction=reduction1)

        reduction2 = Reduction.objects.create(name="Reduction 2")
        scan21 = Scan.objects.create(name="Scan 1 of Reduction 2", reduction=reduction2)
        scan22 = Scan.objects.create(name="Scan 2 of Reduction 2", reduction=reduction2)

        j = Job.objects.create(content_object=reduction1)
        print "Job created:", j, j.content_object
        j = Job.objects.create(content_object=scan21)
        print "Job created:", j, j.content_object
        j = Job.objects.create(content_object=scan22)
        print "Job created:", j, j.content_object
        print 80*"*"

    def test_generic(self):
        jobs = Job.objects.all()
        for job in jobs:
            print "Job generic:", job, job.content_object, ":", job.content_type
            self.assertTrue( str(job.content_type) in ['scan','reduction'])

    def test_from_related(self):
        jobs = Job.objects.filter(scans__name__contains='Scan')
        for job in jobs:
            print "Job Scans:", job, job.status,
            for scan in job.scans.all():
                print "Scan:", scan.name
                self.assertTrue('Reduction 2' in scan.name)

    def test_specific(self):

        reduction = Reduction.objects.create(name="Reduction Specific")
        scan = Scan.objects.create(name="Scan Specific of Reduction Specific", reduction=reduction)

        Job.objects.create(content_object=reduction)
        Job.objects.create(content_object=scan)

        # This fail!
        # this_scan = Job.objects.get(content_object = scan)
        # self.assertEqual(this_scan,scan)

        job_for_this_scan = Job.objects.get(scans__name = "Scan Specific of Reduction Specific")
        self.assertEqual(job_for_this_scan.content_object,scan)

        job_for_this_reduction = Job.objects.get(reductions__name = "Reduction Specific")
        self.assertEqual(job_for_this_reduction.content_object,reduction)
