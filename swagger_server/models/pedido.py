# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pedido(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id_pedido: str=None, nombre: str=None, usuario: str=None):  # noqa: E501
        """Pedido - a model defined in Swagger

        :param id_pedido: The id_pedido of this Pedido.  # noqa: E501
        :type id_pedido: str
        :param nombre: The nombre of this Pedido.  # noqa: E501
        :type nombre: str
        :param usuario: The usuario of this Pedido.  # noqa: E501
        :type usuario: str
        """
        self.swagger_types = {
            'id_pedido': str,
            'nombre': str,
            'usuario': str
        }

        self.attribute_map = {
            'id_pedido': 'idPedido',
            'nombre': 'nombre',
            'usuario': 'usuario'
        }
        self._id_pedido = id_pedido
        self._nombre = nombre
        self._usuario = usuario

    @classmethod
    def from_dict(cls, dikt) -> 'Pedido':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pedido of this Pedido.  # noqa: E501
        :rtype: Pedido
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_pedido(self) -> str:
        """Gets the id_pedido of this Pedido.


        :return: The id_pedido of this Pedido.
        :rtype: str
        """
        return self._id_pedido

    @id_pedido.setter
    def id_pedido(self, id_pedido: str):
        """Sets the id_pedido of this Pedido.


        :param id_pedido: The id_pedido of this Pedido.
        :type id_pedido: str
        """
        if id_pedido is None:
            raise ValueError("Invalid value for `id_pedido`, must not be `None`")  # noqa: E501

        self._id_pedido = id_pedido

    @property
    def nombre(self) -> str:
        """Gets the nombre of this Pedido.


        :return: The nombre of this Pedido.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this Pedido.


        :param nombre: The nombre of this Pedido.
        :type nombre: str
        """
        if nombre is None:
            raise ValueError("Invalid value for `nombre`, must not be `None`")  # noqa: E501

        self._nombre = nombre

    @property
    def usuario(self) -> str:
        """Gets the usuario of this Pedido.


        :return: The usuario of this Pedido.
        :rtype: str
        """
        return self._usuario

    @usuario.setter
    def usuario(self, usuario: str):
        """Sets the usuario of this Pedido.


        :param usuario: The usuario of this Pedido.
        :type usuario: str
        """
        if usuario is None:
            raise ValueError("Invalid value for `usuario`, must not be `None`")  # noqa: E501

        self._usuario = usuario