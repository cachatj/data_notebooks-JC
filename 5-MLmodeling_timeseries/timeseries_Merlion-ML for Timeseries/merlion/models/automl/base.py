#
# Copyright (c) 2022 salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#
"""
Base class/mixin for AutoML hyperparameter search.
"""
from abc import abstractmethod
from copy import deepcopy
from typing import Any, Iterator, Optional, Tuple

from merlion.models.layers import ModelBase, LayeredModel
from merlion.utils import TimeSeries
from merlion.utils.misc import AutodocABCMeta


class AutoMLMixIn(LayeredModel, metaclass=AutodocABCMeta):
    """
    Abstract base class which converts `LayeredModel` into an AutoML models.
    """

    def train_model(self, train_data: TimeSeries, **kwargs):
        """
        Generates a set of candidate models and picks the best one.

        :param train_data: the data to train on, after any pre-processing transforms have been applied.
        """
        candidate_thetas = self.generate_theta(train_data)
        theta, model, train_result = self.evaluate_theta(candidate_thetas, train_data, kwargs)
        if model is not None:
            self.model = model
            return train_result
        else:
            model = deepcopy(self.model)
            model.reset()
            self.set_theta(model, theta, train_data)
            self.model = model
            return self.model.train(train_data, **kwargs)

    @abstractmethod
    def generate_theta(self, train_data: TimeSeries) -> Iterator:
        r"""
        :param train_data: Training data to use for generation of hyperparameters :math:`\theta`

        Returns an iterator of hyperparameter candidates for consideration with th underlying model.
        """
        raise NotImplementedError

    @abstractmethod
    def evaluate_theta(
        self, thetas: Iterator, train_data: TimeSeries, train_config=None, **kwargs
    ) -> Tuple[Any, Optional[ModelBase], Optional[Tuple[TimeSeries, Optional[TimeSeries]]]]:
        r"""
        :param thetas: Iterator of the hyperparameter candidates
        :param train_data: Training data
        :param train_config: Training configuration

        Return the optimal hyperparameter, as well as optionally a model and result of the training procedure.
        """
        raise NotImplementedError

    @abstractmethod
    def set_theta(self, model, theta, train_data: TimeSeries = None):
        r"""
        :param model: Underlying base model to which the new theta is applied
        :param theta: Hyperparameter to apply
        :param train_data: Training data (Optional)

        Sets the hyperparameter to the provided ``model``. This is used to apply the :math:`\theta` to the model, since
        this behavior is custom to every model. Oftentimes in internal implementations, ``model`` is the optimal model.
        """
        raise NotImplementedError
