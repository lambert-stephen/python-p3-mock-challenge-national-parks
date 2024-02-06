#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    rocky_mountain = NationalPark("Rocky Mountain Park")
    visitor1 = Visitor("Stephen")
    visitor2 = Visitor("Frank")
    trip1 = Trip(visitor1, rocky_mountain, "10/31/23", "10/31/23")
    trip2 = Trip(visitor2, rocky_mountain, "11/31/23", "11/31/23")
    print(rocky_mountain.trips())
    print(rocky_mountain.visitors())
    print(rocky_mountain.total_visits())
    visitor1.name = "Dylan"
    print(visitor1.name)
    ipdb.set_trace()
