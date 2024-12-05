# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2016 sliptonic <shopinthewoods@gmail.com>               *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import PathScripts.PathUtils as PathUtils
import unittest


class depthTestCases(unittest.TestCase):
    def test00(self):
        """Stepping down to zero"""
        args = {
            "clearance_height": 15,
            "safe_height": 12,
            "start_depth": 10,
            "step_down": 2,
            "z_finish_step": 1,
            "z_entry_step": 0,
            "final_depth": 0,
            "user_depths": None,
        }

        expected = [8, 6, 4, 2, 1, 0]

        d = PathUtils.depth_params(**args)
        r = [i for i in d]
        self.assertListEqual(r, expected)