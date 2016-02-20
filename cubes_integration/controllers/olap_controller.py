# -*- coding: utf-8 -*-

import openerp.addons.web.http as http


class OlapController(http.Controller):
    _cp_path = '/olap_analytics'

    @http.httprequest
    def index(self, req, s_action=None, **kw):
        html_tempale = open('gui.html')
        render_html = html_tempale.read()
        return render_html
