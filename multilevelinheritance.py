class Order:
    def __init__(self, order_id):
        self.orderid = order_id

    def order_placed(self):
        print("Order ID:", self.orderid)
        print("Order placed successfully")


class ShippedOrder(Order):
    def __init__(self, order_id, partner):
        super().__init__(order_id)
        self.partner = partner

    def order_shipped(self):
        print("Order shipped via", self.partner)


class DeliveredOrder(ShippedOrder):
    def __init__(self, order_id, partner, date):
        super().__init__(order_id, partner)
        self.date = date

    def order_delivered(self):
        print("Order delivered on", self.date)


# Object creation
o = DeliveredOrder(123, "BlueDart", "21-Jan-2026")

o.order_placed()
o.order_shipped()
o.order_delivered()
