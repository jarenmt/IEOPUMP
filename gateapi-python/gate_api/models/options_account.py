# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class OptionsAccount(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'user': 'int',
        'total': 'str',
        'short_enabled': 'bool',
        'unrealised_pnl': 'str',
        'init_margin': 'str',
        'maint_margin': 'str',
        'order_margin': 'str',
        'available': 'str',
        'point': 'str',
        'currency': 'str',
    }

    attribute_map = {
        'user': 'user',
        'total': 'total',
        'short_enabled': 'short_enabled',
        'unrealised_pnl': 'unrealised_pnl',
        'init_margin': 'init_margin',
        'maint_margin': 'maint_margin',
        'order_margin': 'order_margin',
        'available': 'available',
        'point': 'point',
        'currency': 'currency',
    }

    def __init__(
        self,
        user=None,
        total=None,
        short_enabled=None,
        unrealised_pnl=None,
        init_margin=None,
        maint_margin=None,
        order_margin=None,
        available=None,
        point=None,
        currency=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, str, bool, str, str, str, str, str, str, str, Configuration) -> None
        """OptionsAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._total = None
        self._short_enabled = None
        self._unrealised_pnl = None
        self._init_margin = None
        self._maint_margin = None
        self._order_margin = None
        self._available = None
        self._point = None
        self._currency = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if total is not None:
            self.total = total
        if short_enabled is not None:
            self.short_enabled = short_enabled
        if unrealised_pnl is not None:
            self.unrealised_pnl = unrealised_pnl
        if init_margin is not None:
            self.init_margin = init_margin
        if maint_margin is not None:
            self.maint_margin = maint_margin
        if order_margin is not None:
            self.order_margin = order_margin
        if available is not None:
            self.available = available
        if point is not None:
            self.point = point
        if currency is not None:
            self.currency = currency

    @property
    def user(self):
        """Gets the user of this OptionsAccount.  # noqa: E501

        User ID  # noqa: E501

        :return: The user of this OptionsAccount.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this OptionsAccount.

        User ID  # noqa: E501

        :param user: The user of this OptionsAccount.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def total(self):
        """Gets the total of this OptionsAccount.  # noqa: E501

        Total account balance  # noqa: E501

        :return: The total of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OptionsAccount.

        Total account balance  # noqa: E501

        :param total: The total of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def short_enabled(self):
        """Gets the short_enabled of this OptionsAccount.  # noqa: E501

        If the account is allowed to short  # noqa: E501

        :return: The short_enabled of this OptionsAccount.  # noqa: E501
        :rtype: bool
        """
        return self._short_enabled

    @short_enabled.setter
    def short_enabled(self, short_enabled):
        """Sets the short_enabled of this OptionsAccount.

        If the account is allowed to short  # noqa: E501

        :param short_enabled: The short_enabled of this OptionsAccount.  # noqa: E501
        :type: bool
        """

        self._short_enabled = short_enabled

    @property
    def unrealised_pnl(self):
        """Gets the unrealised_pnl of this OptionsAccount.  # noqa: E501

        Unrealized PNL  # noqa: E501

        :return: The unrealised_pnl of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._unrealised_pnl

    @unrealised_pnl.setter
    def unrealised_pnl(self, unrealised_pnl):
        """Sets the unrealised_pnl of this OptionsAccount.

        Unrealized PNL  # noqa: E501

        :param unrealised_pnl: The unrealised_pnl of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._unrealised_pnl = unrealised_pnl

    @property
    def init_margin(self):
        """Gets the init_margin of this OptionsAccount.  # noqa: E501

        Initial position margin  # noqa: E501

        :return: The init_margin of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._init_margin

    @init_margin.setter
    def init_margin(self, init_margin):
        """Sets the init_margin of this OptionsAccount.

        Initial position margin  # noqa: E501

        :param init_margin: The init_margin of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._init_margin = init_margin

    @property
    def maint_margin(self):
        """Gets the maint_margin of this OptionsAccount.  # noqa: E501

        Position maintenance margin  # noqa: E501

        :return: The maint_margin of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._maint_margin

    @maint_margin.setter
    def maint_margin(self, maint_margin):
        """Sets the maint_margin of this OptionsAccount.

        Position maintenance margin  # noqa: E501

        :param maint_margin: The maint_margin of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._maint_margin = maint_margin

    @property
    def order_margin(self):
        """Gets the order_margin of this OptionsAccount.  # noqa: E501

        Order margin of unfinished orders  # noqa: E501

        :return: The order_margin of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._order_margin

    @order_margin.setter
    def order_margin(self, order_margin):
        """Sets the order_margin of this OptionsAccount.

        Order margin of unfinished orders  # noqa: E501

        :param order_margin: The order_margin of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._order_margin = order_margin

    @property
    def available(self):
        """Gets the available of this OptionsAccount.  # noqa: E501

        Available balance to transfer out or trade  # noqa: E501

        :return: The available of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this OptionsAccount.

        Available balance to transfer out or trade  # noqa: E501

        :param available: The available of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._available = available

    @property
    def point(self):
        """Gets the point of this OptionsAccount.  # noqa: E501

        POINT amount  # noqa: E501

        :return: The point of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this OptionsAccount.

        POINT amount  # noqa: E501

        :param point: The point of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._point = point

    @property
    def currency(self):
        """Gets the currency of this OptionsAccount.  # noqa: E501

        Settle currency  # noqa: E501

        :return: The currency of this OptionsAccount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this OptionsAccount.

        Settle currency  # noqa: E501

        :param currency: The currency of this OptionsAccount.  # noqa: E501
        :type: str
        """

        self._currency = currency

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OptionsAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsAccount):
            return True

        return self.to_dict() != other.to_dict()