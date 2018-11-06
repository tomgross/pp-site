__author__ = 'itconsense@gmail.com'

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


class EvaluateTestView(BrowserView):

    def get_radar_chart(self, df):
        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        values = [i[0] for i in list(df.values())[1:]]
        values += values[:1]

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
        plt.yticks([10, 20, 30], ["10", "20", "30"], color="grey", size=7)
        plt.ylim(0, 40)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'b', alpha=0.1)
        fig.savefig('test.png')

        img = six.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        return base64.b64encode(img.read())

    def chart_img(self):
        df = {
            'group': ['A', 'B', 'C', 'D'],
            'var1': [38, 1.5, 30, 4],
            'var2': [29, 10, 9, 34],
            'var3': [8, 39, 23, 24],
            'var4': [7, 31, 33, 14],
            'var5': [28, 15, 32, 14]
        }
        return 'data:image/jpeg;base64, ' + self.get_radar_chart(df)
