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

from blackfox.models.keras_hidden_layer_config import KerasHiddenLayerConfig  # noqa: F401,E501


class KerasOptimizedNetwork(object):
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
        'dropout': 'float',
        'id': 'str',
        'hidden_layers': 'list[KerasHiddenLayerConfig]',
        'training_algorithm': 'str',
        'output_layer_activation_function': 'str'
    }

    attribute_map = {
        'dropout': 'dropout',
        'id': 'id',
        'hidden_layers': 'hiddenLayers',
        'training_algorithm': 'trainingAlgorithm',
        'output_layer_activation_function': 'outputLayerActivationFunction'
    }

    def __init__(self, dropout=None, id=None, hidden_layers=None, training_algorithm=None, output_layer_activation_function=None):  # noqa: E501
        """KerasOptimizedNetwork - a model defined in Swagger"""  # noqa: E501

        self._dropout = None
        self._id = None
        self._hidden_layers = None
        self._training_algorithm = None
        self._output_layer_activation_function = None
        self.discriminator = None

        if dropout is not None:
            self.dropout = dropout
        if id is not None:
            self.id = id
        if hidden_layers is not None:
            self.hidden_layers = hidden_layers
        if training_algorithm is not None:
            self.training_algorithm = training_algorithm
        if output_layer_activation_function is not None:
            self.output_layer_activation_function = output_layer_activation_function

    @property
    def dropout(self):
        """Gets the dropout of this KerasOptimizedNetwork.  # noqa: E501


        :return: The dropout of this KerasOptimizedNetwork.  # noqa: E501
        :rtype: float
        """
        return self._dropout

    @dropout.setter
    def dropout(self, dropout):
        """Sets the dropout of this KerasOptimizedNetwork.


        :param dropout: The dropout of this KerasOptimizedNetwork.  # noqa: E501
        :type: float
        """

        self._dropout = dropout

    @property
    def id(self):
        """Gets the id of this KerasOptimizedNetwork.  # noqa: E501


        :return: The id of this KerasOptimizedNetwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KerasOptimizedNetwork.


        :param id: The id of this KerasOptimizedNetwork.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def hidden_layers(self):
        """Gets the hidden_layers of this KerasOptimizedNetwork.  # noqa: E501


        :return: The hidden_layers of this KerasOptimizedNetwork.  # noqa: E501
        :rtype: list[KerasHiddenLayerConfig]
        """
        return self._hidden_layers

    @hidden_layers.setter
    def hidden_layers(self, hidden_layers):
        """Sets the hidden_layers of this KerasOptimizedNetwork.


        :param hidden_layers: The hidden_layers of this KerasOptimizedNetwork.  # noqa: E501
        :type: list[KerasHiddenLayerConfig]
        """

        self._hidden_layers = hidden_layers

    @property
    def training_algorithm(self):
        """Gets the training_algorithm of this KerasOptimizedNetwork.  # noqa: E501


        :return: The training_algorithm of this KerasOptimizedNetwork.  # noqa: E501
        :rtype: str
        """
        return self._training_algorithm

    @training_algorithm.setter
    def training_algorithm(self, training_algorithm):
        """Sets the training_algorithm of this KerasOptimizedNetwork.


        :param training_algorithm: The training_algorithm of this KerasOptimizedNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["SGD", "RMSprop", "Adagrad", "Adadelta", "Adam", "Adamax", "Nadam"]  # noqa: E501
        if training_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `training_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(training_algorithm, allowed_values)
            )

        self._training_algorithm = training_algorithm

    @property
    def output_layer_activation_function(self):
        """Gets the output_layer_activation_function of this KerasOptimizedNetwork.  # noqa: E501


        :return: The output_layer_activation_function of this KerasOptimizedNetwork.  # noqa: E501
        :rtype: str
        """
        return self._output_layer_activation_function

    @output_layer_activation_function.setter
    def output_layer_activation_function(self, output_layer_activation_function):
        """Sets the output_layer_activation_function of this KerasOptimizedNetwork.


        :param output_layer_activation_function: The output_layer_activation_function of this KerasOptimizedNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["SoftMax", "Elu", "Selu", "SoftPlus", "SoftSign", "ReLu", "TanH", "Sigmoid", "HardSigmoid", "Linear"]  # noqa: E501
        if output_layer_activation_function not in allowed_values:
            raise ValueError(
                "Invalid value for `output_layer_activation_function` ({0}), must be one of {1}"  # noqa: E501
                .format(output_layer_activation_function, allowed_values)
            )

        self._output_layer_activation_function = output_layer_activation_function

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
        if not isinstance(other, KerasOptimizedNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
