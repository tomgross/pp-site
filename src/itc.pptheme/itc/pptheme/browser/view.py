# -*- coding: utf-8 -*-
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

elements = {

'sprache': {

# Verständlichkeit
  '1': {
    'Meistens': '',
    'Manchmal': 'Versuchen Sie die Wortwahl immer möglichst genau Ihrem Zielpublikum anzupassen. Es macht einen Unterschied, ob Sie mit Experten oder Laien sprechen.',
    'Selten':  'Versuchen Sie die Wortwahl möglichst genau Ihrem Zielpublikum anzupassen. Es macht einen Unterschied, ob Sie mit Experten oder Laien sprechen.',
    'Nie': 'Versuchen Sie die Wortwahl möglichst genau Ihrem Zielpublikum anzupassen. Es macht einen Unterschied, ob Sie mit Experten oder Laien sprechen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Verständlichkeit',
   },

# Fachbegriffe
  '2': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Benutzen Sie in Fachkreisen öfter Fachbegriffe.',
    'Nie': 'Benutzen Sie in Fachkreisen öfter Fachbegriffe.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Fachbegriffe',
   },

# Fremdwörter
  '3': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Verwenden Sie wenig Fremdwörter. Durch Fremdwörter sind Ihre Zuhörer meist eine kurze Zeit abgelenkt. Viele Menschen müssen diese Fremdwörter für sich übersetzen. Dadurch können Sie den Anschluss verpassen.',
    'Nie': 'Verwenden Sie wenig Fremdwörter. Durch Fremdwörter sind Ihre Zuhörer meist eine kurze Zeit abgelenkt. Viele Menschen müssen diese Fremdwörter für sich übersetzen. Dadurch können Sie den Anschluss verpassen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Fremdwörter',
   },

# Satzbau
  '4': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Ein komplizierter Satzbau lenkt von den Inhalten und Ihrem Ziel ab. Bilden Sie einfache und kurze Sätze.',
    'Nie': 'Ein komplizierter Satzbau lenkt von den Inhalten und Ihrem Ziel ab. Bilden Sie einfache und kurze Sätze.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Satzbau',
   },

# Bespiele/Geschichten
  '5': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Beispiele und Geschichten prägen sich bei Ihrem Gegenüber besonders gut ein. Denn Beispiele und Geschichten rufen sofort innere Bilder hervor und können Emotionen auslösen. Lassen Sie daher eine Vielzahl von Beispielen und Geschichten einfliessen.',
    'Nie': 'Beispiele und Geschichten prägen sich bei Ihrem Gegenüber besonders gut ein. Denn Beispiele und Geschichten rufen sofort innere Bilder hervor und können Emotionen auslösen. Lassen Sie daher eine Vielzahl von Beispielen und Geschichten einfliessen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Bespiele/Geschichten',
   },

},

'kontakt': {

# Zielpublikum
  '1': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Versuchen Sie, soviel wie möglich über Ihr Publikum herauszufinden. Dann können Sie nämlich meist Ihren Auftritt genau auf Ihr Gegenüber abstimmen.',
    'Nie': 'Versuchen Sie, soviel wie möglich über Ihr Publikum herauszufinden. Dann können Sie nämlich Ihren Auftritt genau auf Ihr Gegenüber abstimmen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Zielpublikum',
   },

# Inhalte
  '2': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Versuchen Sie sich in Ihren Gesprächspartner / Ihr Publikum hineinzuversetzen und definieren Sie dann deren Wissensstand und deren Erwartungen genau. Stimmen Sie Ihren Auftritt inhaltlich bestmöglich auf Ihr Gegenüber ab.',
    'Nie': 'Versuchen Sie sich in Ihren Gesprächspartner / Ihr Publikum hineinzuversetzen und definieren Sie dann deren Wissensstand und deren Erwartungen genau. Stimmen Sie Ihren Auftritt inhaltlich bestmöglich auf Ihr Gegenüber ab.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Inhalte',
   },

