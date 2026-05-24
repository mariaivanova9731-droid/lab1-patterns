class MessageBus:

    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_type, handler):

        if event_type not in self.handlers:
            self.handlers[event_type] = []

        self.handlers[event_type].append(handler)

    def publish(self, event):

        event_type = type(event)

        if event_type in self.handlers:

            for handler in self.handlers[event_type]:
                handler(event)


class OrderCreated:

    def __init__(self, order_id):
        self.order_id = order_id


def send_email(event):
    print(f"Email sent for order #{event.order_id}")


def update_warehouse(event):
    print(f"Warehouse updated for order #{event.order_id}")


def create_log(event):
    print(f"Log created for order #{event.order_id}")


if __name__ == "__main__":

    bus = MessageBus()

    bus.subscribe(OrderCreated, send_email)
    bus.subscribe(OrderCreated, update_warehouse)
    bus.subscribe(OrderCreated, create_log)

    event = OrderCreated(101)

    bus.publish(event)
