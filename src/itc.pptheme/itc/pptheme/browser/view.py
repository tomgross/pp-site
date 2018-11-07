# -*- coding: utf-8 -*-
__author__ = 'itconsense@gmail.com'

from collections import OrderedDict
from math import pi
from Products.Five import BrowserView
from plone import api

import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import six


class UpgradeIt(BrowserView):

    def __call__(self):
        portal_setup = api.portal.get_tool(name='portal_setup')
        portal_setup.runImportStepFromProfile(
            'profile-plonetheme.sunburst:default', 'cssregistry', run_dependencies=False)
        portal_skins = api.portal.get_tool(name='portal_skins')
        custom = portal_skins['custom']
        for oid in ['main_template', 'base_properties', 'ploneCustom.css']:
            if oid in custom:
                api.content.delete(obj=custom[oid])
        return "DONE"


class Result(object):

    details = {}
    good = ''
    title = ''


class EvaluateTestView(BrowserView):

    no_text = 'Kein Textbaustein'
    factors = {
        'Meistens': 3,
        'Manchmal': 1,
        'Selten': 0,
        'Nie': -2
    }
    pie_factors = {
        'Meistens': 3,
        'Manchmal': 2,
        'Selten': 1,
        'Nie': 0
    }

    chart_img = ''

    def get_detail_elements(self):
        zope_script = self.context.restrictedTraverse('text_detail_elements')
        return zope_script()

    def get_summary_elements(self):
        zope_script = self.context.restrictedTraverse('text_summary_elements')
        return zope_script()

    def text_blocks(self):
        result = OrderedDict()
        form = self.request.form
        summary = 0
        df = {}
        elements = self.get_detail_elements()
        for group in elements.keys():
            if group not in form:
                continue
            group_title = self.context[group].Title()
            result[group_title] = Result()
            good_values = []
            for key, val in form[group].items():
                summary += self.factors[val]
                element = elements[group].get(key, self.no_text)
                title = element.get('Titel', group_title)
                if val == 'Meistens':
                    good_values.append(title)
                    continue
                text = element.get(val)
                if not text:
                    continue
                if val in element:
                    result[group_title].details[title] = text
                else:
                    result[group_title].details[title] = element.get('default')
                if group_title not in df:
                    df[group_title] = 0
                df[group_title] += self.pie_factors[val]
            if good_values:
                result[group_title].good = ', '.join(good_values)
        summary_elements = self.get_summary_elements()
        if summary < 20:
            result['summary'] = summary_elements['bad']
        elif 20 >= summary < 70:
            result['summary'] = summary_elements['med']
        else:
            result['summary'] = summary_elements['good']
        self.chart_img = 'data:image/jpeg;base64, ' + self.get_radar_chart(df)
        return result

    def get_radar_chart(self, df):
        # number of variable
        categories = list(df)
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        # import pdb; pdb.set_trace()
        values = df.values()
        values.append(values[0])

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        fig = plt.figure()
        ax = plt.subplot(111, polar=True)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([10], ["10"], color="grey", size=7)
        plt.ylim(0, 20)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)
        fig.savefig('test.png')

        img = six.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        return base64.b64encode(img.read())