# Emotionaler Zugang
  '3': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Wenn Sie Ihr Gegenüber emotional erreichen, haben Sie meist gewonnen. Bauen Sie deshalb eine emotionale Basis auf. Zeigen Sie Empathie und gehen Sie auf die emotionalen Bedürfnisse und Wünsche Ihres Gegenübers ein.',
    'Nie': 'Wenn Sie Ihr Gegenüber emotional erreichen, haben Sie meist gewonnen. Bauen Sie deshalb eine emotionale Basis auf. Zeigen Sie Empathie und gehen Sie auf die emotionalen Bedürfnisse und Wünsche Ihres Gegenübers ein.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Emotionaler Zugang',
   },

# Blickkontakt
  '4': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Gucken Sie Ihr Gegenüber an. Nur derjenige, den Sie anschauen, fühlt sich auch angesprochen. In grösseren Gruppen, wird es Ihnen nicht gelingen, alle Personen anzusehen. Versuchen Sie aber auch da zumindest alle Bereiche des Publikums immer wieder eines Blickes zu würdigen.',
    'Nie': 'Gucken Sie Ihr Gegenüber an. Nur derjenige, den Sie anschauen, fühlt sich auch angesprochen. In grösseren Gruppen, wird es Ihnen nicht gelingen, alle Personen anzusehen. Versuchen Sie aber auch da zumindest alle Bereiche des Publikums immer wieder eines Blickes zu würdigen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Blickkontakt',
   },

# Interaktion
  '5': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Binden Sie Ihren Gesprächspartner oder Ihre Zuhörer interaktiv in das Gespräch oder die Präsentation ein z.B. durch Fragen. Dadurch setzt sich Ihr Gegenüber engagierter mit Ihren Zielen auseinander.',
    'Nie': 'Binden Sie Ihren Gesprächspartner oder Ihre Zuhörer interaktiv in das Gespräch oder die Präsentation ein z.B. durch Fragen. Dadurch setzt sich Ihr Gegenüber engagierter mit Ihren Zielen auseinander.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Interaktion',
   },

# Motivationsfähigkeit/Begeisterung
  '6': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Um Ihr Ziel letztendlich zu erreichen, sollten Sie Ihr Gegenüber für Ihre Sache gewinnen. Ihre Motivation und Begeisterung wird sich auf Ihre(n) Gesprächspartner übertragen. Machen Sie sich Ihre Motivation bewusst.',
    'Nie': 'Um Ihr Ziel letztendlich zu erreichen, sollten Sie Ihr Gegenüber für Ihre Sache gewinnen. Ihre Motivation und Begeisterung wird sich auf Ihre(n) Gesprächspartner übertragen. Machen Sie sich Ihre Motivation bewusst.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Motivationsfähigkeit/Begeisterung',
   },

# Überzeugungskraft
  '7': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Hier gilt Überzeugung überzeugt. Sobald Sie selbst wirklich überzeugt sind, werden Sie auch andere leichter überzeugen.',
    'Nie': 'Hier gilt Überzeugung überzeugt. Sobald Sie selbst wirklich überzeugt sind, werden Sie auch andere leichter überzeugen.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Überzeugungskraft',
   },

},

'stimme': {

# Lautstärke
  '1': {
    'Meistens': '',
    'Manchmal': 'Denken sie immer mal wieder daran, so laut zu sprechen, dass alle Zuhörer Sie problemlos hören können.',
    'Selten':  'Denken sie daran, immer so laut zu sprechen, dass alle Zuhörer Sie problemlos hören können.',
    'Nie': 'Denken sie daran, so laut zu sprechen, dass alle Zuhörer Sie problemlos hören können.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Lautstärke',
   },

# Sprechtempo
  '2': {
    'Meistens': '',
    'Manchmal': 'Sie sprechen meist in einer angemessenen Geschwindigkeit. Sprechen Sie immer nur so schnell, wie Sie selbst denken können.',
    'Selten':  'Ihr Zuhörer kann Ihnen nur folgen, wenn Sie nicht zu schnell sprechen. Sprechen Sie immer nur so schnell, wie Sie selbst denken können.',
    'Nie': 'Ihr Zuhörer kann Ihnen nur folgen, wenn Sie nicht zu schnell sprechen. Sonst schaltet er ab. Sprechen Sie nur so schnell, wie Sie selbst denken können.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Sprechtempo',
   },

# Dynamik in der Stimme
  '3': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Monotonie in der Stimme ist langweilig. Versuchen Sie mehr mit der Geschwindigkeit, Tonhöhe, mit Pausen und der Lautstärke zu variieren.',
    'Nie': 'Monotonie in der Stimme ist langweilig. Versuchen Sie mit der Geschwindigkeit, Tonhöhe, mit Pausen und der Lautstärke zu variieren.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Dynamik in der Stimme',
   },

