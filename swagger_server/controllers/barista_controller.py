import connexion
import six

from swagger_server.models.cuenta import Cuenta  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server import util


def crear_cuenta(id_cuenta, body=None):  # noqa: E501
    """Crea una cuenta

    Crea una cuenta # noqa: E501

    :param id_cuenta: Pasa el id de la cuenta
    :type id_cuenta: str
    :param body: Cuenta para agregar
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Cuenta.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def obtener_cuenta(id_cuenta):  # noqa: E501
    """Obtiene la cuenta

    Obtiene la cuenta # noqa: E501

    :param id_cuenta: Pasa el id de la cuenta
    :type id_cuenta: str

    :rtype: List[Cuenta]
    """
    return 'do some magic!'


def obtener_pedido(id_pedido=None):  # noqa: E501
    """Obtiene los pedidos

    Obtiene los pedidos # noqa: E501

    :param id_pedido: Pasa el id del Pedido
    :type id_pedido: str

    :rtype: List[Pedido]
    """
    return 'do some magic!'


def obtener_producto(id_producto):  # noqa: E501
    """Obtiene los productos

    Obtiene los productos # noqa: E501

    :param id_producto: Pasa el id del Producto
    :type id_producto: str

    :rtype: List[Producto]
    """
    return 'do some magic!'


def reemplazar_producto(id_producto, body=None):  # noqa: E501
    """Reemplaza el producto

    Reemplazar el producto # noqa: E501

    :param id_producto: Pasa el id del Producto
    :type id_producto: str
    :param body: Pedido para agregar
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Producto.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
