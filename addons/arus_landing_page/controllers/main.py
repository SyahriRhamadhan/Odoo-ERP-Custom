from odoo import http
from odoo.http import request


class ArusLandingController(http.Controller):
    @http.route(["/", "/landing"], type="http", auth="public", website=False)
    def landing_page(self, **kwargs):
        return request.render("arus_landing_page.landing_page_template")
