# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cuenta import Cuenta  # noqa: E501
from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClienteController(BaseTestCase):
    """ClienteController integration test stubs"""

    def test_obtener_cuenta(self):
        """Test case for obtener_cuenta

        Obtiene la cuenta
        """
        response = self.client.open(
            '/v1/cuenta/{idCuenta}/'.format(id_cuenta='id_cuenta_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_producto(self):
        """Test case for obtener_producto

        Obtiene los productos
        """
        response = self.client.open(
            '/v1/producto/{idProducto}/'.format(id_producto='id_producto_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