# Betonung
  '4': {
    'Meistens': '',
    'Manchmal': 'Betonen Sie immer mal wieder wichtige Sachverhalte.',
    'Selten':  'Betonen Sie noch mehr wichtige Sachverhalte.',
    'Nie': 'Betonen Sie wichtige Sachverhalte.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Betonung',
   },

# Artikulation
  '5': {
    'Meistens': '',
    'Manchmal': 'Oft artikulieren Sie verständlich. Erinnern Sie sich, immer deutlich zu sprechen.',
    'Selten':  'Auch wenn Sie noch so wichtige Informationen zu sagen haben: Wenn Sie nuscheln, wird Sie keiner verstehen. Reden Sie bewusst deutlich.',
    'Nie': 'Auch wenn Sie noch so wichtige Informationen zu sagen haben: Wenn Sie nuscheln, wird Sie keiner verstehen. Reden Sie bewusst deutlich.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Artikulation',
   },

# Sprechpausen
  '6': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Ihr Gegenüber kann Ihnen schwer folgen, wenn Sie ohne Punkt und Komma sprechen. Daher machen Sie immer am Ende eines Satzes oder Teilsatzes eine kleine Pause, bevor Sie fortfahren.',
    'Nie': 'Ihr Gegenüber kann Ihnen schwer folgen, wenn Sie ohne Punkt und Komma sprechen. Daher machen Sie am Ende eines Satzes oder Teilsatzes eine kleine Pause, bevor Sie fortfahren.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Sprechpausen',
   },

},

'koerper':  {

# Körperhaltung
  '1': {
    'Meistens': '',
    'Manchmal': 'Sie können manchmal noch daran arbeiten, sich aufrecht hinzustellen. Sie kennen sicher die Aussage: „hinter seinen Worten stehen“.',
    'Selten':  'Eine aufrechte Körperhaltung ist sehr wichtig. Sie kennen sicher die Aussage: „hinter seinen Worten stehen“. Denken Sie so oft wie möglich daran, sich wieder aufrecht hinzustellen. Wichtig ist dabei, dass Sie weder über- noch unterspannt sind. ',
    'Nie': 'Eine aufrechte Körperhaltung ist sehr wichtig. Sie kennen sicher die Aussage: „hinter seinen Worten stehen“. Denken Sie so oft wie möglich daran, sich wieder aufrecht hinzustellen. Wichtig ist dabei, dass Sie weder über- noch unterspannt sind. ',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Körperhaltung',
   },

# Gestik
  '2': {
    'Meistens': '',
    'Manchmal': 'Sie verwenden schon einiges an Gestik, um das Gesagte zu unterstreichen. Das ist überzeugend. Beobachten Sie sich kritisch im Spiegel, ob Sie nur kleine und verhaltene Gesten machen. Nur selbstsicher eingesetzte Gesten sind wirklich überzeugend.',
    'Selten':  'Verwenden Sie mehr Gesten, um das Gesagte noch besser zu unterstreichen. Das lässt Ihren Auftritt überzeugend und lebendig wirken.',
    'Nie': 'Verwenden Sie Gesten, um das Gesagte zu unterstreichen. Das lässt Ihren Auftritt überzeugend und lebendig wirken.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Gestik',
   },

# Mimik
  '3': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Um Ihr Gegenüber zu motivieren, benötigen Sie Ihre Mimik. Durch den Einsatz der Mimik fühlt sich Ihr Gegenüber emotional einbezogen. Setzen Sie noch mehr Ihre Mimik ein.',
    'Nie': 'Um Ihr Gegenüber zu motivieren, benötigen Sie Ihre Mimik. Erst durch den Einsatz der Mimik fühlt sich Ihr Gegenüber emotional einbezogen. Setzen Sie Ihre Mimik ein.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Mimik',
   },

