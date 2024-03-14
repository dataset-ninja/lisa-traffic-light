Dataset **LISA Traffic Light** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/V/O/hv/5riDaFt3Z30WmdwEAgVOj3AQXnjKHXH1CmOgLMXW2Oqy4h88lGq8LIV883ddZDCIK31C6w03fzNOnxVY7HnV082SbzjaK6Pf0qHfUAVutKN4JPeVVvTCav3CjD9i.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='LISA Traffic Light', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset/download?datasetVersionNumber=2).