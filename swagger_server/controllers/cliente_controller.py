import connexion
import six

from swagger_server.models.cuenta import Cuenta  # noqa: E501
from swagger_server.models.producto import Producto  # noqa: E501
from swagger_server import util


def obtener_cuenta(id_cuenta):  # noqa: E501
    """Obtiene la cuenta

    Obtiene la cuenta # noqa: E501

    :param id_cuenta: Pasa el id de la cuenta
    :type id_cuenta: str

    :rtype: List[Cuenta]
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
