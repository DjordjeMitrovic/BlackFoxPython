from blackfox.api.data_set_api import DataSetApi
from blackfox.api.network_api import NetworkApi
from blackfox.api.prediction_api import PredictionApi
from blackfox.api.training_api import TrainingApi
from blackfox.api.optimization_api import OptimizationApi

from blackfox.api_client import ApiClient
from blackfox.configuration import Configuration
from blackfox.rest import ApiException

import hashlib
import shutil
import time
from datetime import datetime

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


class BlackFox:

    def __init__(self, host="http://localhost:50476/"):
        self.host = host
        configuration = Configuration()
        configuration.host = host
        self.client = ApiClient(configuration)
        self.data_set_api = DataSetApi(self.client)
        self.network_api = NetworkApi(self.client)
        self.prediction_api = PredictionApi(self.client)
        self.training_api = TrainingApi(self.client)
        self.optimization_api = OptimizationApi(self.client)

    def upload_data_set(self, path):
        id = self.sha1(path)
        try:
            self.data_set_api.head(id)
        except ApiException as e:
            if e.status == 404:
                id = self.data_set_api.post(file=path)
            else:
                raise e
        return id

    def download_data_set(self, id, path):
        temp_path = self.data_set_api.get(id)
        shutil.move(temp_path, path)

    def upload_network(self, path):
        id = self.sha1(path)
        try:
            self.network_api.head(id)
        except ApiException as e:
            if e.status == 404:
                id = self.network_api.post(file=path)
            else:
                raise e
        return id

    def download_network(self, id, path):
        temp_path = self.network_api.get(id)
        shutil.move(temp_path, path)

    def train_keras(
        self,
        config,
        data_set_path=None,
        network_path=None
    ):
        """
        Train network

        :param KerasTrainingConfig config:
        :param str data_set_path:
        :param str nework_path:
        :return: TrainedNetwork
                If data_set_path is not None upload data set 
                and sets config.dataset_id to new id.
                If network_path is not None 
                download network to given file.
        """
        if data_set_path is not None:
            config.dataset_id = self.upload_data_set(data_set_path)

        trained_network = self.training_api.post(value=config)

        if network_path is not None:
            self.download_network(trained_network.id, network_path)

        return trained_network

    def predict_from_file_keras(
        self,
        config,
        network_path=None,
        data_set_path=None,
        result_path=None
    ):
        """
        Predict values and download results in file

        :param PredictionFileConfig config:
        :param str network_path:
        :param str data_set_path:
        :param str result_path:
        :return: str: result data set id
                If network_path is not None upload network,
                and sets config.network_id to new id.
                If data_set_path is not None upload data set,
                and sets config.data_set_id to new id.
                If result_path is not None download results
                to given file.
        """
        if network_path is not None:
            config.network_id = self.upload_network(network_path)
        if data_set_path is not None:
            config.data_set_id = self.upload_data_set(data_set_path)
        result_id = self.prediction_api.post_file(config=config)
        if result_path is not None:
            self.download_data_set(result_id, result_path)
        return result_id

    def predict_from_array_keras(
        self,
        config,
        network_path=None
    ):
        """
        Predict values and return results

        :param PredictionArrayConfig config:
        :param str network_path:
        :return: list[list[float]]: 
                If network_path is not None upload network,
                and sets config.network_id to new id.
        """
        if network_path is not None:
            config.network_id = self.upload_network(network_path)
        results = self.prediction_api.post_array(config=config)
        return results

    def optimize_keras_sync(
        self,
        config,
        data_set_path=None,
        network_path=None,
        status_interval=5,
        log_path=None
    ):
        """
        Find optimal network for given problem.

        :param KerasOptimizationConfig config:
        :param str data_set_path:
        :param str network_path:
        :param int status_interval:
        :param str log_path:
        :return: KerasOptimizationStatus: 
                If data_set_path is not None upload data set,
                and sets config.dataset_id to new id.
                If network_path is not None download network to given file.
                If log_path is not None write to log file 
                every 5 seconds(status_interval)
        """
        if data_set_path is not None:
            config.dataset_id = self.upload_data_set(data_set_path)
        id = self.optimization_api.post_async(config=config)
        running = True
        status = None
        while running:
            status = self.optimization_api.get_status_async(id)
            running = (status.state == 'Active')
            if log_path is not None:
                with open(log_path, "a") as log_file:
                    log_file.write(
                        ("%s -> %s, Generation: %s/%s, Validation set error: %f, Training set error: %f, Epoch: %d, OptId: %s\n") %
                        (
                            datetime.now(),
                            status.state,
                            status.generation,
                            status.total_generations,
                            status.validation_set_error,
                            status.training_set_error,
                            status.epoch,
                            id
                        )
                    )
            time.sleep(status_interval)

        if status.state == 'Finished' or status.state == 'Stopped':
            if network_path is not None:
                self.download_network(status.network.id, network_path)
            return status

        elif status.state == 'Error':
            # Handle error
            raise 'Optimization error'
        else:
            # TODO
            raise 'Error unknown'

    def optimize_keras(
        self,
        config,
        data_set_path=None
    ):
        """
        Find optimal network for given problem async.

        :param KerasOptimizationConfig config:
        :param str data_set_path:
        :return: str: 
                If data_set_path is not None upload data set,
                and sets config.dataset_id to new id.
                Return optimization id.
        """
        if data_set_path is not None:
            config.dataset_id = self.upload_data_set(data_set_path)
        return self.optimization_api.post_async(config=config)

    def get_optimization_status_keras(
        self,
        id,
        network_path=None
    ):
        """
        Get status for optimization.

        :param KerasOptimizationConfig config:
        :param str network_path:
        :return: KerasOptimizationStatus: 
                If data_set_path is not None upload data set,
                and sets config.dataset_id to new id.
        """
        status = self.optimization_api.get_status_async(id)
        if (
            (status.state == 'Finished' or status.state == 'Stopped')
            and (network_path is not None)
        ):
            self.download_network(status.network.id, network_path)

        return status

    def cancel_optimization_keras(self, id):
        """
            Cancel optimization.

            :param str id:
            :return: None: 
                    Call get_optimization_status_keras to get status.
        """
        self.optimization_api.post_action_async(id, 'Cancel')

    def stop_optimization_keras(self, id, network_path=None):
        """
            Stop optimization

            :param str id:
            :param str network_path:
            :return: None: 
                    If network_path is not None download network to given file,
                    else call get_optimization_status_keras to get status
                    and download network.
        """
        self.optimization_api.post_action_async(id, 'Stop')
        if network_path is not None:
            state = 'Active'
            while state == 'Active':
                status = self.get_optimization_status_keras(id, network_path)
                state = status.state

    def sha1(self, path):
        sha1 = hashlib.sha1()
        with open(path, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()