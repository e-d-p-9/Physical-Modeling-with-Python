#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
explore the model of the viral load (number of virons in the blood of HIV
                                     infected patient)
after the administration of antiretroviral drug

One model for the viral load predicts that the concentration V(t) of HIV in
the blodo at time t after the start of treatment will be

V(t) = A exp(-a*t) + B exp(-b*t)

The four parameters A, a, B, and b are constants that control the behavior of 
the model

A and B specify the initial viral load
a is the rate at which new cells are infected,
and b is the rate at which virons are removed from the blood


@author: ethanpeacock
"""

