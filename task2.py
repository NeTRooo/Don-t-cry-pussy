#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {
        '1а': 30, '1б': 25,
        '2б': 30, '6а': 12,
        '7в': 5
    }
    print(school)
    school['2б'] -= 3
    school['11б'] = 17
    del school['7в']
    general_count = sum(school.values())
    print(school)