from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from watson_developer_cloud import LanguageTranslatorV3
from watson_developer_cloud import WatsonApiException

import json

DEFAULT_LANG = 'ja'


class IndexView(TemplateView):
    template_name = 'translate/index.html'

    def get(self, request, *args, **kwargs):
        context = {'source_lang': DEFAULT_LANG}
        return self.render_to_response(context) 

    def post(self, request, *args, **kwargs):
        context = ''
        if request.POST['source']:
            try:
                language_translator = LanguageTranslatorV3(
                    version='2018-05-01',
                    iam_apikey='',
                    url='https://gateway-tok.watsonplatform.net/language-translator/api'
                )

                translation = language_translator.translate(
                text=request.POST['source'],
                source=request.POST['source_lang'],
                target=request.POST['target_lang'],
                ).get_result()

                if translation:
                    context = translation['translations'][0]['translation']

            except WatsonApiException as ex:
                print("Method failed with status code " + str(ex.code) + ": " + ex.message)
                context = ''

        return HttpResponse(context)
        # return self.render_to_response(context)