# Körperorientierung
  '4': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Egal ob ein einzelner Gesprächspartner oder ein grosses Publikum. Es fühlt sich nur der angesprochen, dem Sie sich mit Ihrer Körperorientierung zugewendet haben. Wenden Sie Ihren Körper also möglichst Ihrem Gegenüber zu.',
    'Nie': 'Egal ob ein einzelner Gesprächspartner oder ein grosses Publikum. Es fühlt sich nur der angesprochen, dem Sie sich mit Ihrer Körperorientierung zugewendet haben. Wenden Sie Ihren Körper also möglichst Ihrem Gegenüber zu.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Körperorientierung',
   },

# Bewegung
  '5': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Wenn Sie immer an einem Ort stehen, wird Ihr Auftritt starr und leblos. Auch wenn Sie pausenlos durch den Raum „tigern“, wirkt Ihr Auftritt unruhig. Wechseln Sie Bewegung und Ruhepositionen ab.',
    'Nie': 'Wenn Sie immer an einem Ort stehen, wird Ihr Auftritt starr und leblos. Auch wenn Sie pausenlos durch den Raum „tigern“, wirkt Ihr Auftritt unruhig. Wechseln Sie Bewegung und Ruhepositionen ab.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Bewegung',
   },

},

'empfindung': {

# Stimmung
  '1': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Nur wenn Sie sich selber wohl fühlen, wird das auch Ihr Publikum tun. Erst dann werden Sie Ihr Gegenüber motivieren und begeistern können. Überlegen Sie sich, wie Sie sich in eine gute Stimmung versetzen können.',
    'Nie': 'Nur wenn Sie sich selber wohl fühlen, wird das auch Ihr Publikum tun. Erst dann werden Sie Ihr Gegenüber motivieren und begeistern können. Überlegen Sie sich, wie Sie sich in eine gute Stimmung versetzen können.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Stimmung',
   },

# Innere Einstellung
  '2': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Wenn Sie eine positive innere Einstellung zur Auftrittssituation haben, werden Sie überzeugend sein. Dann werden Sie auch Freude und Enthusiasmus fühlen. Arbeiten Sie an einer positiven inneren Einstellung.',
    'Nie': 'Wenn Sie eine positive innere Einstellung zur Auftrittssituation haben, werden Sie überzeugend sein. Dann werden Sie auch Freude und Enthusiasmus fühlen. Arbeiten Sie an einer positiven inneren Einstellung.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Innere Einstellung',
   },

# Authentizität
  '3': {
    'Meistens': '',
    'Manchmal': 'Bleiben Sie während Ihres Auftritts möglichst immer authentisch.',
    'Selten':  'Bleiben Sie während Ihres Auftritts authentisch.',
    'Nie': 'Bleiben Sie während Ihres Auftritts authentisch.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Authentizität',
   },

# Selbstsicherheit
  '4': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Ab und zu ist es normal, dass man sich in Auftrittssituationen nicht selbstsicher fühlt. Ihr Gegenüber wird auch nicht jede Unsicherheit bemerken. Sollte die Unsicherheit jedoch überwiegen, versuchen Sie diese zu überwinden.',
    'Nie': 'Schauen Sie sich mal genauer an, warum Sie in einer Auftrittssituation nicht selbstbewusst agieren. Blockiert Sie das Lampenfieber oder fehlt Ihnen die Übung? Versuchen Sie die Ihre Unsicherheit zu überwinden.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Selbstsicherheit',
   },

# Expertise
  '5': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Nur wenn Ihr Gegenüber Ihre Expertise nicht in Frage stellt, werden Sie überzeugen können. Wenn Sie über ausreichendes Fachwissen verfügen, aber das in Auftrittssituationen nicht für andere bemerkbar wird, haben Sie 2 Möglichkeiten: 1. Bringen Sie mit mehr Selbstbewusstsein Ihre Meinung ein oder 2. Stimmen Sie Ihre Aussagen besser auf den Wissensstand Ihres Gegenübers ab.',
    'Nie': 'Nur wenn Ihr Gegenüber Ihre Expertise nicht in Frage stellt, werden Sie überzeugen können. Wenn Sie über ausreichendes Fachwissen verfügen, aber das in Auftrittssituationen nicht für andere bemerkbar wird, haben Sie 2 Möglichkeiten: 1. Bringen Sie mit mehr Selbstbewusstsein Ihre Meinung ein oder 2. Stimmen Sie Ihre Aussagen besser auf den Wissensstand Ihres Gegenübers ab.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Expertise',
   },

