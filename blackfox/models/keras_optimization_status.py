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

from blackfox.models.keras_optimized_network import KerasOptimizedNetwork  # noqa: F401,E501


class KerasOptimizationStatus(object):
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
        'state': 'str',
        'generation': 'int',
        'total_generations': 'int',
        'validation_set_error': 'float',
        'training_set_error': 'float',
        'epoch': 'int',
        'network': 'KerasOptimizedNetwork'
    }

    attribute_map = {
        'state': 'state',
        'generation': 'generation',
        'total_generations': 'totalGenerations',
        'validation_set_error': 'validationSetError',
        'training_set_error': 'trainingSetError',
        'epoch': 'epoch',
        'network': 'network'
    }

    def __init__(self, state=None, generation=None, total_generations=None, validation_set_error=None, training_set_error=None, epoch=None, network=None):  # noqa: E501
        """KerasOptimizationStatus - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._generation = None
        self._total_generations = None
        self._validation_set_error = None
        self._training_set_error = None
        self._epoch = None
        self._network = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if generation is not None:
            self.generation = generation
        if total_generations is not None:
            self.total_generations = total_generations
        if validation_set_error is not None:
            self.validation_set_error = validation_set_error
        if training_set_error is not None:
            self.training_set_error = training_set_error
        if epoch is not None:
            self.epoch = epoch
        if network is not None:
            self.network = network

    @property
    def state(self):
        """Gets the state of this KerasOptimizationStatus.  # noqa: E501


        :return: The state of this KerasOptimizationStatus.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this KerasOptimizationStatus.


        :param state: The state of this KerasOptimizationStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Finished", "Stopped", "Error"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def generation(self):
        """Gets the generation of this KerasOptimizationStatus.  # noqa: E501


        :return: The generation of this KerasOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this KerasOptimizationStatus.


        :param generation: The generation of this KerasOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._generation = generation

    @property
    def total_generations(self):
        """Gets the total_generations of this KerasOptimizationStatus.  # noqa: E501


        :return: The total_generations of this KerasOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_generations

    @total_generations.setter
    def total_generations(self, total_generations):
        """Sets the total_generations of this KerasOptimizationStatus.


        :param total_generations: The total_generations of this KerasOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._total_generations = total_generations

    @property
    def validation_set_error(self):
        """Gets the validation_set_error of this KerasOptimizationStatus.  # noqa: E501


        :return: The validation_set_error of this KerasOptimizationStatus.  # noqa: E501
        :rtype: float
        """
        return self._validation_set_error

    @validation_set_error.setter
    def validation_set_error(self, validation_set_error):
        """Sets the validation_set_error of this KerasOptimizationStatus.


        :param validation_set_error: The validation_set_error of this KerasOptimizationStatus.  # noqa: E501
        :type: float
        """

        self._validation_set_error = validation_set_error

    @property
    def training_set_error(self):
        """Gets the training_set_error of this KerasOptimizationStatus.  # noqa: E501


        :return: The training_set_error of this KerasOptimizationStatus.  # noqa: E501
        :rtype: float
        """
        return self._training_set_error

    @training_set_error.setter
    def training_set_error(self, training_set_error):
        """Sets the training_set_error of this KerasOptimizationStatus.


        :param training_set_error: The training_set_error of this KerasOptimizationStatus.  # noqa: E501
        :type: float
        """

        self._training_set_error = training_set_error

    @property
    def epoch(self):
        """Gets the epoch of this KerasOptimizationStatus.  # noqa: E501


        :return: The epoch of this KerasOptimizationStatus.  # noqa: E501
        :rtype: int
        """
        return self._epoch

    @epoch.setter
    def epoch(self, epoch):
        """Sets the epoch of this KerasOptimizationStatus.


        :param epoch: The epoch of this KerasOptimizationStatus.  # noqa: E501
        :type: int
        """

        self._epoch = epoch

    @property
    def network(self):
        """Gets the network of this KerasOptimizationStatus.  # noqa: E501


        :return: The network of this KerasOptimizationStatus.  # noqa: E501
        :rtype: KerasOptimizedNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this KerasOptimizationStatus.


        :param network: The network of this KerasOptimizationStatus.  # noqa: E501
        :type: KerasOptimizedNetwork
        """

        self._network = network

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
        if not isinstance(other, KerasOptimizationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
