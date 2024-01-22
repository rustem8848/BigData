#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
user_number = input("Enter a figure from 0 to 10: ")
user_number = int(user_number)
random_number = random.randint(0, 10)
if user_number == random_number:
    print("You've guessed")
else:
    print("You haven't guessed")