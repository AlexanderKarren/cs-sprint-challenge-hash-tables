#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ticket_hash = {}
    route = [None] * length
    for i in range(length):
        ticket_hash.update({tickets[i].source: tickets[i].destination})
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination

    for i in range(length - 1):
        route[i + 1] = ticket_hash[route[i]]

    return route
