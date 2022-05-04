# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cuenta import Cuenta  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBaristaController(BaseTestCase):
    """BaristaController integration test stubs"""

    def test_crear_cuenta(self):
        """Test case for crear_cuenta

        Crea una cuenta
        """
        body = Cuenta()
        response = self.client.open(
            '/v1/cuenta/{idCuenta}/'.format(id_cuenta='id_cuenta_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_cuenta(self):
        """Test case for obtener_cuenta

        Obtiene la cuenta
        """
        response = self.client.open(
            '/v1/cuenta/{idCuenta}/'.format(id_cuenta='id_cuenta_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_pedido(self):
        """Test case for obtener_pedido

        Obtiene los pedidos
        """
        query_string = [('id_pedido', 'id_pedido_example')]
        response = self.client.open(
            '/v1/pedido',
            method='GET',
            query_string=query_string)
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

    def test_reemplazar_producto(self):
        """Test case for reemplazar_producto

        Reemplaza el producto
        """
        body = Producto()
        response = self.client.open(
            '/v1/producto/{idProducto}/'.format(id_producto='id_producto_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