# Ziel
  '6': {
    'Meistens': '',
    'Manchmal': 'Seien Sie sich immer über Ihr Ziel in der Auftrittssituation bewusst. Sie kennen den Ausspruch: „Wer ohne Ziel beginnt, muss sich nicht wundern, wenn er irgendwo rauskommt.',
    'Selten':  'Sie kennen den Ausspruch: „Wer ohne Ziel beginnt, muss sich nicht wundern, wenn er irgendwo rauskommt.“ Definieren Sie vor einer Auftrittssituation immer genau Ihr Ziel.',
    'Nie': 'Sie kennen den Ausspruch: „Wer ohne Ziel beginnt, muss sich nicht wundern, wenn er irgendwo rauskommt.“ Definieren Sie vor einer Auftrittssituation genau Ihr Ziel.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Ziel',
   },

},

'erscheinung': {

# KLeidung
  '1': {
    'Meistens': '',
    'Manchmal': 'Überlegen Sie sich immer genau, welche Kleidung dem Publikum und dem Anlass angemessen ist. Kleiden Sie sich danach, ohne sich zu „verkleiden“.',
    'Selten':  'Überlegen Sie sich genau, welche Kleidung dem Publikum und dem Anlass angemessen ist. Kleiden Sie sich danach, ohne sich zu „verkleiden“.',
    'Nie': 'Überlegen Sie sich genau, welche Kleidung dem Publikum und dem Anlass angemessen ist. Kleiden Sie sich danach, ohne sich zu „verkleiden“.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Kleidung',
   },

# Schuhe
  '2': {
    'Meistens': '',
    'Manchmal': 'Tragen Sie immer Schuhe, die Ihnen einen sicheren Stand geben und ein souveränes Auftreten ermöglichen!',
    'Selten':  'Tragen Sie immer Schuhe, die Ihnen einen sicheren Stand geben und ein souveränes Auftreten ermöglichen!',
    'Nie': 'Tragen Sie Schuhe, die Ihnen ein souveränes Auftreten ermöglichen und einen sicheren Stand geben!',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Schuhe',
   },

# Frisur/Rasur
  '3': {
    'Meistens': '',
    'Manchmal': 'Im Gespräch ist Ihr Gesicht im Fokus. Achten Sie deshalb immer auf gepflegte Kopf- und Barthaare.',
    'Selten':  'Im Gespräch ist Ihr Gesicht im Fokus. Achten Sie deshalb auf gepflegte Kopf- und Barthaare.',
    'Nie': 'Im Gespräch ist Ihr Gesicht im Fokus. Achten Sie deshalb auf gepflegte Kopf- und Barthaare.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Haare',
   },

# Make-up
  '4': {
    'Meistens': '',
    'Manchmal': '',
    'Selten':  'Wenn es benötigt wird, wählen Sie ein passendes Make-up, das nicht übertrieben wirkt.',
    'Nie': 'Wenn es benötigt wird, wählen Sie ein passendes Make-up, das nicht übertrieben wirkt.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Make-up',
   },

# Parfum/Geruch
  '5': {
    'Meistens': '',
    'Manchmal': 'Einige Menschen haben einen ausgeprägten Geruchssinn. Achten Sie deshalb in jedem Fall auf einen angenehmen Körpergeruch und ggf. ein dezentes Parfum.',
    'Selten':  'Einige Menschen haben einen ausgeprägten Geruchssinn. Achten Sie deshalb immer auf einen angenehmen Körpergeruch und ggf. ein dezentes Parfum.',
    'Nie': 'Einige Menschen haben einen ausgeprägten Geruchssinn. Achten Sie auf deshalb einen angenehmen Körpergeruch und ggf. ein dezentes Parfum.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Parfum/Geruch',
   },

# Accessoires
  '6': {
    'Meistens': '',
    'Manchmal': 'Accessoires (z.B. Brille, Schmuck etc.) können viel Aufmerksamkeit auf sich ziehen. Wählen Sie nur Accessoires aus, die nicht von Ihrem Auftritt ablenken.',
    'Selten':  'Accessoires (z.B. Brille, Schmuck etc.) können viel Aufmerksamkeit auf sich ziehen. Wählen Sie nur Accessoires aus, die nicht von Ihrem Auftritt ablenken.',
    'Nie': 'Accessoires (z.B. Brille, Schmuck etc.) können viel Aufmerksamkeit auf sich ziehen. Wählen Sie nur Accessoires aus, die nicht von Ihrem Auftritt ablenken.',
    'default': 'Nicht ausgefüllt',
    'Titel': 'Accessoires',
   },

}

}


