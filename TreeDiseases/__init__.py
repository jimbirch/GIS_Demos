# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EABDemo
                                 A QGIS plugin
 Simple simulation of the spread of tree diseases for a presentation on
 statistical modeling. Not a real model for actual decision making.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-17
        copyright            : (C) 2022 by Jim Burchfield
        email                : jim@jdbirch.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load EABDemo class from file EABDemo.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .EAB import EABDemo
    return EABDemo(iface)
