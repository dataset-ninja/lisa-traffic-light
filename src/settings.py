from typing import Dict, List, Literal, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "LISA Traffic Light"
PROJECT_NAME_FULL: str = "LISA Traffic Light Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Automotive()]
CATEGORY: Category = Category.SelfDriving()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2016

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 15219081
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/lisa-traffic-light"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = (
    "https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset/download?datasetVersionNumber=2"
)
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]] or Literal["predefined"]] = {
    "go traffic light": [230, 25, 75],
    "stop traffic light": [60, 180, 75],
    "stop left traffic light": [255, 225, 25],
    "warning traffic light": [0, 130, 200],
    "go left traffic light": [245, 130, 48],
    "warning left traffic light": [145, 30, 180],
    "go forward traffic light": [70, 240, 240],
    "go": [240, 50, 230],
    "stop": [210, 245, 60],
    "top left": [250, 190, 212],
    "warning": [0, 128, 128],
    "go left": [220, 190, 255],
    "warning left": [170, 110, 40],
    "go forward": [255, 250, 200],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = (
    "https://vbn.aau.dk/ws/portalfiles/portal/224024952/main"
)
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Jensen Morten Born",
    "Philipsen Mark Philip",
    "Mogelmose Andreas",
    "; Moeslund Thomas",
    "Trivedi Mohan",
]
AUTHORS_CONTACTS: Optional[List[str]] = [
    "mpph@create.aau.dk",
    "anmo@create.aau.dk",
    "tbm@create.aau.dk",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "BEUMER Group, Denmark",
    "Aalborg University, Denmark",
    "University of California, USA",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.beumergroup.com/l/beumer-as-denmark/",
    "https://www.aau.dk/",
    "https://www.hult.edu/",
]

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "times of day": ["day", "night"],
    "__POSTTEXT__": "Additionally, every image marked with its ***sequence*** and ***track frame number*** tags",
}
TAGS: Optional[
    List[Literal["multi-view", "synthetic", "simulation", "multi-camera", "multi-modal"]]
] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
