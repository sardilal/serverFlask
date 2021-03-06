# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Producto(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id_producto: str=None, precio: int=None):  # noqa: E501
        """Producto - a model defined in Swagger

        :param id_producto: The id_producto of this Producto.  # noqa: E501
        :type id_producto: str
        :param precio: The precio of this Producto.  # noqa: E501
        :type precio: int
        """
        self.swagger_types = {
            'id_producto': str,
            'precio': int
        }

        self.attribute_map = {
            'id_producto': 'idProducto',
            'precio': 'precio'
        }
        self._id_producto = id_producto
        self._precio = precio

    @classmethod
    def from_dict(cls, dikt) -> 'Producto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Producto of this Producto.  # noqa: E501
        :rtype: Producto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_producto(self) -> str:
        """Gets the id_producto of this Producto.


        :return: The id_producto of this Producto.
        :rtype: str
        """
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto: str):
        """Sets the id_producto of this Producto.


        :param id_producto: The id_producto of this Producto.
        :type id_producto: str
        """
        if id_producto is None:
            raise ValueError("Invalid value for `id_producto`, must not be `None`")  # noqa: E501

        self._id_producto = id_producto

    @property
    def precio(self) -> int:
        """Gets the precio of this Producto.


        :return: The precio of this Producto.
        :rtype: int
        """
        return self._precio

    @precio.setter
    def precio(self, precio: int):
        """Sets the precio of this Producto.


        :param precio: The precio of this Producto.
        :type precio: int
        """
        if precio is None:
            raise ValueError("Invalid value for `precio`, must not be `None`")  # noqa: E501

        self._precio = precio