TEXT_BAD = \
"""
Sie sollten dringend an Ihrer Auftrittskompetenz arbeiten. Denken Sie daran, wenn Sie unsicher auftreten, geht Ihr Publikum wahrscheinlich davon aus, dass auch Ihre Informationen und Argumente nicht ganz fundiert sind. Wenn Sie aber überzeugend auftreten und spannend präsentieren, werden Sie Ihr Gegenüber überzeugen! Holen Sie sich aber Feedback von einer weiteren Person, wie diese Ihr Auftreten und Ihre Präsentationen einschätzt. Manchmal liegen Eigen- und Fremdwahrnehmung weit auseinander. Ich wünsche Ihnen viel Erfolg und Freude bei den nächsten Auftritten und Präsentationen. Und denken Sie immer daran: Übung macht den Meister!
Bei der Schulung von hervorragendem Auftreten und Präsentieren helfe ich ihnen gern.
Gern können Sie mich kontaktieren, wenn Sie ein professionelles Feedback wünschen. Weitere Angebote von PRESENTATION POWER finden Sie hier.
"""


TEXT_MED = \
"""
Ihre Auftrittskompetenz hat Stärken und Schwächen. Üben Sie kontinuierlich Ihre schwächeren Momente beim Auftreten zu verbessern. Aber konzentrieren Sie sich nicht nur auf Ihre Schwachpunkte. Ich finde es wichtig, dass Sie sich auch Ihre Stärken immer wieder vor Augen halten. Sobald Sie sich Ihre Stärken immer wieder bewusst machen, wird Ihnen Auftreten und Präsentieren mehr Freude bereiten. Und das ist wichtig! Ihr Publikum spürt sehr genau, ob Sie Freude und Engagement haben. Natürlich werden Sie auch mehr Spass beim Auftreten haben, wenn Sie sich sicher fühlen. Und denken Sie immer daran: Übung macht den Meister!
Bei der Schulung von hervorragendem Auftreten und Präsentieren helfe ich ihnen gern.
Gern können Sie mich kontaktieren, wenn Sie ein professionelles Feedback wünschen. Weitere Angebote von PRESENTATION POWER finden Sie hier.
"""

TEXT_GOOD = \
"""
Sie sind auf einem guten Weg. Mein Tipp ist: Werden Sie nicht perfektionistisch. Sobald Sie perfekt sein wollen, verlieren Sie Ihre Lockerheit und die Freude am Auftreten und Präsentieren. Genau diese beiden Dinge sind es, die Ihren Auftritt/Vortrag/Präsentation lebendig und spannend werden lassen. Sie haben jetzt die Auswertung zu Ihrer Eigenwahrnehmung. Um ein objektiveres Bild zu Ihren Auftritts- und Präsentationsfähigkeiten zu erhalten, bitten Sie eine andere Person um eine ehrliche Einschätzung und spielen Sie diesen Test erneut durch. Ich wünsche Ihnen viel Erfolg und Freude bei Ihren nächsten Auftritten und Präsentationen.
Bei der Schulung von hervorragendem Auftreten und Präsentieren helfe ich ihnen gern.
Gern können Sie mich kontaktieren, wenn Sie ein professionelles Feedback wünschen. Weitere Angebote von PRESENTATION POWER finden Sie hier.
"""


from collections import OrderedDict


class Result(object):

    points = 0
    details = {}
    good = ''


class EvaluateTestView(BrowserView):

    no_text = 'Kein Textbaustein'
    factors = {
        'Meistens': 3,
        'Manchmal': 1,
        'Selten': 0,
        'Nie': -2
    }

    def text_blocks(self):
        result = OrderedDict()
        form = self.request.form
        summary = 0
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
                result[group_title].points += self.factors[val]
            if good_values:
                result[group_title].good = ', '.join(good_values)
        print(summary)
        if summary < 20:
            result['summary'] = TEXT_BAD
        elif summary >= 20 and summary < 70:
            result['summary'] = TEXT_MED
        else:
            result['summary'] = TEXT_GOOD
        return result

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
