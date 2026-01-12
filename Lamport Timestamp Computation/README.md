Lamport timestamps are logical clocks used in distributed systems to establish a partial ordering of events without relying on physical time. Each process maintains a logical clock that increases as events occur. This allows the system to determine causal relationships between events.

Initially, all five processes start with a clock value of zero. Whenever a process performs a send event, it increments its clock and attaches the timestamp to the message. When another process receives the message, it updates its clock to one greater than the maximum of its current clock and the received timestamp. This guarantees that the receive event always occurs logically after the corresponding send event.

In this implementation, ten messages are exchanged among five processes. For each message, two events occur: a send event at the sender and a receive event at the receiver. The program simulates this sequence step-by-step, updating Lamport clocks according to the defined rules. The output shows the logical time at which each message is sent and received.

Lamport timestamps do not measure real time but ensure causal ordering, meaning if one event causally affects another, its timestamp will be smaller. This makes Lamport clocks essential for reasoning about event ordering in distributed systems such as databases, distributed algorithms, and concurrency control.
