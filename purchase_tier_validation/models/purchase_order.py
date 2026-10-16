# Copyright 2017 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from typing import ClassVar

from odoo import models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit: ClassVar[list[str]] = ["purchase.order", "tier.validation"]
    _state_from: ClassVar[list[str]] = ["draft", "sent", "to approve"]
    _state_to: ClassVar[list[str]] = ["purchase", "approved"]

    _tier_validation_manual_config = False
