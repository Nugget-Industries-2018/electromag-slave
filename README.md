# electromag-slve
This guy opens a socket and waits for a trigger to make it interact with the electromagnet on the ROV. The trigger could be a 't' for toggle, 'o' for open, or 'c' for close, all sent over the socket on 8084.

# How to use
This code opens a socket on localhost:8084. Send the character t to toggle the current state, and the socket will reply with the current state of the pin after the toggle. The same reply occurs for 'o', which opens, or 'c', which closes. "Opening" means to set the gpio pin high and engage the electromagnet while "closing" means to shut it down and disengage the electromagnet.
