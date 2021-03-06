# coding: utf-8

"""
    BlackFox

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrainedNetwork(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'epoch_count': 'int',
        'errors_on_validation_set': 'list[float]',
        'errors_on_training_set': 'list[float]'
    }

    attribute_map = {
        'id': 'id',
        'epoch_count': 'epochCount',
        'errors_on_validation_set': 'errorsOnValidationSet',
        'errors_on_training_set': 'errorsOnTrainingSet'
    }

    def __init__(self, id=None, epoch_count=None, errors_on_validation_set=None, errors_on_training_set=None):  # noqa: E501
        """TrainedNetwork - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._epoch_count = None
        self._errors_on_validation_set = None
        self._errors_on_training_set = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if epoch_count is not None:
            self.epoch_count = epoch_count
        if errors_on_validation_set is not None:
            self.errors_on_validation_set = errors_on_validation_set
        if errors_on_training_set is not None:
            self.errors_on_training_set = errors_on_training_set

    @property
    def id(self):
        """Gets the id of this TrainedNetwork.  # noqa: E501


        :return: The id of this TrainedNetwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrainedNetwork.


        :param id: The id of this TrainedNetwork.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def epoch_count(self):
        """Gets the epoch_count of this TrainedNetwork.  # noqa: E501


        :return: The epoch_count of this TrainedNetwork.  # noqa: E501
        :rtype: int
        """
        return self._epoch_count

    @epoch_count.setter
    def epoch_count(self, epoch_count):
        """Sets the epoch_count of this TrainedNetwork.


        :param epoch_count: The epoch_count of this TrainedNetwork.  # noqa: E501
        :type: int
        """

        self._epoch_count = epoch_count

    @property
    def errors_on_validation_set(self):
        """Gets the errors_on_validation_set of this TrainedNetwork.  # noqa: E501


        :return: The errors_on_validation_set of this TrainedNetwork.  # noqa: E501
        :rtype: list[float]
        """
        return self._errors_on_validation_set

    @errors_on_validation_set.setter
    def errors_on_validation_set(self, errors_on_validation_set):
        """Sets the errors_on_validation_set of this TrainedNetwork.


        :param errors_on_validation_set: The errors_on_validation_set of this TrainedNetwork.  # noqa: E501
        :type: list[float]
        """

        self._errors_on_validation_set = errors_on_validation_set

    @property
    def errors_on_training_set(self):
        """Gets the errors_on_training_set of this TrainedNetwork.  # noqa: E501


        :return: The errors_on_training_set of this TrainedNetwork.  # noqa: E501
        :rtype: list[float]
        """
        return self._errors_on_training_set

    @errors_on_training_set.setter
    def errors_on_training_set(self, errors_on_training_set):
        """Sets the errors_on_training_set of this TrainedNetwork.


        :param errors_on_training_set: The errors_on_training_set of this TrainedNetwork.  # noqa: E501
        :type: list[float]
        """

        self._errors_on_training_set = errors_on_training_set

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, TrainedNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
